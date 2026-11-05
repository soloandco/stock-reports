"""홈 화면: 결론 카드, 시장 분위기 줄, 방식별 기록 요약, 최근 알림, 거물 신규 매수 표.

2026-10-02 gen.py 에서 나눴다. 다른 sitegen 모듈은 함수를 이름째 가져오지 않고
「모듈.이름」으로 부른다(테스트가 한 곳만 바꿔 끼워도 모든 호출에 먹게).
"""
from __future__ import annotations

import json
import re

from sitegen import common, config as cfg, strategies


HOME_NEW_ROWS = 10


def _sec_title(name: str) -> str:
    """SEC 회사명 정리: 주 표기 꼬리표(/DE)를 떼고 전부 대문자면 첫 글자만 대문자로."""
    name = re.sub(r"\s*/[A-Z]{2,3}/?\s*$", "", name).strip()
    return name.title() if name.isupper() else name


def _superinvestor_home(data: dict, names: dict, link_prefix: str = "") -> str:
    """「거물 신규 매수」 표. 유명 투자자 2명 이상이 이번 분기에 새로 산 종목 (2026-09-23).

    2026-11-05 에 홈에서 시장 현황 맨 아래로 옮겼다(사용자 승인: 홈은 오늘 살 종목만).
    names: 관찰 종목 {티커: 기업명}. 관찰 중이면 종목 페이지로 잇는다. 자료가 없으면 빈 문자열.
    link_prefix: 사이트 맨 위까지의 상대 경로.
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
        (f'<a class="m-chip13" href="{link_prefix}watchlist/{r["ticker"]}/">' if r["ticker"] in names
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

# ── 첫 화면 (2026-09-23 개편, 2026-11-05 사용자 승인으로 다시 줄임) ─────────────
# 홈은 「알림이 나간 매수」만 보여 준다. 스냅샷 판정이 아니라 추천 기록(data/strategy_perf.json)이
# 정본이라 알림과 홈이 어긋나지 않는다. 그 전에는 관찰 목록 판정으로 그려서 알림이 나간 관찰 목록
# 밖 종목(DIS 11-05)은 빠지고, 알림이 안 나간 종목(SW·SNPS)은 올라왔다.
PICK_MAX_CARDS = 8
RECENT_DAYS = 7          # 달력 기준. 신호가 유효한 5거래일과 같다
_WEEKDAY_KO = "월화수목금토일"


def _open_buys(perf: dict) -> list[dict]:
    """알림이 나갔고 아직 안 끝난 매수, 최근 것부터."""
    from datetime import date, timedelta
    try:
        today = date.fromisoformat(str(perf.get("generated", ""))[:10])
    except ValueError:
        return []
    start = (today - timedelta(days=RECENT_DAYS)).isoformat()
    rows = [t for t in perf.get("trades") or []
            if t.get("pushed") and not t.get("closed") and str(t.get("ts", ""))[:10] >= start
            and t.get("entry") is not None]
    return sorted(rows, key=lambda t: str(t.get("ts", "")), reverse=True)


def _buy_card(t: dict, names: dict, alert_pages: dict, today: str) -> str:
    """매수 카드 한 장: 티커·이름·방식 / 가격·손절·날짜."""
    tk = t["ticker"]
    name = common._name_of(tk, names)
    name = "" if name == tk else name
    name_html = f'<span class="m-card__name">{name}</span>' if name else ""
    day = str(t.get("ts", ""))[:10]
    when = "오늘" if day == today else common._md(day)
    body = (f'<div class="m-card__head"><b class="m-card__ticker">{tk}</b>{name_html}'
            f'<span class="m-card__how">{common._STRAT_LABEL.get(t.get("strategy"), "")}</span></div>'
            f'<div class="m-card__line"><b>${t["entry"]:,.2f}</b>'
            f'<span>손절 <b class="m-neg">${t["stop"]:,.2f}</b></span><span class="m-muted">{when}</span></div>')
    href = f"watchlist/{tk}/" if tk in names else alert_pages.get(tk)
    if href:
        return f'<a class="m-card" href="{href}">{body}</a>'
    return f'<div class="m-card">{body}</div>'


def _conclusion_section(perf: dict, snaps: list[dict], names: dict, alerts: list[dict],
                        max_cards: int = PICK_MAX_CARDS) -> str:
    """홈 첫 화면: 오늘 살 종목 수 → 매수 카드 → 매수 상태 전체로 가는 한 줄."""
    buys = _open_buys(perf)
    today = str(perf.get("generated", ""))[:10]
    n_today = sum(1 for t in buys if str(t.get("ts", ""))[:10] == today)
    pages: dict = {}
    for a in alerts:
        pages.setdefault(a["ticker"], f'alerts/{a["fname"][:-3]}/')
    hero = (f'<div class="m-hero__n">{n_today}<small>종목</small></div>' if n_today
            else '<div class="m-hero__n m-hero__n--none">없음</div>')
    out = [f'<div class="m-hero"><div class="m-hero__k">오늘 살 종목</div>{hero}</div>']
    if buys:
        out.append('<div class="m-cards">'
                   + "".join(_buy_card(t, names, pages, today) for t in buys[:max_cards]) + '</div>')
    n_buy = sum(1 for s in snaps if s["verdict"] in common._BUY_STATES)
    if n_buy:
        out.append(f'<a class="m-row" href="watchlist/#buy"><span>매수 상태 전체 <b>{n_buy}</b>종목</span>'
                   '<span class="m-go">›</span></a>')
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
    """홈 맨 위 한 줄: 공포·탐욕 지수. 자료가 없으면 ""."""
    fg = fear.get("cnn_fear_greed") or {}
    if fg.get("score") is None:
        return ""
    cls = {"extreme fear": "m-wrn", "fear": "m-wrn", "greed": "m-pos",
           "extreme greed": "m-pos"}.get(str(fg.get("rating", "")).lower(), "")
    return ('<a class="m-mkt" href="fear-index/"><span>시장 분위기</span>'
            f'<b class="{cls}">{fg.get("rating_ko", "")} {fg["score"]:.0f}</b><span class="m-go">›</span></a>\n')


def _strategy_box(perf: dict) -> str:
    """홈 「추천대로 샀다면」: 금액 합계와 건수만 (자세한 것은 추천 기록)."""
    money = perf.get("money") or {}
    if not money:
        return ""
    total = sum(m.get("total_won", 0) for m in money.values())
    closed = sum(m.get("closed", 0) for m in money.values())
    open_n = sum(m.get("open", 0) + m.get("pending", 0) for m in money.values())
    cls = "m-pos" if total >= 0 else "m-neg"
    return (f'<a class="m-row" href="strategies/"><span>추천대로 샀다면 <b class="{cls}">{total:+,.0f}원</b></span>'
            f'<span class="m-muted">끝남 {closed} · 진행 {open_n}</span><span class="m-go">›</span></a>\n')


def _dashboard(entries, snaps, alerts, names, positions=None) -> str:
    basis = _basis_label(snaps)
    perf = strategies._collect_strategy_perf()
    return "\n".join([
        "# 오늘",
        "",
        f'<p class="m-basis">{basis}</p>' if basis else "",
        "",
        _market_line(_load_fear_index()),
        _conclusion_section(perf, snaps, names, alerts),
        _strategy_box(perf),
        "",
    ]) + "\n"
