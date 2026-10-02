"""홈 화면: 결론 카드, 시장 분위기 줄, 방식별 기록 요약, 최근 알림, 거물 신규 매수 표.

2026-10-02 gen.py 에서 나눴다. 다른 sitegen 모듈은 함수를 이름째 가져오지 않고
「모듈.이름」으로 부른다(테스트가 한 곳만 바꿔 끼워도 모든 호출에 먹게).
"""
from __future__ import annotations

import json
import re

from sitegen import common, config as cfg, strategies, watch_pages


HOME_NEW_ROWS = 10


def _sec_title(name: str) -> str:
    """SEC 회사명 정리: 주 표기 꼬리표(/DE)를 떼고 전부 대문자면 첫 글자만 대문자로."""
    name = re.sub(r"\s*/[A-Z]{2,3}/?\s*$", "", name).strip()
    return name.title() if name.isupper() else name


def _superinvestor_home(data: dict, names: dict) -> str:
    """홈 「거물 신규 매수」 표. 유명 투자자 2명 이상이 이번 분기에 새로 산 종목 (2026-09-23).

    names: 관찰 종목 {티커: 기업명}. 관찰 중이면 종목 페이지로 잇는다. 자료가 없으면 빈 문자열.
    """
    rows = data.get("top_new")
    if rows is None:
        return ""
    lines = ["## 거물 신규 매수 (13F)", "",
             f"유명 투자자 83곳 중 **2명 이상이 이번 분기에 새로 산 종목** {len(rows)}개 · "
             f"{data.get('period') or '?'} 기준 (분기 말 뒤 최대 45일 늦게 공개)", ""]
    if not rows:
        return "\n".join(lines + ["이번 분기에는 없습니다.", ""])
    # 폰 첫 화면에서는 칩 한 줄, 누가 샀는지는 접힌 표에서 (2026-09-23 모바일 개편)
    chips = "".join(
        (f'<a class="m-chip13" href="watchlist/{r["ticker"]}/">' if r["ticker"] in names
         else '<span class="m-chip13">')
        + f'{r["ticker"]}<small>{len(r["buyers"])}명</small>'
        + ("</a>" if r["ticker"] in names else "</span>")
        for r in rows[:HOME_NEW_ROWS])
    lines += [f'<div class="m-chips13">{chips}</div>', "",
              '??? note "누가 샀는지 보기"', "",
              "    | 종목 | 새로 산 투자자 | 인원 |", "    |------|----------------|-----:|"]
    for r in rows[:HOME_NEW_ROWS]:
        t = r["ticker"]
        label = f"[**{t}**](watchlist/{t}.md)" if t in names else f"**{t}**"
        nm = names.get(t) or _sec_title(r.get("name") or "")
        who = " · ".join(f"{b['name'].split(' - ')[0]} {b['weight'] * 100:.1f}%" for b in r["buyers"])
        lines.append(f"    | {label}<br>{nm} | {who} | {len(r['buyers'])} |")
    if len(rows) > HOME_NEW_ROWS:
        lines.append(f"    | 외 {len(rows) - HOME_NEW_ROWS}종목 | | |")
    lines += ["", '<p class="m-fine">참고 정보이며 매수 신호가 아닙니다. '
              "검증(2026-09-23, 11년 1만 건)에서 여러 기관이 새로 산 종목의 매수 신호는 성적이 좋은 쪽이었지만 "
              "기준에 못 미쳤습니다.</p>", ""]
    return "\n".join(lines)


# --- 페이지 빌더 ---

# ── 모바일 화면 부품 (2026-09-23 개편) ─────────────────────────────────
# 시안: stock-agent/docs/mockups/site-mobile-wireframe/index.html
# 홈은 「오늘 새로 살 만한 종목」(신호 5일 이내)만 크게, 지난 신호는 한 줄로 접는다.
# 카드에는 판단에 쓰는 숫자 셋(손절까지 · 첫 저항까지 · 신호 경과일)만 둔다.
# 새 계산·새 점수 없이 최신 스냅샷 frontmatter 값만 쓴다.
# 카드 순서는 알림 슬롯 배분(monitor._entry_priority)과 같다: 주봉 신고가영역
# 우선, 동률이면 저항 손익비 높은 순. 만료 후보(D+5 초과)는 맨 뒤로.
_PICK_WEEKLY_RANK = {"신고가영역": 0, "저항대아래": 1}          # monitor._WEEKLY_RANK 와 동일
PICK_MAX_CARDS = 8
NEAR_RESIST_PCT = 3.0     # 첫 저항이 이보다 가까우면 카드에 주황 경고 줄
_WEEKDAY_KO = "월화수목금토일"


def _pick_priority(snap: dict) -> tuple:
    """카드 순서. 만료는 뒤로, 주봉 신고가영역 우선, 그다음 저항 손익비.

    ⚠ 2026-09-04 에 **등급(매수후보 우선) 항을 뺐다.** 8/8 이 더 낫다는 근거가
    없다 (충족 조건 8개 +0.148R < 7개 +0.189R < 6개 +0.208R, n=13,187).
    알림 슬롯 배분(monitor._entry_priority)도 등급을 쓰지 않는다. 두 순서를
    같게 유지할 것.
    """
    rr = common._num(snap.get("rr")) or 0.0
    return (common._is_expired(snap),
            _PICK_WEEKLY_RANK.get(snap.get("weekly_pos") or "", 2), -rr, snap["ticker"])


def _first_resist(snap: dict) -> "tuple[str, str]":
    """(첫 저항까지 표기, 색 클래스). 신고가 영역이면 머리 위 저항이 없다."""
    if (snap.get("weekly_pos") or "") == "신고가영역":
        return "없음", "m-pos"
    w = common._num(snap.get("weekly_pct"))
    if w is None:
        return "—", ""
    return common._pct_text(w), ("m-wrn" if w < NEAR_RESIST_PCT else "m-pos")


def _stop_pct(snap: dict) -> "float | None":
    price, stop = common._num(snap.get("price")), common._num(snap.get("stop"))
    if not price or stop is None:
        return None
    return (stop - price) / price * 100


def _fresh_card(snap: dict, name: str) -> str:
    """홈 카드. 숫자 셋만. 누르면 그 종목의 관찰 페이지로 간다."""
    t = snap["ticker"]
    sp = _stop_pct(snap)
    rtxt, rcls = _first_resist(snap)
    w = common._num(snap.get("weekly_pct"))
    warn = ('<div class="m-card__warn">머리 위 저항이 바로 앞</div>'
            if rcls == "m-wrn" and w is not None else "")
    name_html = f'<span class="m-card__name">{name}</span>' if name else ""
    return (
        f'<a class="m-card" href="watchlist/{t}/">'
        f'<div class="m-card__head"><b class="m-card__ticker">{t}</b>{name_html}'
        f'<span class="verdict verdict-buy">{common._display_verdict(snap["verdict"])}</span></div>'
        f'<div class="m-card__nums">'
        f'<div><span>손절까지</span><b class="m-neg">{common._pct_text(sp) if sp is not None else "—"}</b></div>'
        f'<div><span>첫 저항까지</span><b class="{rcls}">{rtxt}</b></div>'
        f'<div><span>신호</span><b>{common._signal_label(snap) or "—"}</b></div>'
        f'</div>{warn}</a>'
    )


def _conclusion_section(snaps: list[dict], names: dict, positions: "list[dict] | None" = None,
                        max_cards: int = PICK_MAX_CARDS) -> str:
    """홈 첫 화면: 새 신호 수(큰 숫자) → 새 신호 카드 → 지난 신호 한 줄."""
    buys = sorted((s for s in snaps if s["verdict"] in common._BUY_STATES), key=_pick_priority)
    fresh = [s for s in buys if not common._is_expired(s)]
    stale = [s for s in buys if common._is_expired(s)]
    out = [
        '<div class="m-hero">'
        '<div class="m-hero__k">오늘 새로 살 만한 종목</div>'
        f'<div class="m-hero__n">{len(fresh)}<small>종목</small></div>'
        f'<div class="m-hero__s">신호 {common.CANDIDATE_FRESH_MAX_DAYS}일 이내 · 매수 상태 {len(buys)}종목 중</div>'
        '</div>'
    ]
    if fresh:
        out.append('<div class="m-cards">'
                   + "".join(_fresh_card(s, names.get(s["ticker"], "")) for s in fresh[:max_cards])
                   + '</div>')
    else:
        out.append('<p class="m-empty">오늘 새 신호는 없습니다.</p>')
    if stale:
        head = "·".join(s["ticker"] for s in stale[:3]) + (" 외" if len(stale) > 3 else "")
        out.append(
            '<a class="m-row" href="watchlist/#buy">'
            f'<span>이미 지난 신호 <b>{len(stale)}</b>종목</span>'
            f'<span class="m-muted">추격 비추천 · {head}</span><span class="m-go">›</span></a>')
    return "\n".join(out) + "\n"


def _basis_label(snaps: list[dict]) -> str:
    """'9월 23일(화) 기준'. 스냅샷 날짜가 없으면 ""."""
    basis = max((s.get("created", "") for s in snaps), default="")
    try:
        from datetime import date
        d = date.fromisoformat(str(basis))
    except ValueError:
        return ""
    return f"{d.month}월 {d.day}일({_WEEKDAY_KO[d.weekday()]}) 기준"


def _load_fear_index() -> dict:
    try:
        return json.loads(cfg.FEAR_INDEX_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _market_line(fear: dict) -> str:
    """홈 맨 위 한 줄: 공포·탐욕 지수와 VIX. 자료가 없으면 ""."""
    fg, vix = fear.get("cnn_fear_greed") or {}, fear.get("vix") or {}
    bits = []
    if fg.get("score") is not None:
        cls = {"extreme fear": "m-wrn", "fear": "m-wrn", "greed": "m-pos",
               "extreme greed": "m-pos"}.get(str(fg.get("rating", "")).lower(), "")
        bits.append(f'<b class="{cls}">{fg.get("rating_ko", "")} {fg["score"]:.0f}</b>')
    if vix.get("value") is not None:
        bits.append(f'<span>VIX {vix["value"]:.1f} {vix.get("grade", "")}</span>')
    if not bits:
        return ""
    return ('<a class="m-mkt" href="fear-index/"><span>시장 분위기</span>'
            + '<span class="m-dot">·</span>'.join(bits) + '<span class="m-go">›</span></a>\n')


def _strategy_box(perf: dict) -> str:
    """홈 「추천 기록」: 지금 켜진 방식의 완료·평균·진행만 (방식별 기록 페이지 요약)."""
    active = perf.get("active")
    periods = [p for p in (perf.get("periods") or []) if p.get("strategy") == active]
    if not active or not periods:
        return ""
    s = periods[-1].get("active") or {}
    if active == "both":
        # 둘 다 켜진 기간 (2026-09-24): other 가 단타 알림 거래다. 두 방식을 합쳐 보여 준다
        o = periods[-1].get("other") or {}
        n = s.get("closed", 0) + o.get("closed", 0)
        tot = ((s.get("mean_r") or 0) * s.get("closed", 0)
               + (o.get("mean_r") or 0) * o.get("closed", 0))
        s = {"closed": n, "open": s.get("open", 0) + o.get("open", 0),
             "mean_r": tot / n if n else None}
    r = s.get("mean_r")
    rtxt = f"{r:+.2f}R" if r is not None else "—"
    rcls = "" if r is None else ("m-pos" if r >= 0 else "m-neg")
    return (
        '<div class="m-sec"><span>추천 기록</span><a href="strategies/">전체 ›</a></div>\n'
        '<a class="m-box m-strat" href="strategies/">'
        f'<div class="m-kv"><span>지금 켜진 방식</span><b>{common._STRAT_LABEL.get(active, active)}</b>'
        f'<span class="m-muted">{common._md(perf.get("active_since", ""))}부터</span></div>'
        '<div class="m-stat3">'
        f'<div><b>{s.get("closed", 0)}</b><span>완료</span></div>'
        f'<div><b class="{rcls}">{rtxt}</b><span>평균</span></div>'
        f'<div><b>{s.get("open", 0)}</b><span>진행 중</span></div>'
        '</div></a>\n')


def _alert_name(alert: str) -> str:
    """'🔒 본전 스톱' → '본전 스톱' (앞 기호 떼기)."""
    head, _, rest = str(alert).partition(" ")
    return rest if rest and not any(ch.isalnum() for ch in head) else str(alert)


def _recent_alerts(alerts: list[dict], n: int = 3) -> str:
    if not alerts:
        return ""
    rows = "".join(
        f'<a class="m-li" href="alerts/{a["fname"][:-3]}/">'
        f'<span class="m-li__d">{common._md(a["created"])}</span><b>{a["ticker"]}</b>'
        f'<span>{_alert_name(a["alert"])}</span></a>'
        for a in alerts[:n])
    return ('<div class="m-sec"><span>최근 알림</span><a href="alerts/">전체 ›</a></div>\n'
            f'<div class="m-box m-list">{rows}</div>\n')


def _dashboard(entries, snaps, alerts, names, positions=None) -> str:
    basis = _basis_label(snaps)
    lines = [
        "# 주식 리포트",
        "",
        f'<p class="m-basis">{basis}</p>' if basis else "",
        "",
        _market_line(_load_fear_index()),
        _conclusion_section(snaps, names, positions),
        _strategy_box(strategies._collect_strategy_perf()),
        _recent_alerts(alerts),
        _superinvestor_home(watch_pages._load_superinvestors(), names),
        "",
    ]
    lines += [
        "## 용어 설명",
        "",
        '??? info "📘 Stage (Weinstein 스테이지)란?"',
        "    주가 생명주기를 4단계로 분류하는 Stan Weinstein의 프레임워크. **100일 지수이동평균(EMA)** 방향과 가격 위치로 판단합니다 "
        "(원전은 30주≈150일 단순이동평균, 2026-09-28 EMA 로 전환).",
        "",
        "    | Stage | 명칭 | MA 방향 | 가격 위치 | 대응 |",
        "    |-------|------|---------|---------|------|",
        "    | **1** | 바닥 다지기 | 수평 | MA 위아래 | 대기 |",
        "    | **2** | 상승 국면 | 우상향 | MA 위 | **매수 구간** |",
        "    | **3** | 천장 분배 | 수평화 | MA 근처 | 매도 준비 |",
        "    | **4** | 하락 국면 | 우하향 | MA 아래 | 절대 금지 |",
        "",
        "    이 시스템은 **Stage 2** 종목만 매수 후보로 분류합니다.",
        "",
        '??? info "📘 TT (Trend Template — 상승 구조 7조건)란?"',
        "    Mark Minervini가 정의한 상승 구조 체크리스트. **충족 조건 수 / 7** 로 점수화.",
        "",
        "    | # | 조건 |",
        "    |---|------|",
        "    | 1 | 현재가 > 100일 EMA, 200일 EMA |",
        "    | 2 | 100일 EMA > 200일 EMA |",
        "    | 3 | 200일 EMA 최소 1개월째 상승 중 |",
        "    | 4 | 현재가 > 20일 EMA |",
        "    | 5 | 현재가 ≥ 52주 저점 × 1.25 (+25% 이상) |",
        "    | 6 | 현재가 ≥ 52주 고점 × 0.75 (-25% 이내) |",
        "    | 7 | RS Rating(상대강도 등급) ≥ 70 |",
        "",
        "    **5/7 이상**: 매수 · **4/7 이하**: 기준미달. "
        "조건 개수는 등급이 아닙니다 — 11년 13,187건에서 만점(+0.148R)이 "
        "하한(+0.208R)보다 나았다는 근거가 없습니다. "
        "2026-09-10 에 `SMA50 > SMA150·SMA200` 조건을 뺐습니다 "
        "(성적 변화 없음, 예외 규칙 하나가 함께 사라짐). "
        "2026-09-28 에 판정선을 단순이동평균 50·150·200일에서 "
        "지수이동평균(EMA) 20·100·200일로 바꿨습니다 "
        "(과거 11년 측정에서는 건당 +0.30R → +0.26R 로 낮았습니다).",
        "",
        '??? info "📘 진입 게이팅 — 점수가 만점이어도 매수불가가 되는 4가지"',
        "    Stage·TT 점수와 별개로, 아래 조건에 걸리면 매수에서 제외됩니다 (2026-06-11 도입).",
        "",
        "    | 게이트 | 조건 | 사유 표기 |",
        "    |--------|------|----------|",
        "    | 시장 국면 | 지수 MA 정렬이 하락/횡보 | 매수불가 (시장국면) |",
        "    | DD 누적 | 4주 내 Distribution Day(기관 매도일) 5회 이상 | 매수불가 (시장국면) |",
        "    | 지수 과열 | 지수가 20일 EMA 대비 +15% 초과 (파라볼릭) | 매수불가 (시장국면) |",
        "    | 종목 과열 | 20일 EMA +25% 이격 또는 RSI > 90 | 매수불가 (과열) |",
        "    | 변동성 | 2N ATR 손절폭이 진입가의 8% 초과 | 매수불가 (변동성과대) |",
        "",
        "    매수 후 **+1.5R** 도달 시 손절선을 본전으로 올리라는 🔒 본전 스톱 알림이 발송됩니다.",
        "",
    ]
    return "\n".join(lines) + "\n"
