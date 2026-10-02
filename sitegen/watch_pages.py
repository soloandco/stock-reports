"""관찰 종목 페이지: 공개용 정리, 차트 데이터, 판정 근거, 거물 투자자·가격 수준 칸, 관찰 목록.

2026-10-02 gen.py 에서 나눴다. 다른 sitegen 모듈은 함수를 이름째 가져오지 않고
「모듈.이름」으로 부른다(테스트가 한 곳만 바꿔 끼워도 모든 호출에 먹게).
"""
from __future__ import annotations

import json
import re
import shutil

from sitegen import common, config as cfg


SUPERINV_ROWS = 10
SUPERINV_FIRST = 3      # 관찰 페이지에서 접지 않고 보이는 줄 수


# --- 소스 → 출력 복사 + 메타 수집 ---

# 실계좌 정보 프론트매터 키 — 공개 복사본에서 제거 ("리포트만 공개" 정책)
_PRIVATE_FM_KEYS = {"held", "buy_price", "buy_stop", "entry_price",
                    "entry_stop", "entry_date", "trail_stop", "alert_above", "shares"}
_PRIVATE_BLOCK_RE = re.compile(
    r"<!--\s*private\s*-->.*?<!--\s*/private\s*-->\n?", re.DOTALL)


def _sanitize_public_md(text: str) -> str:
    """공개 복사 전 실계좌 흔적 제거.

    - 프론트매터: _PRIVATE_FM_KEYS 최상위 스칼라 줄 삭제
    - 본문: <!-- private --> ... <!-- /private --> 블록 삭제
    """
    m = re.match(r"^---\n(.*?\n)---", text, re.DOTALL)
    if m:
        kept = [ln for ln in m.group(1).splitlines(keepends=True)
                if not (":" in ln and not ln.startswith((" ", "-"))
                        and ln.partition(":")[0].strip() in _PRIVATE_FM_KEYS)]
        text = f"---\n{''.join(kept)}---" + text[m.end():]
    return _PRIVATE_BLOCK_RE.sub("", text)


# 차트 자리. JS(stock-chart.js)가 data-src를 읽어 채운다. 데이터를 못 받으면
# 이 요소는 스스로 사라져 빈 상자가 남지 않는다.
_CHART_BLOCK = """
## 차트

<div class="stock-chart" data-src="../charts/{ticker}.json"{attrs}></div>

<details class="stock-chart-note"><summary>매물벽·지지대는 검증에서 무작위 선과 같았습니다. 아래 두 칸도 매수 신호 아님 · 자세히</summary>
<p>추세선·매물벽(저항)·지지대·주봉 저항을 함께 표시합니다. 매물벽·지지대는 위치 참고용이며, 검증(2026-09-07)에서 받치고 막는 비율이 무작위 선과 같았습니다. 아래 칸은 일봉 종가 위치로 추정한 수급 누적선입니다(매수 신호 아님). 맨 아래 칸은 물린 비율(최근 1년 거래량 중 현재가보다 비싸게 거래된 비중)입니다. 측정(2026-09-14, 11년 620종목)에서 이 비율은 「1년 가격 범위의 어디에 있나」와 구분되지 않았고, 앞으로의 수익을 가르지 못했습니다(층화 차이 −0.02R·CI 0 포함). 심리 지도라기보다 위치 표시로 읽으세요. 손가락으로 확대·이동할 수 있습니다.</p>
</details>
"""


def _write_chart_data(entries) -> int:
    """종목별 차트 데이터(JSON)를 쓰고 성공 건수를 반환한다.

    실패한 종목은 건너뛴다 — 차트는 페이지의 부속물이고, 한 종목의 시세 조회
    실패가 사이트 생성 전체를 막으면 안 된다.
    """
    import sys
    sys.path.insert(0, str(cfg.ROOT.parent))
    try:
        from core.chart_data import WATCH_CHART_DAYS, build_chart_payload
        from core.chart_lines import parse_lines
    except Exception as exc:      # 분석 코드가 없는 환경(CI 등)에서는 조용히 생략
        print(f"  차트 데이터 생략 — {exc}")
        return 0

    auto = {}
    auto_path = cfg.ROOT.parent / "data" / "auto_lines.json"
    if auto_path.exists():
        try:
            auto = json.loads(auto_path.read_text(encoding="utf-8"))
        except Exception:
            auto = {}

    # 실제로 보낸 알림 원장 (2026-10-02). 차트에 매수·청산 날짜를 찍는다. 없거나 깨진 줄은 건너뛴다.
    alerts_by_ticker: dict[str, list] = {}
    ledger = cfg.ROOT.parent / "data" / "alert_ledger.jsonl"
    if ledger.exists():
        for raw in ledger.read_text(encoding="utf-8").splitlines():
            try:
                row = json.loads(raw)
            except Exception:
                continue
            if isinstance(row, dict) and row.get("ticker"):
                alerts_by_ticker.setdefault(row["ticker"], []).append(row)

    cfg.OUT_WL_CHARTS.mkdir(parents=True, exist_ok=True)
    ok = 0
    for ticker, market, _name, _fname in entries:
        lines, _errs = parse_lines(auto.get(ticker) or [])
        payload = build_chart_payload(ticker, market, lines=lines, days=WATCH_CHART_DAYS,
                                      alerts=alerts_by_ticker.get(ticker))
        if not payload:
            continue
        # 구분자를 붙이지 않아 파일을 작게 유지한다 (48종목이 매일 갱신된다)
        (cfg.OUT_WL_CHARTS / f"{ticker}.json").write_text(
            json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8")
        ok += 1
    return ok


def _load_superinvestors() -> dict:
    """data/superinvestors.json 로드. 없거나 깨졌으면 {} (절을 그리지 않는다)."""
    try:
        return json.loads(cfg.SUPERINV_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _usd(v: float) -> str:
    return f"${v:,.0f}" if v >= 100 else f"${v:,.2f}"


def _cost_cell(cost: "dict | None", price: "float | None") -> str:
    """추정 평단 칸. 첫 줄 평단(현재가 대비), 둘째 줄 범위. 자료 전부터 보유면 「모름」."""
    if not cost:
        return ""
    if not cost.get("known"):
        since = (cost.get("since") or "")[:7]
        return f"모름<br>첫 신고({since}) 전부터 보유" if since else "모름"
    avg = cost["avg"]
    gain = f" ({(price / avg - 1) * 100:+.0f}%)" if price and avg else ""
    return f"{_usd(avg)}{gain}<br>{_usd(cost['low'])}~{_usd(cost['high'])}"


def _superinvestor_block(ticker: str, data: dict) -> str:
    """관찰 페이지 「거물 투자자(13F)」 절. 자료에 없는 종목은 빈 문자열.

    참고 표시다. 판정·알림에 쓰지 않는다. 성적과의 관계는 사전등록 id 40 에서 잰다.
    """
    t = (data.get("tickers") or {}).get(ticker)
    if t is None:
        return ""
    period = data.get("period") or "?"
    rows = t.get("famous") or []
    lines = ["", "## 거물 투자자 (13F)", ""]
    head = (f"유명 투자자 83곳 중 **{t.get('famous_holders', 0)}곳 보유**"
            f" · 이번 분기 신규 **{t.get('famous_new', 0)}곳**"
            f" · 집중 투자 기관 {t.get('conc_holders', 0)}곳 보유(신규 {t.get('conc_new', 0)}곳)")
    lines.append(head)
    if rows:
        # 폰에서는 비중 큰 셋만 먼저 보이고 나머지는 접는다 (2026-09-23 모바일 개편)
        head_row = ["| 투자자 | 비중 | 구분 | 추정 평단 |", "|--------|-----:|------|-----------|"]
        cells = [f"| {r['name']} | {r['weight'] * 100:.1f}% | {'신규' if r.get('new') else '보유'} "
                 f"| {_cost_cell(r.get('cost'), t.get('price'))} |" for r in rows[:SUPERINV_ROWS]]
        if len(rows) > SUPERINV_ROWS:
            cells.append(f"| 외 {len(rows) - SUPERINV_ROWS}곳 | | | |")
        lines += ["", *head_row, *cells[:SUPERINV_FIRST]]
        if cells[SUPERINV_FIRST:]:
            lines += ["", f'??? note "나머지 {len(rows) - SUPERINV_FIRST}곳 보기"', "",
                      *("    " + x for x in head_row + cells[SUPERINV_FIRST:])]
    lines += ["", f'<details class="stock-chart-note"><summary>{period} 기준 공시(최대 45일 늦음). '
              "참고 정보이며 매수 신호가 아닙니다 · 자세히</summary>",
              f'<p>{period} 기준 보유를 SEC 13F 공시로 셉니다(공시 반영 '
              f'{data.get("as_of", "?")}). 분기 말 뒤 최대 45일 늦게 공개되고 매입 단가는 없습니다. '
              "비중 1% 미만 보유는 세지 않습니다. 추정 평단은 주식이 늘어난 분기마다 그 분기 거래량 가중 "
              "평균가에 샀다고 보고 쌓은 값이고, 둘째 줄은 그 분기 최저가~최고가로 잡은 범위입니다. "
              "괄호는 현재가 대비입니다. 그 투자자의 첫 13F 신고(가장 이르면 2013년) 전부터 들고 있던 "
              "종목은 매입가를 알 수 없어 「모름」입니다. 버크셔 실제 원가와 대조(2019~2021년)하면 장내에서 "
              "산 종목은 대부분 ±6% 안이었고, 판 뒤에는 10~16%까지 벌어졌습니다. 종목 코드가 바뀐 경우"
              "(구글→알파벳 등)는 이어서 계산합니다. 신주인수권 행사로 받은 주식은 크게 틀릴 수 있습니다. "
              "유명 투자자 명단은 Dataroma, 집중 투자 기관은 "
              "보유 5~50종목·총액 5억 달러 이상인 기관입니다. 검증(2026-09-23, 11년 1만 건)에서 보유 기관 수는 "
              "매수 신호 성적과 무관했고, 여러 기관이 새로 산 종목은 좋은 쪽이었지만 기준에 못 미쳤습니다. "
              "참고 정보이며 매수 신호가 아닙니다.</p></details>", ""]
    return "\n".join(lines)


def _load_valuation() -> dict:
    """data/valuation_band.json 로드. 없거나 깨졌으면 {} (절을 그리지 않는다)."""
    try:
        return json.loads(cfg.VALUATION_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {}


# 자기 과거 3년 밴드에서 이 분위 이하면 「싼 편」, 초과면 「비싼 편」. 가운데는 「보통」.
_VAL_CHEAP, _VAL_DEAR = 33, 66
# 측정 결과 한 줄 (id 22·41). 🚫 재측정 없이 문구를 바꾸지 말 것.
VAL_EVIDENCE = ("검증(2026-09-27, 11년 매수 신호 7,398건): 자기 과거 대비 가장 싼 5분의 1에서 나온 신호는 "
                "건당 +0.43R, 가장 비싼 5분의 1은 +0.19R 이었습니다. 방향은 맞았지만 채택 기준에 "
                "못 미쳐 판정·알림에는 쓰지 않습니다.")


def _valuation_block(ticker: str, snap: "dict | None", data: dict) -> str:
    """관찰 페이지 「가격 수준」 절. 자료가 없는 종목(ETF 등)은 빈 문자열.

    지금 P/S 는 **스냅샷 현재가**로 다시 계산한다(판정과 같은 가격). 밴드·매출·주식수는
    주 1회 갱신 파일에서 읽는다. 참고 표시다. 판정·알림에 쓰지 않는다.
    """
    import bisect
    t = (data.get("tickers") or {}).get(ticker)
    price = common._num((snap or {}).get("price"))
    if not t or not price or not t.get("ttm") or not t.get("band"):
        return ""
    band = t["band"]
    ps = price * t["shares"] / t["ttm"]
    if ps < band[0]:
        where = "3년 중 가장 낮은 수준보다 아래"
    elif ps > band[-1]:
        where = "3년 중 가장 높은 수준보다 위"
    else:
        pct = round(bisect.bisect_left(band, ps) / (len(band) - 1) * 100)
        label = ("싼 편" if pct <= _VAL_CHEAP else "비싼 편" if pct > _VAL_DEAR else "보통")
        where = f"과거 3년 중 **{label}** (하위 {pct}%)"
    rows = [f"| 회사값 (P/S) | **{ps:.0f}배** · {where}<br>3년 범위 {band[0]:.0f}~{band[-1]:.0f}배 |"]
    if t.get("growth") is not None:
        rows.append(f"| 매출 성장 | 전년 같은 분기 대비 **{t['growth']:+.1f}%**"
                    f" ({(t.get('growth_q') or '')[:7]} 분기) |")
    gap = common._num((snap or {}).get("gap"))
    if gap is not None:
        rows.append(f"| 20일 EMA 대비 | **{gap:+.1f}%** (15% 넘으면 매수 보류) |")
    return "\n".join([
        "", "## 가격 수준 (참고)", "", "| 항목 | 지금 |", "|------|------|", *rows, "",
        '<details class="stock-chart-note"><summary>참고 정보이며 매수 신호가 아닙니다 · 자세히</summary>',
        f"<p>P/S 는 회사값(시가총액)을 최근 1년 매출로 나눈 값입니다. 자기 과거 3년 분포와 비교해 "
        f"아래 3분의 1은 싼 편, 위 3분의 1은 비싼 편으로 적습니다. 매출·주식수·범위는 매주 일요일 "
        f"갱신합니다({data.get('as_of', '?')}). 매출은 SEC 공시, 주식수는 액면분할을 반영했습니다. "
        f"{VAL_EVIDENCE}</p></details>", ""])


def _split_at_first_h2(text: str) -> tuple[str, str]:
    """(머리, 첫 H2부터 끝). H2가 없으면 (전체, "")."""
    idx = text.find("\n## ")
    if idx == -1:
        return text.rstrip() + "\n", ""
    return text[:idx], text[idx:]


# ── 관찰 페이지 모바일 정리 (2026-09-23) ──────────────────────────────────
# 워치리스트 본문은 등록 때 손으로 쓴 메모라 날짜가 지나면 지금 판정과 어긋난다
# (GOOGL 은 5월 메모 「TT 8/8 매수 후보 1순위」가 맨 위에 보였다). 원본은 그대로 두고
# 공개 사본에서만 접는다. 「카톡 알림」 절은 없앤 기능의 설명이라 뺀다.
_KAKAO_SECTION_RE = re.compile(r"\n## [^\n]*카톡[^\n]*\n.*?(?=\n## |\Z)", re.DOTALL)


def _fold_old_memo(rest: str, written: str) -> str:
    """첫 H2부터의 손 메모를 「지난 분석 메모」 접힘 상자로 감싼다. 빈 메모면 ""."""
    body = _KAKAO_SECTION_RE.sub("", rest).strip("\n")
    if not body.strip():
        return ""
    when = f"작성 {written} · " if written else ""
    indented = "\n".join(("    " + ln) if ln.strip() else "" for ln in body.splitlines())
    return f'\n\n??? note "지난 분석 메모 ({when}지금 판정과 다를 수 있음)"\n\n{indented}\n'


def _chart_attrs(snap: "dict | None") -> str:
    """차트에 손절선을 넘긴다. 매수 상태일 때만 (그 밖의 손절가는 가정값이라 그리지 않는다)."""
    if not snap or snap["verdict"] not in common._BUY_STATES or common._num(snap.get("stop")) is None:
        return ""
    return f' data-stop="{common._num(snap["stop"]):.4f}"'


def _checks(snap: dict) -> str:
    """판정 근거 체크 목록. ✓ 통과 · ! 주의 · ✕ 걸림. 쉬운 말 먼저, 원래 용어는 괄호."""
    items = []
    st = str(snap.get("stage", ""))
    if st:
        items.append(("ok", "상승 추세", f"Stage {st}") if st == "2"
                     else ("no", f"{_STAGE_KO.get(st, '')} 구간".strip(), f"Stage {st}"))
    n, mx = common._num(snap.get("tt")), common._num(snap.get("ttmax", 8))
    if n is not None and mx:
        need = int(mx) - 2          # 7조건이면 5, 옛 8조건이면 6
        items.append(("ok" if n >= need else "no",
                      f"상승 구조 {int(mx)}개 중 {int(n)}개 충족", f"기준 {need}개"))
    if snap["verdict"] in common._BUY_STATES:
        if common._truthy(snap.get("start_unknown", "")):
            items.append(("warn", "시작일 미상", "관찰 등록 전부터 매수 상태"))
        elif common._is_expired(snap):
            items.append(("warn", f"신호 {common._signal_label(snap)}", "추격 비추천"))
        elif common._signal_label(snap):
            items.append(("ok", f"신호 {common.CANDIDATE_FRESH_MAX_DAYS}일 이내", common._signal_label(snap)))
    pos = snap.get("weekly_pos") or ""
    if pos == "신고가영역":
        items.append(("ok", "머리 위 저항 없음", "신고가 영역"))
    elif pos == "돌파후되돌림":
        items.append(("ok", "저항 돌파 후 되돌림 자리", ""))
    elif pos:
        w = common._num(snap.get("weekly_pct"))
        items.append(("warn", "주봉 저항 아래 자리", f"첫 저항 {common._pct_text(w)}" if w is not None else ""))
    if snap["verdict"] == "매수불가" and snap.get("reason"):
        items.append(("no", snap["reason"], ""))
    icon = {"ok": "✓", "warn": "!", "no": "✕"}
    return '<div class="m-box m-checks">' + "".join(
        f'<div class="m-ck m-ck--{k}"><i>{icon[k]}</i><span>{t}'
        + (f' <small>({s})</small>' if s else "") + '</span></div>'
        for k, t, s in items) + '</div>'


def _status_section(snap: "dict | None", name: str) -> str:
    """관찰 페이지 맨 위 결론 카드 + 체크 목록. 최신 스냅샷이 없으면 "".

    매수 상태면 손절 · 목표(5R, 알림과 같은 기준) · 첫 저항 숫자 셋을 스크롤 없이 보인다.
    매수가 아니면 숫자 대신 이유 한 문장.
    """
    if not snap:
        return ""
    stem = snap["fname"][:-3] if snap["fname"].endswith(".md") else snap["fname"]
    market = snap.get("market", "")
    buy = snap["verdict"] in common._BUY_STATES
    kind = "buy" if buy else ("nobuy" if snap["verdict"] == "매수불가" else "sell")
    price, stop = common._num(snap.get("price")), common._num(snap.get("stop"))

    sub = []
    if buy and common._signal_label(snap):
        sub.append(f"신호 {common._signal_label(snap)}")
        if snap.get("since") and not common._truthy(snap.get("start_unknown", "")):
            sub.append(f"{common._md(snap['since'])} 매수 전환")
    if snap.get("created"):
        sub.append(f"기준일 {snap['created']}")

    extra = ""
    if buy and price and stop is not None:
        target = price + (price - stop) * common.REWARD_RATIO
        wprice = common._num(snap.get("wprice"))
        if (snap.get("weekly_pos") or "") == "신고가영역":
            resist = '<b>없음</b><em class="m-pos">신고가 영역</em>'
        elif wprice:
            resist = (f'<b>{common._fmt_price(market, wprice)}</b>'
                      f'<em class="m-pos">{common._pct_text((wprice / price - 1) * 100)}</em>')
        else:
            resist = "<b>—</b>"
        extra = (
            '<div class="m-lv3">'
            f'<div><span>손절</span><b>{common._fmt_price(market, stop)}</b>'
            f'<em class="m-neg">{common._pct_text((stop / price - 1) * 100)}</em></div>'
            f'<div><span>목표 ({common.REWARD_RATIO:g}R)</span><b>{common._fmt_price(market, target)}</b>'
            f'<em class="m-pos">{common._pct_text((target / price - 1) * 100)}</em></div>'
            f'<div><span>첫 저항</span>{resist}</div></div>')
    else:
        why = (_REASON_KO.get(snap.get("reason", ""), "") if kind == "nobuy"
               else _SELL_KO.get(snap["verdict"], ""))
        if why:
            extra = f'<p class="m-why">{why}</p>'

    reason = (f' <span class="verdict-reason">({snap["reason"]})</span>'
              if kind == "nobuy" and snap.get("reason") else "")
    card = (
        f'<div class="m-sum m-sum--{kind}">'
        f'<div class="m-sum__top"><span class="m-sum__px">{common._fmt_price(market, price) if price else ""}</span>'
        f'<span class="verdict verdict-{kind}">{common._display_verdict(snap["verdict"])}</span>{reason}</div>'
        f'<div class="m-sum__sub">{" · ".join(sub)}</div>{extra}</div>')
    return (f"\n{card}\n\n{_checks(snap)}\n\n"
            f'<p class="m-more"><a href="../../snapshots/{stem}/">분석 스냅샷 전체 보기 ›</a></p>\n')


def _collect_watchlist(latest_by_ticker: "dict | None" = None) -> list[tuple[str, str, str, str]]:
    """type=watchlist 만 복사하고 (ticker, market, name, fname) 리스트 반환.

    출력 파일명은 {ticker}.md (ASCII only) — 한글 파일명은 GitHub Pages에서
    URL 인코딩 불일치로 404가 발생하므로 여기서 강제 변환한다.

    원자적 교체: 임시 디렉터리에 복사 완료 후 OUT_WL과 스왑 — 크래시 시
    기존 OUT_WL을 손상시키지 않는다.
    """
    tmp = cfg.OUT_WL.parent / f"{cfg.OUT_WL.name}_tmp"
    common._reset_dir(tmp)
    entries = []
    superinv = _load_superinvestors()
    valuation = _load_valuation()
    for md in sorted(cfg.SRC_WL.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        fm = common._frontmatter(text)
        if fm.get("type") != "watchlist":
            continue
        ticker = fm.get("ticker", md.stem)
        out_name = f"{ticker}.md"   # ASCII-only: 한글 파일명 → 티커만
        name = common._company_name(fm.get("title", ""))
        # 실계좌 필드·private 블록 제거 후 복사 — 원본(비공개)은 그대로 유지
        # 순서: 머리말 → 지금 상태 → 차트 → 가격 수준 → 13F → 지난 분석 메모(접힘) (2026-09-27)
        head, rest = _split_at_first_h2(_sanitize_public_md(text))
        snap = (latest_by_ticker or {}).get(ticker)
        page = (head + _status_section(snap, name)
                + "\n" + _CHART_BLOCK.format(ticker=ticker, attrs=_chart_attrs(snap))
                + _valuation_block(ticker, snap, valuation)
                + _superinvestor_block(ticker, superinv)
                + _fold_old_memo(rest, str(fm.get("updated") or fm.get("created") or "")))
        (tmp / out_name).write_text(page, encoding="utf-8")
        entries.append((ticker, fm.get("market", ""), name, out_name))
    # 모든 파일 복사 완료 후 원자적 교체
    if cfg.OUT_WL.exists():
        shutil.rmtree(cfg.OUT_WL)
    tmp.rename(cfg.OUT_WL)
    return entries


_STAGE_KO = {"1": "바닥 다지기", "2": "상승", "3": "천장 분배", "4": "하락"}
# 매수불가 사유를 한 문장으로 (core/verdict.py 의 REASON_* 와 짝)
_REASON_KO = {
    "과열": "20일 EMA보다 25% 넘게 위에 있거나 RSI가 90을 넘었습니다. 지금은 추격 자리입니다.",
    "이격과대": "20일 EMA보다 15% 넘게 위에 있습니다. 지금은 추격 자리입니다.",
    "기준미달": "상승 구조 조건이 매수 기준에 못 미칩니다.",
    "시장국면": "지수 흐름이 매수에 불리했습니다(옛 규칙).",
    "변동성과대": "손절폭이 넓었습니다(옛 규칙).",
}
_SELL_KO = {"매도후보": "천장 분배 구간입니다. 새로 사지 않는 자리입니다.",
            "매도관찰": "하락 구간입니다. 새로 사지 않는 자리입니다."}
_WL_GROUPS = [("buy", "매수"), ("nobuy", "매수불가"), ("sellc", "매도후보"),
              ("sellw", "매도관찰"), ("none", "분석 전")]
_WL_GROUP_OF = {"매수후보": "buy", "매수관찰": "buy", "매수불가": "nobuy",
                "매도후보": "sellc", "매도관찰": "sellw"}


def _wl_sub(s: dict) -> str:
    """목록 줄 오른쪽 아래 작은 글씨: 매수는 경과, 매수불가는 사유."""
    if s["verdict"] in common._BUY_STATES:
        lab = common._signal_label(s)
        if lab and common._is_expired(s) and lab != "시작일 미상":
            lab += " · 만료"
        return lab
    return s.get("reason", "") if s["verdict"] == "매수불가" else ""


def _watchlist_index(entries, latest_by_ticker=None) -> str:
    """관찰 종목 목록 — 표 대신 줄 카드, 드롭다운 대신 판정 칩 (2026-09-23).

    칩 동작은 watchlist-cards.js. 칩 값은 줄의 data-f 와 같다. 주소 끝 #buy 면
    매수 칩이 켜진 채로 열린다(홈의 「이미 지난 신호」 줄이 여기로 온다).
    """
    latest_by_ticker = latest_by_ticker or {}
    rows = []
    for ticker, market, name, _fname in entries:
        s = latest_by_ticker.get(ticker)
        f = _WL_GROUP_OF.get(s["verdict"], "none") if s else "none"
        fresh = "1" if (f == "buy" and not common._is_expired(s)) else "0"
        rank = [g for g, _ in _WL_GROUPS].index(f)
        days = common._num(s.get("days")) if s else None
        rows.append((rank, fresh == "0", days if days is not None else 9999, ticker,
                     ticker, market, name, s, f, fresh))
    rows.sort()
    counts = {g: sum(1 for r in rows if r[8] == g) for g, _ in _WL_GROUPS}

    chips = [f'<button type="button" class="wl-chip" data-f="all" aria-pressed="true">'
             f'전체 {len(rows)}</button>']
    chips += [f'<button type="button" class="wl-chip" data-f="{g}" aria-pressed="false">'
              f'{label} {counts[g]}</button>' for g, label in _WL_GROUPS if counts[g]]

    body, seen = [], set()
    n_fresh = sum(1 for r in rows if r[8] == "buy" and r[9] == "1")
    n_stale = counts["buy"] - n_fresh
    for *_k, ticker, market, name, s, f, fresh in rows:
        if f == "buy" and fresh not in seen:
            seen.add(fresh)
            body.append(
                f'<div class="wl-grp" data-fresh="{fresh}">새 신호 <b>{n_fresh}</b>'
                f'<span>{common.CANDIDATE_FRESH_MAX_DAYS}일 이내</span></div>' if fresh == "1" else
                f'<div class="wl-grp" data-fresh="0">지난 신호 <b>{n_stale}</b>'
                f'<span>추격 비추천</span></div>')
        if s:
            kind = {"buy": "buy", "nobuy": "nobuy"}.get(f, "sell")
            badge = f'<span class="verdict verdict-{kind}">{common._display_verdict(s["verdict"])}</span>'
            price = common._fmt_price_str(s.get("price", ""), market)
            sub = _wl_sub(s)
        else:
            badge, price, sub = "", "", "분석 전"
        name_html = f'<span class="wl-name">{name}</span>' if name else ""
        sub_html = f'<span class="wl-sub">{sub}</span>' if sub else ""
        body.append(
            f'<a class="wl-row" data-f="{f}" data-fresh="{fresh}" href="{ticker}/">'
            f'<span class="wl-l"><b>{ticker}</b>{name_html}</span>'
            f'<span class="wl-r"><span class="wl-px">{price}</span>{badge}{sub_html}</span></a>')

    return "\n".join([
        f"# 관찰 종목 <small class=\"wl-count\">{len(rows)}</small>",
        "",
        f'<div class="wl-chips" id="wl-chips">{"".join(chips)}</div>',
        "",
        f'<div class="wl-list" id="wl-list" data-active="all">{"".join(body)}</div>',
        "",
        '??? info "판정·경과 표시 설명"',
        "    판정·현재가는 각 종목의 **최신 분석 스냅샷** 기준입니다. "
        "30분마다 상태를 보고, 바뀌면 [알림](../alerts/index.md)이 나갑니다.",
        "",
        "    **경과**는 매수 상태가 이어진 거래일 수입니다(전환일이 오늘). "
        f"매수 추천은 **{common.CANDIDATE_FRESH_MAX_DAYS}일째까지만 유효**합니다. "
        "넘기면 「만료」로 표시하고 푸시 알림도 보내지 않습니다(백테스트상 늦은 진입은 "
        "기대값이 줄어듭니다. 매수 상태를 벗어났다 다시 들어오면 새 추천이 됩니다). "
        "관찰 등록 때 이미 매수 상태였던 종목은 전환일을 알 수 없어 「시작일 미상」으로 "
        "표시하고 새 추천으로 보지 않습니다.",
        "",
    ]) + "\n"
