"""워치리스트·스냅샷·알림을 MkDocs 사이트 docs/로 변환·생성.

소스(메인 저장소):
  ../docs/watchlist/*.md            관찰 종목 (type=watchlist)
  ../docs/watchlist/snapshots/*.md  분석 스냅샷

출력(이 저장소 docs/):
  index.md            홈 포털 (바로 가기 + 용어 설명)
  watchlist/index.md  관찰 종목 목록  + 종목 상세 페이지 복사본
  snapshots/index.md  분석 스냅샷 목록 + 스냅샷 상세 페이지 복사본
  alerts/index.md     알림 타임라인 (이벤트 기록)

알림 상세(alerts/{uid}.md)는 monitor.py가 직접 push하므로 이 스크립트는
**삭제하지 않고** 인덱스만 다시 만든다. (과거 _reset_dir(OUT)가 alerts/를
통째로 지우던 버그를 회피 — 워치리스트/스냅샷 디렉터리만 재생성한다.)

판정 어휘·메뉴 구조 설명: ../docs/verdict-taxonomy.md
"""
from __future__ import annotations

import json
import re
import shutil
from datetime import date
from pathlib import Path

ROOT      = Path(__file__).parent
SRC_WL    = ROOT.parent / "docs" / "watchlist"
SRC_SNAP  = SRC_WL / "snapshots"
SRC_NOTES = ROOT.parent / "docs" / "notes"
OUT       = ROOT / "docs"
OUT_WL    = OUT / "watchlist"
OUT_SNAP  = OUT / "snapshots"
OUT_NOTES = OUT / "notes"
OUT_ALERT = OUT / "alerts"
OUT_POS   = OUT / "positions"
FEAR_INDEX_JSON = ROOT.parent / "data" / "fear_index.json"
SECTOR_JSON = ROOT.parent / "data" / "sector_strength.json"
TRADE_REPORT_JSON = ROOT.parent / "data" / "trade_report.json"
# 방식별 기록 (2026-09-19). monitor._refresh_strategy_perf 가 사이트 생성 직전에 만든다.
STRATEGY_PERF_JSON = ROOT.parent / "data" / "strategy_perf.json"
OUT_STRAT = OUT / "strategies"
# 거물 투자자 13F (2026-09-22). research_13f_build.py / monitor 가 만든다 (core.thirteenf.site_payload).
SUPERINV_JSON = ROOT.parent / "data" / "superinvestors.json"
SUPERINV_ROWS = 10
SUPERINV_FIRST = 3      # 관찰 페이지에서 접지 않고 보이는 줄 수

# 매수 추천 유효기간(거래일). 이 값을 넘긴 신호는 '만료'로 표시된다.
# 2026-09-04부터 매수 두 등급 모두에 적용된다 (옛 구현은 매수후보에만 걸었다).
# core.notifier.CANDIDATE_FRESH_MAX_DAYS와 같아야 한다 — 이 스크립트는 공개 저장소에
# 있어 core를 런타임 의존하지 않으므로 값을 복제하고, 일치 여부는 테스트로 강제한다
# (test_gen.py::test_expiry_threshold_matches_core, 2026-08-11).
CANDIDATE_FRESH_MAX_DAYS = 5

# 공개 사이트 표시값. core의 청산 상수와 일치하는지 test_gen.py에서 검사한다.
REWARD_RATIO = 5.0
MAX_HOLD_DAYS = 90

DISCLAIMER = """\
!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.
"""

SNAP_FILTERS = """\
<div class="snap-filters">
<label class="sf-label" for="sf-verdict">판정</label>
<select class="sf-select" id="sf-verdict" data-f="verdict">
<option value="">전체</option>
<option value="buy">매수</option>
<option value="nobuy">매수불가</option>
</select>
<label class="sf-label" for="sf-stage">Stage</label>
<select class="sf-select" id="sf-stage" data-f="stage">
<option value="">전체</option>
<option value="1">1</option>
<option value="2">2</option>
<option value="3">3</option>
<option value="4">4</option>
</select>
</div>
"""

def _frontmatter(text: str) -> dict:
    """YAML 프론트매터에서 **최상위 단일 줄 스칼라**만 추출(들여쓰기·리스트 줄 무시).

    멀티라인 값은 지원하지 않는다 — 현재 쓰는 필드(verdict, verdict-reason, stage 등)는
    모두 단일 줄이라 충분하다. 멀티라인 필드를 추가하면 PyYAML로 교체할 것.
    """
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" ") and not line.startswith("-"):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"')
    return fm


def _reset_dir(p: Path):
    if p.exists():
        shutil.rmtree(p)
    p.mkdir(parents=True)


# 매수후보·매수관찰은 **같은 칸**이다 (2026-09-04 사용자 결정). 두 등급을 나눌
# 근거가 측정에 없다 — 충족 조건 8개 +0.148R < 7개 +0.189R < 6개 +0.208R
# (n=13,187). 저장 값(frontmatter verdict)은 그대로 두고 표시·필터·정렬만 합친다.
# 클래스 이름이 곧 필터 값이다 (tablesort.js 가 `verdict-<값>` 으로 건다).
_BUY_STATES    = ("매수후보", "매수관찰")   # 저장 값. 연구 파이프라인이 이걸로 층화한다
_VERDICT_KIND  = {"매수후보": "buy", "매수관찰": "buy", "매수불가": "nobuy"}
_VERDICT_ORDER = {"매수후보": 0, "매수관찰": 0, "매수불가": 2}


_BUY_DISPLAY = "매수"


def _display_verdict(verdict: str) -> str:
    """저장 라벨 → 화면 이름. 매수 두 등급만 합친다 (core.verdict.display_label 와 동일 규칙).

    gen.py 는 report-site 에서 단독 실행되므로 core 를 import 하지 않는다.
    규칙을 바꿀 때 양쪽을 함께 고칠 것 (test_verdict_unified.py 가 이쪽을 고정).
    """
    return _BUY_DISPLAY if verdict in _BUY_STATES else verdict


def _verdict_cell(verdict: str, reason: str) -> str:
    """판정을 색상 배지 HTML로 렌더 (사유는 옆에 옅은 글씨).

    md_in_html 확장으로 표 셀 내 인라인 HTML이 렌더된다. .verdict-sort span은
    Tablesort가 textContent로 정렬할 때 우선순위 숫자(0/1/2)를 앞에 붙여
    매수→매수불가 순서를 강제한다.
    """
    kind = _VERDICT_KIND.get(verdict, "nobuy")
    sort_key = _VERDICT_ORDER.get(verdict, 9)
    shown = _display_verdict(verdict)
    badge = f'<span class="verdict-sort">{sort_key}</span><span class="verdict verdict-{kind}">{shown}</span>'
    if reason:
        return f'{badge} <span class="verdict-reason">({reason})</span>'
    return badge


def _truthy(v) -> bool:
    return str(v).strip().lower() == "true"


def _candidate_days_cell(days: str, start_unknown: str = "") -> str:
    """candidate-days 프론트매터 → 'D+N' 셀 (임계 초과는 '만료' — 재전환 대기).

    매수 상태가 아니거나 구형 스냅샷이면 빈 문자열.
    임계는 CANDIDATE_FRESH_MAX_DAYS (모듈 상단, core와 동기화 대상).
    """
    try:
        n = int(days)
    except (TypeError, ValueError):
        return ""
    if n > CANDIDATE_FRESH_MAX_DAYS:
        return f"D+{n} 만료"
    # 관찰 등록 전부터 매수 상태라 경과일이 짧게 보이는 종목 (2026-09-16)
    return "시작일 미상" if _truthy(start_unknown) else f"D+{n}"


def _company_name(title: str) -> str:
    """워치리스트 title('NVIDIA 관찰 종목')에서 기업명만 추출."""
    return re.sub(r"\s*관찰\s*종목\s*$", "", title).strip()


def _fmt_price_str(price: str, market: str) -> str:
    """스냅샷 price 프론트매터(문자열) → 통화 표기. 값 없음/파싱 실패 시 ""."""
    try:
        return _fmt_price(market, float(price))
    except (TypeError, ValueError):
        return ""


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


# ── 관찰 페이지 캔들차트 ──────────────────────────────────────────────────
# 그림(PNG)이 아니라 숫자만 올리고 브라우저가 그린다. 관찰 페이지는 48종목이고
# 매일 갱신돼서 이미지로 커밋하면 한 번에 1.8MB씩 공개 저장소에 쌓인다
# (2026-08-29 실측: 종목당 37KB). 숫자는 종목당 약 6KB다.
OUT_WL_CHARTS = OUT_WL / "charts"

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
    sys.path.insert(0, str(ROOT.parent))
    try:
        from core.chart_data import build_chart_payload
        from core.chart_lines import parse_lines
    except Exception as exc:      # 분석 코드가 없는 환경(CI 등)에서는 조용히 생략
        print(f"  차트 데이터 생략 — {exc}")
        return 0

    auto = {}
    auto_path = ROOT.parent / "data" / "auto_lines.json"
    if auto_path.exists():
        try:
            auto = json.loads(auto_path.read_text(encoding="utf-8"))
        except Exception:
            auto = {}

    OUT_WL_CHARTS.mkdir(parents=True, exist_ok=True)
    ok = 0
    for ticker, market, _name, _fname in entries:
        lines, _errs = parse_lines(auto.get(ticker) or [])
        payload = build_chart_payload(ticker, market, lines=lines)
        if not payload:
            continue
        # 구분자를 붙이지 않아 파일을 작게 유지한다 (48종목이 매일 갱신된다)
        (OUT_WL_CHARTS / f"{ticker}.json").write_text(
            json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8")
        ok += 1
    return ok


def _load_superinvestors() -> dict:
    """data/superinvestors.json 로드. 없거나 깨졌으면 {} (절을 그리지 않는다)."""
    try:
        return json.loads(SUPERINV_JSON.read_text(encoding="utf-8"))
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
    if not snap or snap["verdict"] not in _BUY_STATES or _num(snap.get("stop")) is None:
        return ""
    return f' data-stop="{_num(snap["stop"]):.4f}"'


def _checks(snap: dict) -> str:
    """판정 근거 체크 목록. ✓ 통과 · ! 주의 · ✕ 걸림. 쉬운 말 먼저, 원래 용어는 괄호."""
    items = []
    st = str(snap.get("stage", ""))
    if st:
        items.append(("ok", "상승 추세", f"Stage {st}") if st == "2"
                     else ("no", f"{_STAGE_KO.get(st, '')} 구간".strip(), f"Stage {st}"))
    n, mx = _num(snap.get("tt")), _num(snap.get("ttmax", 8))
    if n is not None and mx:
        need = int(mx) - 2          # 7조건이면 5, 옛 8조건이면 6
        items.append(("ok" if n >= need else "no",
                      f"상승 구조 {int(mx)}개 중 {int(n)}개 충족", f"기준 {need}개"))
    if snap["verdict"] in _BUY_STATES:
        if _truthy(snap.get("start_unknown", "")):
            items.append(("warn", "시작일 미상", "관찰 등록 전부터 매수 상태"))
        elif _is_expired(snap):
            items.append(("warn", f"신호 {_signal_label(snap)}", "추격 비추천"))
        elif _signal_label(snap):
            items.append(("ok", f"신호 {CANDIDATE_FRESH_MAX_DAYS}일 이내", _signal_label(snap)))
    pos = snap.get("weekly_pos") or ""
    if pos == "신고가영역":
        items.append(("ok", "머리 위 저항 없음", "신고가 영역"))
    elif pos == "돌파후되돌림":
        items.append(("ok", "저항 돌파 후 되돌림 자리", ""))
    elif pos:
        w = _num(snap.get("weekly_pct"))
        items.append(("warn", "주봉 저항 아래 자리", f"첫 저항 {_pct_text(w)}" if w is not None else ""))
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
    buy = snap["verdict"] in _BUY_STATES
    kind = "buy" if buy else ("nobuy" if snap["verdict"] == "매수불가" else "sell")
    price, stop = _num(snap.get("price")), _num(snap.get("stop"))

    sub = []
    if buy and _signal_label(snap):
        sub.append(f"신호 {_signal_label(snap)}")
        if snap.get("since") and not _truthy(snap.get("start_unknown", "")):
            sub.append(f"{_md(snap['since'])} 매수 전환")
    if snap.get("created"):
        sub.append(f"기준일 {snap['created']}")

    extra = ""
    if buy and price and stop is not None:
        target = price + (price - stop) * REWARD_RATIO
        wprice = _num(snap.get("wprice"))
        if (snap.get("weekly_pos") or "") == "신고가영역":
            resist = '<b>없음</b><em class="m-pos">신고가 영역</em>'
        elif wprice:
            resist = (f'<b>{_fmt_price(market, wprice)}</b>'
                      f'<em class="m-pos">{_pct_text((wprice / price - 1) * 100)}</em>')
        else:
            resist = "<b>—</b>"
        extra = (
            '<div class="m-lv3">'
            f'<div><span>손절</span><b>{_fmt_price(market, stop)}</b>'
            f'<em class="m-neg">{_pct_text((stop / price - 1) * 100)}</em></div>'
            f'<div><span>목표 ({REWARD_RATIO:g}R)</span><b>{_fmt_price(market, target)}</b>'
            f'<em class="m-pos">{_pct_text((target / price - 1) * 100)}</em></div>'
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
        f'<div class="m-sum__top"><span class="m-sum__px">{_fmt_price(market, price) if price else ""}</span>'
        f'<span class="verdict verdict-{kind}">{_display_verdict(snap["verdict"])}</span>{reason}</div>'
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
    tmp = OUT_WL.parent / f"{OUT_WL.name}_tmp"
    _reset_dir(tmp)
    entries = []
    superinv = _load_superinvestors()
    for md in sorted(SRC_WL.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        fm = _frontmatter(text)
        if fm.get("type") != "watchlist":
            continue
        ticker = fm.get("ticker", md.stem)
        out_name = f"{ticker}.md"   # ASCII-only: 한글 파일명 → 티커만
        name = _company_name(fm.get("title", ""))
        # 실계좌 필드·private 블록 제거 후 복사 — 원본(비공개)은 그대로 유지
        # 순서: 머리말 → 지금 상태 → 차트 → 13F → 지난 분석 메모(접힘) (2026-09-23)
        head, rest = _split_at_first_h2(_sanitize_public_md(text))
        snap = (latest_by_ticker or {}).get(ticker)
        page = (head + _status_section(snap, name)
                + "\n" + _CHART_BLOCK.format(ticker=ticker, attrs=_chart_attrs(snap))
                + _superinvestor_block(ticker, superinv)
                + _fold_old_memo(rest, str(fm.get("updated") or fm.get("created") or "")))
        (tmp / out_name).write_text(page, encoding="utf-8")
        entries.append((ticker, fm.get("market", ""), name, out_name))
    # 모든 파일 복사 완료 후 원자적 교체
    if OUT_WL.exists():
        shutil.rmtree(OUT_WL)
    tmp.rename(OUT_WL)
    return entries


def _collect_snapshots() -> list[dict]:
    """스냅샷 복사 + 메타 dict 리스트 반환.

    _reset_dir 대신 증분 복사 — 이미 있는 파일은 유지하고 새/변경 파일만 덮어씀.
    reset하면 auto-deploy 타이밍에 따라 일부 파일이 누락·삭제될 수 있음.
    """
    OUT_SNAP.mkdir(parents=True, exist_ok=True)
    snaps = []
    for md in sorted(SRC_SNAP.glob("*.md")):
        fm = _frontmatter(md.read_text(encoding="utf-8"))
        shutil.copy(md, OUT_SNAP / md.name)
        snaps.append({
            "ticker":  fm.get("ticker", md.stem),
            "created": fm.get("created", ""),
            "verdict": fm.get("verdict", ""),
            "reason":  fm.get("verdict-reason", ""),
            "stage":   fm.get("stage", ""),
            "tt":      fm.get("trend-template-score", ""),
            # 점수 분모. 2026-09-10 에 조건 4 를 빼면서 7 이 됐다.
            # 이 줄이 없는 과거 스냅샷은 8조건 시절이므로 8 로 읽는다 —
            # 기본값을 7 로 두면 옛 기록이 소급으로 틀린 분모를 갖는다.
            "ttmax":   fm.get("tt-max", 8),
            "price":   fm.get("price", ""),
            "market":  fm.get("market", ""),
            "days":    fm.get("candidate-days", ""),   # 매수 상태 경과 거래일 (구형 스냅샷은 "")
            "start_unknown": fm.get("candidate-start-unknown", ""),  # 등록 전부터 매수 상태
            "gap":     fm.get("sma50-gap-pct", ""),    # SMA50 이격 %
            # 홈 「오늘의 결론」 카드용 (2026-09-03) — 값이 없는 구형 스냅샷은 ""
            "stop":       fm.get("stop-price", ""),
            "weekly_pos": fm.get("weekly-position", ""),
            "weekly_pct": fm.get("weekly-overhead-pct", ""),
            "rr":         fm.get("real-rr", ""),
            # 관찰 페이지 결론 카드용 (2026-09-23)
            "since":      fm.get("candidate-since", ""),
            "wprice":     fm.get("weekly-overhead-price", ""),
            "fname":   md.name,
        })
    # 분석일 내림차순(동일 날짜는 종목 오름차순 — 안정 정렬)
    snaps.sort(key=lambda s: s["ticker"])
    snaps.sort(key=lambda s: s["created"], reverse=True)
    return snaps


def _collect_notes() -> list[dict]:
    """docs/notes/*.md 중 type=trade-note만 복사 + 메타 dict 리스트 반환.

    entry_date 내림차순. 템플릿(type 없음)은 건너뛴다. 알림 디렉터리와 같은
    이유로 reset 없이 증분 복사 — 청산 전 노트가 배포 타이밍에 유실되면 안 됨.
    """
    OUT_NOTES.mkdir(parents=True, exist_ok=True)
    notes = []
    for md in sorted(SRC_NOTES.glob("*.md")):
        fm = _frontmatter(md.read_text(encoding="utf-8"))
        if fm.get("type") != "trade-note":
            continue
        shutil.copy(md, OUT_NOTES / md.name)
        notes.append({
            "ticker":     fm.get("ticker", md.stem),
            "name":       fm.get("name", ""),
            "entry_date": fm.get("entry_date", ""),
            "status":     fm.get("status", "open"),
            "exit_date":  fm.get("exit_date", ""),
            "r_multiple": fm.get("r_multiple", ""),
            "outcome":    fm.get("outcome", ""),
            "fname":      md.name,
        })
    notes.sort(key=lambda n: n["entry_date"], reverse=True)
    return notes


def _monthly_stats(notes: list[dict]) -> list[dict]:
    """청산된 노트를 exit_date의 YYYY-MM으로 그룹핑해 승률·평균R·합계R 계산.

    합계 R은 단리 합산(동시 포지션 가능성 때문에 복리 계산은 부정확).
    월 내림차순 정렬.
    """
    by_month: dict[str, list[dict]] = {}
    for n in notes:
        if n.get("status") != "closed" or not n.get("exit_date"):
            continue
        month = n["exit_date"][:7]
        by_month.setdefault(month, []).append(n)

    stats = []
    for month, group in by_month.items():
        count = len(group)
        wins = sum(1 for n in group if n.get("outcome") == "win")
        r_values = [float(n["r_multiple"]) for n in group if n.get("r_multiple")]
        stats.append({
            "month":    month,
            "count":    count,
            "win_rate": (wins / count * 100) if count else 0.0,
            "avg_r":    (sum(r_values) / len(r_values)) if r_values else 0.0,
            "sum_r":    sum(r_values),
        })
    stats.sort(key=lambda s: s["month"], reverse=True)
    return stats


def _latest_per_ticker(snaps: list[dict]) -> list[dict]:
    """종목당 최신 스냅샷 1건만 반환.

    snaps은 날짜 내림차순 정렬 상태여야 한다 (_collect_snapshots 반환값).
    파일은 모두 복사되므로 히스토리 URL은 그대로 유지된다.
    """
    seen: set[str] = set()
    result = []
    for s in snaps:
        if s["ticker"] not in seen:
            seen.add(s["ticker"])
            result.append(s)
    return result


def _collect_positions() -> list[dict]:
    """현재 열린 매수 포지션을 core.positions로 복원해 dict 리스트로 반환.

    진입가 = 첫 매수전환 스냅샷가, 현재가 = 최신 스냅샷가(라이브 fetch 없음).
    core 미탑재(스냅샷 없음 등)면 빈 리스트. 렌더러는 plain dict만 받아 테스트 가능.
    """
    import sys
    if str(ROOT.parent) not in sys.path:
        sys.path.insert(0, str(ROOT.parent))
    try:
        from core.outcome import load_snapshot_series
        from core.positions import build_open_positions
        from core.scanner import _latest_snapshot_path
    except ImportError:
        return []

    snaps_by_ticker, market_by_ticker = load_snapshot_series(SRC_SNAP)
    positions = build_open_positions(snaps_by_ticker, market_by_ticker)
    return [{
        "ticker":        p.ticker,
        "market":        p.market,
        "verdict":       p.verdict,
        "entry_date":    p.entry_date.isoformat(),
        "current_date":  p.current_date.isoformat(),
        "snapshot_file": _latest_snapshot_path(p.ticker, SRC_SNAP).name,
        "entry_price":   p.entry_price,
        "stop_price":    p.stop_price,
        "current_price": p.current_price,
        "return_pct":    p.return_pct,
        "r_multiple":    p.r_multiple,
        "to_stop_pct":   p.to_stop_pct,
        "to_target_pct": p.to_target_pct,
        "days_held":     p.days_held,
        "days_held_basis": p.days_held_basis,
    } for p in positions]


def _fmt_price(market: str, value: float) -> str:
    """시장별 통화 표기 — KRX는 ₩ 정수, 그 외는 $ 소수 2자리."""
    if market.upper() in ("KRX", "KOSPI", "KOSDAQ"):
        return f"₩{value:,.0f}"
    return f"${value:,.2f}"


def _scan_alerts() -> list[dict]:
    """alerts/ 의 알림 페이지(uid.md) 메타를 최신순으로 반환. (삭제하지 않음)"""
    OUT_ALERT.mkdir(parents=True, exist_ok=True)
    alerts = []
    for md in OUT_ALERT.glob("*.md"):
        if md.name == "index.md":
            continue
        fm = _frontmatter(md.read_text(encoding="utf-8"))
        alerts.append({
            "created": fm.get("created", ""),
            "ticker":  fm.get("ticker", md.stem),
            "alert":   fm.get("alert", fm.get("title", "")),
            "fname":   md.name,
        })
    alerts.sort(key=lambda a: a["created"], reverse=True)
    return alerts


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
_STAGE_KO = {"1": "바닥 다지기", "2": "상승", "3": "천장 분배", "4": "하락"}
# 매수불가 사유를 한 문장으로 (core/verdict.py 의 REASON_* 와 짝)
_REASON_KO = {
    "과열": "50일선보다 25% 넘게 위에 있거나 RSI가 90을 넘었습니다. 지금은 추격 자리입니다.",
    "이격과대": "50일선보다 15% 넘게 위에 있습니다. 지금은 추격 자리입니다.",
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
_WEEKDAY_KO = "월화수목금토일"


def _num(v) -> "float | None":
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return None if f != f else f


def _is_expired(snap: dict) -> bool:
    d = _num(snap.get("days"))
    if d is None:
        return False
    return d > CANDIDATE_FRESH_MAX_DAYS or _truthy(snap.get("start_unknown", ""))


def _pick_priority(snap: dict) -> tuple:
    """카드 순서. 만료는 뒤로, 주봉 신고가영역 우선, 그다음 저항 손익비.

    ⚠ 2026-09-04 에 **등급(매수후보 우선) 항을 뺐다.** 8/8 이 더 낫다는 근거가
    없다 (충족 조건 8개 +0.148R < 7개 +0.189R < 6개 +0.208R, n=13,187).
    알림 슬롯 배분(monitor._entry_priority)도 등급을 쓰지 않는다. 두 순서를
    같게 유지할 것.
    """
    rr = _num(snap.get("rr")) or 0.0
    return (_is_expired(snap),
            _PICK_WEEKLY_RANK.get(snap.get("weekly_pos") or "", 2), -rr, snap["ticker"])


def _signal_label(snap: dict) -> str:
    """매수 상태 경과를 사람 말로. 「오늘」·「N일째」·「시작일 미상」."""
    if _truthy(snap.get("start_unknown", "")):
        return "시작일 미상"
    d = _num(snap.get("days"))
    if d is None:
        return ""
    return "오늘" if d == 0 else f"{int(d)}일째"


def _pct_text(v: float) -> str:
    return f"{v:+.1f}%"


def _first_resist(snap: dict) -> "tuple[str, str]":
    """(첫 저항까지 표기, 색 클래스). 신고가 영역이면 머리 위 저항이 없다."""
    if (snap.get("weekly_pos") or "") == "신고가영역":
        return "없음", "m-pos"
    w = _num(snap.get("weekly_pct"))
    if w is None:
        return "—", ""
    return _pct_text(w), ("m-wrn" if w < NEAR_RESIST_PCT else "m-pos")


def _stop_pct(snap: dict) -> "float | None":
    price, stop = _num(snap.get("price")), _num(snap.get("stop"))
    if not price or stop is None:
        return None
    return (stop - price) / price * 100


def _fresh_card(snap: dict, name: str) -> str:
    """홈 카드. 숫자 셋만. 누르면 그 종목의 관찰 페이지로 간다."""
    t = snap["ticker"]
    sp = _stop_pct(snap)
    rtxt, rcls = _first_resist(snap)
    w = _num(snap.get("weekly_pct"))
    warn = ('<div class="m-card__warn">머리 위 저항이 바로 앞</div>'
            if rcls == "m-wrn" and w is not None else "")
    name_html = f'<span class="m-card__name">{name}</span>' if name else ""
    return (
        f'<a class="m-card" href="watchlist/{t}/">'
        f'<div class="m-card__head"><b class="m-card__ticker">{t}</b>{name_html}'
        f'<span class="verdict verdict-buy">{_display_verdict(snap["verdict"])}</span></div>'
        f'<div class="m-card__nums">'
        f'<div><span>손절까지</span><b class="m-neg">{_pct_text(sp) if sp is not None else "—"}</b></div>'
        f'<div><span>첫 저항까지</span><b class="{rcls}">{rtxt}</b></div>'
        f'<div><span>신호</span><b>{_signal_label(snap) or "—"}</b></div>'
        f'</div>{warn}</a>'
    )


def _conclusion_section(snaps: list[dict], names: dict, positions: "list[dict] | None" = None,
                        max_cards: int = PICK_MAX_CARDS) -> str:
    """홈 첫 화면: 새 신호 수(큰 숫자) → 새 신호 카드 → 지난 신호 한 줄."""
    buys = sorted((s for s in snaps if s["verdict"] in _BUY_STATES), key=_pick_priority)
    fresh = [s for s in buys if not _is_expired(s)]
    stale = [s for s in buys if _is_expired(s)]
    out = [
        '<div class="m-hero">'
        '<div class="m-hero__k">오늘 새로 살 만한 종목</div>'
        f'<div class="m-hero__n">{len(fresh)}<small>종목</small></div>'
        f'<div class="m-hero__s">신호 {CANDIDATE_FRESH_MAX_DAYS}일 이내 · 매수 상태 {len(buys)}종목 중</div>'
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
        return json.loads(FEAR_INDEX_JSON.read_text(encoding="utf-8"))
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
    r = s.get("mean_r")
    rtxt = f"{r:+.2f}R" if r is not None else "—"
    rcls = "" if r is None else ("m-pos" if r >= 0 else "m-neg")
    return (
        '<div class="m-sec"><span>추천 기록</span><a href="strategies/">전체 ›</a></div>\n'
        '<a class="m-box m-strat" href="strategies/">'
        f'<div class="m-kv"><span>지금 켜진 방식</span><b>{_STRAT_LABEL.get(active, active)}</b>'
        f'<span class="m-muted">{_md(perf.get("active_since", ""))}부터</span></div>'
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
        f'<span class="m-li__d">{_md(a["created"])}</span><b>{a["ticker"]}</b>'
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
        _strategy_box(_collect_strategy_perf()),
        _recent_alerts(alerts),
        _superinvestor_home(_load_superinvestors(), names),
        "",
    ]
    lines += [
        "## 용어 설명",
        "",
        '??? info "📘 Stage (Weinstein 스테이지)란?"',
        "    주가 생명주기를 4단계로 분류하는 Stan Weinstein의 프레임워크. **30주 이동평균(≈150일 MA)** 방향과 가격 위치로 판단합니다.",
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
        "    | 1 | 현재가 > 150일 MA, 200일 MA |",
        "    | 2 | 150일 MA > 200일 MA |",
        "    | 3 | 200일 MA 최소 1개월째 상승 중 |",
        "    | 4 | 현재가 > 50일 MA |",
        "    | 5 | 현재가 ≥ 52주 저점 × 1.25 (+25% 이상) |",
        "    | 6 | 현재가 ≥ 52주 고점 × 0.75 (-25% 이내) |",
        "    | 7 | RS Rating(상대강도 등급) ≥ 70 |",
        "",
        "    **5/7 이상**: 매수 · **4/7 이하**: 기준미달. "
        "조건 개수는 등급이 아닙니다 — 11년 13,187건에서 만점(+0.148R)이 "
        "하한(+0.208R)보다 나았다는 근거가 없습니다. "
        "2026-09-10 에 `SMA50 > SMA150·SMA200` 조건을 뺐습니다 "
        "(성적 변화 없음, 예외 규칙 하나가 함께 사라짐).",
        "",
        '??? info "📘 진입 게이팅 — 점수가 만점이어도 매수불가가 되는 4가지"',
        "    Stage·TT 점수와 별개로, 아래 조건에 걸리면 매수에서 제외됩니다 (2026-06-11 도입).",
        "",
        "    | 게이트 | 조건 | 사유 표기 |",
        "    |--------|------|----------|",
        "    | 시장 국면 | 지수 MA 정렬이 하락/횡보 | 매수불가 (시장국면) |",
        "    | DD 누적 | 4주 내 Distribution Day(기관 매도일) 5회 이상 | 매수불가 (시장국면) |",
        "    | 지수 과열 | 지수가 50일 MA 대비 +15% 초과 (파라볼릭) | 매수불가 (시장국면) |",
        "    | 종목 과열 | 50일 MA +25% 이격 또는 RSI > 90 | 매수불가 (과열) |",
        "    | 변동성 | 2N ATR 손절폭이 진입가의 8% 초과 | 매수불가 (변동성과대) |",
        "",
        "    매수 후 **+1.5R** 도달 시 손절선을 본전으로 올리라는 🔒 본전 스톱 알림이 발송됩니다.",
        "",
    ]
    return "\n".join(lines) + "\n"


def _wl_sub(s: dict) -> str:
    """목록 줄 오른쪽 아래 작은 글씨: 매수는 경과, 매수불가는 사유."""
    if s["verdict"] in _BUY_STATES:
        lab = _signal_label(s)
        if lab and _is_expired(s) and lab != "시작일 미상":
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
        fresh = "1" if (f == "buy" and not _is_expired(s)) else "0"
        rank = [g for g, _ in _WL_GROUPS].index(f)
        days = _num(s.get("days")) if s else None
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
                f'<span>{CANDIDATE_FRESH_MAX_DAYS}일 이내</span></div>' if fresh == "1" else
                f'<div class="wl-grp" data-fresh="0">지난 신호 <b>{n_stale}</b>'
                f'<span>추격 비추천</span></div>')
        if s:
            kind = {"buy": "buy", "nobuy": "nobuy"}.get(f, "sell")
            badge = f'<span class="verdict verdict-{kind}">{_display_verdict(s["verdict"])}</span>'
            price = _fmt_price_str(s.get("price", ""), market)
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
        f"매수 추천은 **{CANDIDATE_FRESH_MAX_DAYS}일째까지만 유효**합니다. "
        "넘기면 「만료」로 표시하고 푸시 알림도 보내지 않습니다(백테스트상 늦은 진입은 "
        "기대값이 줄어듭니다. 매수 상태를 벗어났다 다시 들어오면 새 추천이 됩니다). "
        "관찰 등록 때 이미 매수 상태였던 종목은 전환일을 알 수 없어 「시작일 미상」으로 "
        "표시하고 새 추천으로 보지 않습니다.",
        "",
    ]) + "\n"


def _snapshots_index(snaps, names) -> str:
    lines = [
        "# 분석 스냅샷",
        "",
        "특정 시점의 **판정 기록**(최신순). 판정 어휘 — "
        "**매수**(Stage 2 + TT 5/7 이상) · "
        "**매수불가**(사유: 과열·시장국면·변동성과대·하락국면·천장권·기준미달).",
        "",
        SNAP_FILTERS,
        # 관찰 종목과 같은 원칙 — 판정을 앞으로, 분석일은 뒤로 (2026-07-19)
        "| 종목 | 기업명 | 판정 | Stage | TT | 분석일 |",
        "|------|--------|------|-------|----|--------|",
    ]
    for s in snaps:
        name = names.get(s['ticker'], '')
        lines.append(
            f"| [{s['ticker']}]({s['fname']}) | [{name}]({s['fname']}) "
            f"| {_verdict_cell(s['verdict'], s['reason'])} "
            f"| {s['stage']} | {s['tt']}/{s.get('ttmax', 8)} | {s['created']} |"
        )
    return "\n".join(lines) + "\n"


def _alerts_index(alerts, names) -> str:
    lines = [
        "# 알림",
        "",
        "관찰 종목이 임계선을 넘은 **순간**에 자동 기록되는 이벤트(최신순). "
        "유형 — 📈 매수신호 · 👀 매수근접 · 📉 매도신호 · 🚨 손절경고.",
        "",
    ]
    if not alerts:
        lines += [
            '!!! info "아직 발생한 알림이 없습니다"',
            "    관찰 종목이 매수·매도·손절 조건을 충족하면 이곳에 자동으로 기록됩니다.",
        ]
        return "\n".join(lines) + "\n"
    lines += ["| 발생일 | 종목 | 기업명 | 유형 |", "|--------|------|--------|------|"]
    for a in alerts:
        lines.append(f"| {a['created']} | [{a['ticker']}]({a['fname']}) | [{names.get(a['ticker'], '')}]({a['fname']}) | {a['alert']} |")
    return "\n".join(lines) + "\n"


_SEED_PANEL = """\
<div class="seed-panel">
<label>시드 (원): <input type="number" id="seed-input" min="0" step="100000" placeholder="예: 10000000"></label>
&nbsp;&nbsp;<label>트레이드당 리스크: <input type="number" id="risk-input" min="0.1" step="0.1" value="1" style="width:4.5em"> %</label>
<p class="seed-hint">💡 시드를 입력하면 종목별 <b>주수·손익(원)</b>과 아래 <b>포트폴리오 요약</b>이 계산됩니다. 시드는 이 브라우저에만 저장되며 서버·공개 저장소에 올라가지 않습니다.</p>
<div id="seed-summary"></div>
</div>
"""


def _positions_index(positions: list[dict], names: dict) -> str:
    """열린 매수 포지션의 진입가 대비 현재 수익률·R 표(진입 R-배수 내림차순)."""
    lines = [
        "# 가상 포지션",
        "",
        '!!! info "알림 기준 성적은 방식별 기록에 있습니다"',
        "    이 페이지는 과거 **판정 기록**에서 매수 전환을 다시 만든 가상 포지션입니다. 알림이 나가지 않은 전환도 "
        "들어가서 건수가 [방식별 기록](../strategies/index.md)보다 많습니다. 실제로 알림이 나간 추천의 "
        "추천가·목표가·손절가와 「추천대로 했다면」 금액은 방식별 기록에서 보세요.",
        "",
        "현재 **매수** 판정인 종목의 진입가 대비 현재 수익률·R-배수. "
        "진입가 = 비매수→매수로 전환된 **첫 스냅샷 가격**, 현재가 = **최신 스냅샷 가격**입니다.",
        "",
        '!!! warning "가정된 진입 (실제 체결 아님)"',
        "    진입가는 판정이 매수로 바뀐 시점의 분석용 스냅샷 가격이며, 실제 매매 체결가가 "
        "아닙니다. R-배수·수익률은 그 가정 진입가 기준의 참고 수치입니다.",
        "",
        '??? info "📘 R이 뭔가요? (수익률 %와 뭐가 다른가요)"',
        "    **R = 이 매매에서 각오한 손실폭(진입가→손절가)을 1로 봤을 때, 지금 얼마나 벌었나**를 나타내는 숫자입니다.",
        "",
        "    - **1R** = 진입가 − 손절가 (각오한 최대 손실폭)",
        "    - **R배수** = 지금 이익 ÷ 1R",
        "",
        "    예시 — $100에 사서 손절을 $90에 뒀다면 1R = $10.",
        "    현재가 $110이면 이익 $10 → **+1.0R** (각오한 손실만큼 벌었다는 뜻). "
        "현재가가 $90까지 내려가 손절되면 **−1.0R**.",
        "",
        "    **왜 수익률 %만으로는 부족한가?** 종목마다 손절폭이 다르기 때문입니다. "
        "+6% 올라도 손절이 −25% 멀리 있으면 +0.2R에 불과하고, +4%라도 손절이 −9%로 가까우면 +0.8R입니다. "
        "**R은 '감수한 위험 대비' 성과라, 종목이 달라도 같은 잣대로 비교**할 수 있습니다.",
        "",
        "    | R 값 | 의미 |",
        "    |------|------|",
        f"    | **+{REWARD_RATIO:g}R** | 목표 도달 ({REWARD_RATIO:g}:1 리워드) |",
        "    | **+1.5R** | 손절선을 본전으로 올릴 때 |",
        "    | **+1R** | 각오한 위험만큼 벌었다 |",
        "    | **0R** | 본전 |",
        "    | **−1R** | 손절 도달 (청산) |",
        "",
    ]
    if not positions:
        lines += [
            '!!! info "열린 포지션 없음"',
            "    현재 매수 판정인 종목이 없습니다. "
            "`python monitor.py --scan` 으로 스냅샷을 갱신하세요.",
        ]
        return "\n".join(lines) + "\n"

    rows = sorted(positions, key=lambda p: p["r_multiple"], reverse=True)
    lines += [
        _SEED_PANEL,
        "",
        "| 종목 | 판정 | 진입일 | 진입가 | 현재가 | 수익률 | R | 손절까지 | 타겟까지 | 보유 | 주수 | 손익(원) |",
        "|------|------|--------|--------|--------|--------|---|---------|---------|------|------|---------|",
    ]
    for p in rows:
        t = p["ticker"]
        name = names.get(t, "")
        snapshot_file = p.get("snapshot_file") or f"{t}-{p['current_date']}.md"
        link = f"../snapshots/{snapshot_file}"
        dot = "🟢" if p["r_multiple"] > 0 else ("🔴" if p["r_multiple"] < 0 else "⚪")
        duration = f"{p['days_held']}일"
        if p.get("days_held_basis") == "observation":
            duration = f"관측 {duration}"
        lines.append(
            f"| [**{t}**]({link}) {name} | {_verdict_cell(p['verdict'], '')} "
            f"| {p['entry_date'][5:]} "
            f"| {_fmt_price(p['market'], p['entry_price'])} "
            f"| {_fmt_price(p['market'], p['current_price'])} "
            f"| {dot} {p['return_pct']:+.1f}% "
            f"| {p['r_multiple']:+.1f}R "
            f"| {p['to_stop_pct']:+.1f}% "
            f"| {p['to_target_pct']:+.1f}% "
            f"| {duration} "
            f'| <span class="js-shares" data-ticker="{t}">—</span> '
            f'| <span class="js-pnl" data-ticker="{t}">—</span> |'
        )

    n = len(rows)
    avg_r = sum(p["r_multiple"] for p in rows) / n
    wins = sum(1 for p in rows if p["r_multiple"] > 0)
    pos_data = [{"ticker": p["ticker"], "entry": p["entry_price"],
                 "stop": p["stop_price"], "current": p["current_price"],
                 "r": p["r_multiple"]} for p in rows]
    lines += [
        "",
        f"**합계** {n}포지션 · 평균 {avg_r:+.1f}R · 양의 R {wins}/{n}",
        "",
        '<script type="application/json" id="pos-data">',
        json.dumps(pos_data, ensure_ascii=False),
        "</script>",
        "",
        DISCLAIMER,
    ]
    return "\n".join(lines) + "\n"


_STRAT_LABEL = {"base": "스윙", "book": "단타"}


def _collect_strategy_perf() -> dict:
    """data/strategy_perf.json 로드. 없거나 깨졌으면 {} (페이지는 안내문으로 그린다)."""
    try:
        return json.loads(STRATEGY_PERF_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _md(ts: str) -> str:
    """'2026-09-18T17:49:00' → '09-18'."""
    return str(ts)[5:10]


def _strat_cell(s: dict) -> tuple[str, str]:
    done = str(s.get("closed", 0))
    if s.get("open"):
        done += f" · 진행 {s['open']}"
    r = s.get("mean_r")
    return done, (f"{r:+.2f}R" if r is not None else "—")


def _strategies_index(data: dict, names: dict) -> str:
    """스윙·단타 두 방식의 켜져 있던 기간별 성적과 최근 거래. 모바일 4열 이하."""
    lines = [
        "# 방식별 기록",
        "",
        "스윙(일봉)과 단타(1시간봉) 두 방식을 섞지 않고 따로 기록합니다. **켜진 방식만 알림이 나가고**, "
        "꺼진 방식은 같은 기간에 무엇을 했을지 기록만 합니다. 텔레그램에 「단타」·「스윙」을 보내 바꿉니다.",
        "",
    ]
    periods = data.get("periods") or []
    if not periods:
        lines += ['!!! info "아직 기록이 없습니다"',
                  "    다음 스캔 때 채워집니다.", "", DISCLAIMER]
        return "\n".join(lines) + "\n"
    active = _STRAT_LABEL.get(data.get("active"), "스윙")
    since = str(data.get("active_since") or "")[5:16].replace("T", " ")
    lines += [f"**지금 켜진 방식: {active}** ({since}부터)", "", "## 기간별 성적", "",
              "| 기간 | 구분 | 끝남 | 거래당 |", "|---|---|---:|---:|"]
    for i, p in enumerate(periods):
        on = _STRAT_LABEL[p["strategy"]]
        off = _STRAT_LABEL["book" if p["strategy"] == "base" else "base"]
        end = "지금" if i == len(periods) - 1 else _md(p["end"])
        done, r = _strat_cell(p["active"])
        lines.append(f"| {_md(p['start'])}~{end} | {on}(알림) | {done} | {r} |")
        done, r = _strat_cell(p["other"])
        lines.append(f"| | {off}(기록만) | {done} | {r} |")
    total = sum(p["active"].get("closed", 0) for p in periods)
    min_n = data.get("min_n", 100)
    lines += ["", f'!!! warning "표본 부족: 알림 나간 끝난 거래 {total}건"',
              f"    {min_n}건이 쌓이기 전에는 두 방식의 우열을 가릴 수 없습니다. 숫자는 기록으로만 읽으세요.",
              ""] if total < min_n else [""]
    money = data.get("money") or {}
    if money:
        seed = int(data.get("seed_won", 1_000_000)) // 10000
        r_won = float(data.get("r_won", 10000))
        lines += ["## 추천대로 했다면", "",
                  f"사지 않았어도 **알림이 나간 추천을 그대로 따랐을 때**의 결과입니다. "
                  f"시드 {seed}만 원에서 추천마다 {r_won:,.0f}원(시드 1%)을 손절 위험으로 건 경우로 환산합니다. "
                  "진행 중인 추천은 지금 가격으로 평가합니다.", "",
                  "| 방식 | 끝난 추천 | 진행 중 | 합계 |", "|---|---:|---:|---:|"]
        for key in ("base", "book"):
            m = money.get(key)
            if not m:
                continue
            won = lambda r: f"{r * r_won:+,.0f}원"  # noqa: E731
            lines.append(f"| {_STRAT_LABEL[key]} | {m['closed']}건 {won(m['closed_r'])} | "
                         f"{m['open']}건 {won(m['open_r'])} | **{m['total_won']:+,.0f}원** |")
        lines.append("")
    trades = data.get("trades") or []
    if trades:
        lines += ["## 최근 추천", "", "| 추천 | 종목 · 추천가 | 방식 | 결과 |", "|---|---|---|---|"]
        for t in trades:
            how = _STRAT_LABEL.get(t["strategy"], "") + ("" if t.get("pushed") else " · 기록만")
            res = t.get("result", "")
            if t.get("r") is not None:
                res += f" {t['r']:+.2f}R"
                if t.get("pct") is not None:
                    res += f" ({t['pct'] * 100:+.1f}%)"
            name = t["ticker"]
            if t.get("entry") is not None and t.get("stop") is not None:
                tg = " / ".join(f"{v:,.2f}" for v in (t.get("targets") or [])) or "-"
                name += f"<br>{t['entry']:,.2f} · 목표 {tg} · 손절 {t['stop']:,.2f}"
            lines.append(f"| {_md(t['ts'])} | {name} | {how} | {res} |")
        lines.append("")
    lines += ["R 은 손절 폭 대비 몇 배를 벌었는지입니다 (−1R = 손절). 거래비용은 빼지 않았습니다. "
              "진행 중 추천의 R 은 지금 가격 기준이라 확정 값이 아닙니다. "
              "알림 기록은 2026-09-04 부터라 그 전에 연 거래는 없습니다.", "",
              f"> 기준 시각: {str(data.get('generated', ''))[:16].replace('T', ' ')}", "", DISCLAIMER]
    return "\n".join(lines) + "\n"


_REGIME_KO = {
    "STRONG_UPTREND":   "강한 상승",
    "UPTREND":          "상승",
    "RANGING":          "횡보",
    "DOWNTREND":        "하락",
    "STRONG_DOWNTREND": "강한 하락",
    "UNKNOWN":          "N/A",
}

_REGIME_ENTRY = {
    "STRONG_UPTREND":   "✅ 신규 진입 허용",
    "UPTREND":          "✅ 신규 진입 허용",
    "RANGING":          "⚠️ 신규 진입 자제",
    "DOWNTREND":        "🚫 신규 진입 금지",
    "STRONG_DOWNTREND": "🚫 신규 진입 금지",
    "UNKNOWN":          "—",
}


_TV_HEATMAP = """\
## 섹터 히트맵 (S&P 500)

<div class="tradingview-widget-container" style="height:520px;margin-bottom:1rem;">
<div class="tradingview-widget-container__widget" style="height:100%;width:100%"></div>
<script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>
{
  "exchanges": [],
  "dataSource": "SPX500",
  "grouping": "sector",
  "blockSize": "market_cap_basic",
  "blockColor": "change",
  "locale": "ko",
  "colorTheme": "dark",
  "hasTopBar": true,
  "isDataSetEnabled": true,
  "isZoomEnabled": true,
  "hasSymbolTooltip": true,
  "isMonoSize": false,
  "width": "100%",
  "height": 500
}
</script>
</div>

> 출처: TradingView · 실시간 데이터 (페이지 로드 시점 기준)
"""


_SIGNAL_EMOJI = {"매집": "🟢", "분산": "🔴", "중립": "⚪"}


def _rank_table(title: str, ranking: list, entity_label: str,
                show_vol_share: bool) -> list[str]:
    """섹터/테마 신호 리스트 → 순위 표 마크다운 줄. 비어 있으면 안내문.

    ranking:        [{name, rs, accum, dist, signal, vol_share?}, ...] dict 리스트
    entity_label:   표 헤더의 대상 컬럼명 ("섹터" | "테마")
    show_vol_share: True면 '거래대금 비중' 컬럼 추가 (섹터 전용, 테마는 제외)
    """
    if not ranking:
        return [f"### {title}", "", "_데이터 없음_", ""]

    has_ticker = any(e.get("ticker") for e in ranking)

    header = f"| 순위 | {entity_label} |"
    divider = "|---|---|"
    if has_ticker:
        header += " ETF/바스켓 |"
        divider += "---|"
    header += " RS | 신호 | 매집일 | 분산일 |"
    divider += "---|---|---|---|"
    if show_vol_share:
        header += " 거래대금 비중 |"
        divider += "---|"

    rows = [f"### {title}", "", header, divider]
    for i, entry in enumerate(ranking, start=1):
        name  = entry.get("name", "?")
        rs    = entry.get("rs", 0)
        sig   = entry.get("signal", "중립")
        accum = entry.get("accum", 0)
        dist  = entry.get("dist", 0)
        emoji = _SIGNAL_EMOJI.get(sig, "⚪")
        row   = f"| {i} | {name} |"
        if has_ticker:
            row += f" {entry.get('ticker') or '-'} |"
        row += f" {rs:+.2f} | {emoji} {sig} | {accum} | {dist} |"
        if show_vol_share:
            row += f" {entry.get('vol_share', 0.0):.1f}% |"
        rows.append(row)
    rows.append("")
    return rows


def _sector_flow_section(data: "dict | None", show_kr: bool = True) -> list[str]:
    """섹터 자금 흐름(RS 순위) 대시보드 섹션 마크다운 줄 생성.

    data: sector_strength.json 파싱 결과 또는 None.
    """
    lines = [
        "## 섹터 자금 흐름",
        "",
    ]
    if not data or (not data.get("us") and not data.get("kr")):
        lines += [
            '!!! info "섹터 데이터 없음"',
            "    `python monitor.py --scan` 을 실행하면 섹터별 상대강도·수급 신호가 채워집니다.",
            "",
        ]
        return lines

    updated = data.get("updated_at", "")
    lines += [
        f"> **RS**: 상대강도 순위 · **신호**: 최근 20일 매집/분산(가격방향×거래량) · "
        f"**거래대금 비중**: 섹터 쏠림 게이지. 수집: {updated} · `--scan` 시 갱신",
        *([">", "> 한·미는 통화·데이터 소스가 달라 **별도 순위**입니다. 두 시장 점수를 직접 비교하지 마세요."]
          if show_kr else []),
        "",
        *_rank_table("미국 (S&P 500 섹터 ETF)", data.get("us") or [], "섹터", show_vol_share=True),
        # 한국은 관찰 종목이 있을 때만 (2026-09-22: 09-05 한국 관찰 제외 뒤 쓰지 않는 칸)
        *(_rank_table("한국 (KODEX/TIGER 섹터 ETF)", data.get("kr") or [], "섹터", show_vol_share=True)
          if show_kr else []),
    ]
    return lines


def _theme_flow_section(data: "dict | None", show_kr: bool = True) -> list[str]:
    """테마 바스켓 자금 흐름 섹션 마크다운 줄 생성."""
    lines = ["## 테마별 자금 흐름 (로테이션)", ""]
    if not data or (not data.get("theme_us") and not data.get("theme_kr")):
        lines += [
            '!!! info "테마 데이터 없음"',
            "    `python monitor.py --scan` 을 실행하면 GPU·전력·기판 등 테마 신호가 채워집니다.",
            "",
        ]
        return lines

    updated = data.get("updated_at", "")
    lines += [
        f"> GPU→전력→반도체→피지컬AI→기판 로테이션 추적. "
        f"RS+신호로 현재 자금이 어느 테마에 집중되는지 판독. 수집: {updated}",
        ">",
        "> **US**: SMH(GPU/반도체)·IRBO(AI인프라)·BOTZ(피지컬AI) ETF + 전력/DataCenter 바스켓",
        *(["> **KR**: 전력(4종)·기판(5종)·피지컬AI(3종) 균등가중 바스켓"] if show_kr else []),
        "",
        *_rank_table("미국 테마", data.get("theme_us") or [], "테마", show_vol_share=False),
        *(_rank_table("한국 테마", data.get("theme_kr") or [], "테마", show_vol_share=False)
          if show_kr else []),
    ]
    return lines


def _trade_report_section(data: "dict | None") -> list[str]:
    """수출입 동향 보도자료 → 대시보드 섹션 마크다운."""
    # 데이터가 없으면 칸 자체를 싣지 않는다 (2026-09-22 사용자 결정: 빈 칸 정리).
    # 보도자료를 넣으려면 `python monitor.py --trade-report <파일경로>`.
    if not data:
        return []
    lines = ["## 수출입 동향 (산업통상자원부)", ""]

    period   = data.get("period", "?")
    updated  = data.get("updated_at", "")
    exp      = data.get("exports_total", {})
    imp      = data.get("imports_total", {})
    bal      = data.get("trade_balance", 0)
    products = data.get("by_product", [])
    highs    = data.get("highlights", [])

    def _sign(v): return "+" if v > 0 else ""

    exp_yoy = exp.get("yoy", 0)
    imp_yoy = imp.get("yoy", 0)

    lines += [
        f"> **{period}** · 수집: {updated} · 출처: 산업통상자원부",
        "",
        "### 총괄",
        "",
        "| 항목 | 금액 | 전년동월비 |",
        "|------|------|-----------|",
        f"| 수출 | **{exp.get('value','?')}억달러** | {_sign(exp_yoy)}{exp_yoy:.1f}% |",
        f"| 수입 | {imp.get('value','?')}억달러 | {_sign(imp_yoy)}{imp_yoy:.1f}% |",
        f"| 무역수지 | {_sign(bal)}{bal:.0f}억달러 | — |",
        "",
    ]

    if products:
        lines += [
            "### 품목별 수출",
            "",
            "| 품목 | 전년동월비 | 비고 |",
            "|------|-----------|------|",
        ]
        for p in products:
            yoy = p.get("yoy", 0)
            emoji = "🟢" if yoy > 5 else ("🔴" if yoy < -5 else "⚪")
            note = p.get("note", "")
            lines.append(
                f"| {p.get('name','?')} | {emoji} {_sign(yoy)}{yoy:.1f}% | {note} |"
            )
        lines.append("")

    if highs:
        lines += ["### 핵심 분석", ""]
        for h in highs:
            lines.append(f"- {h}")
        lines.append("")

    return lines


def _load_trade_report() -> "dict | None":
    """data/trade_report.json 로드. 없거나 오류면 None."""
    if not TRADE_REPORT_JSON.exists():
        return None
    try:
        return json.loads(TRADE_REPORT_JSON.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def _load_sector_flow() -> "dict | None":
    """data/sector_strength.json 로드. 없거나 오류면 None."""
    if not SECTOR_JSON.exists():
        return None
    try:
        return json.loads(SECTOR_JSON.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def _fear_index_page(latest=None, names=None, show_kr: bool = True) -> str:
    """data/fear_index.json → fear-index.md 마크다운."""
    sector = _load_sector_flow()
    trade  = _load_trade_report()
    latest = latest or []
    names  = names or {}

    def _recent_analysis_section() -> list[str]:
        if not latest:
            return []
        rows = [
            "## 최근 분석",
            "",
            "| 종목 | 기업명 | 분석일 | 판정 | Stage | TT |",
            "|------|--------|--------|------|-------|----|",
        ]
        top5 = sorted(latest[:5], key=lambda s: _VERDICT_ORDER.get(s['verdict'], 9))
        for s in top5:
            name = names.get(s['ticker'], '')
            rows.append(
                f"| [**{s['ticker']}**](snapshots/{s['fname']}) | [{name}](snapshots/{s['fname']}) | {s['created']} | {_verdict_cell(s['verdict'], s['reason'])} "
                f"| {s['stage']} | {s['tt']}/{s.get('ttmax', 8)} |"
            )
        rows += ["", "[→ 전체 스냅샷](snapshots/index.md)", ""]
        return rows

    if not FEAR_INDEX_JSON.exists():
        return (
            "# 시장 현황\n\n"
            + "\n".join(_recent_analysis_section()) + "\n"
            + _TV_HEATMAP
            + "\n"
            + "\n".join(_sector_flow_section(sector, show_kr))
            + "\n"
            + "\n".join(_theme_flow_section(sector, show_kr))
            + "\n"
            + "\n".join(_trade_report_section(trade))
            + "\n"
            '!!! info "공포 지수 데이터 없음"\n'
            "    `python monitor.py --scan` 을 실행하면 아래 공포 지수가 채워집니다.\n"
        )

    data = json.loads(FEAR_INDEX_JSON.read_text(encoding="utf-8"))
    updated = data.get("updated_at", "")
    vix    = data.get("vix")
    vkospi = data.get("vkospi")
    us_r   = data.get("us_regime", "UNKNOWN")
    kr_r   = data.get("kr_regime", "UNKNOWN")
    cnn_fg = data.get("cnn_fear_greed")

    def _row(label: str, entry, regime: str) -> str:
        if entry is None:
            return (
                f"| {label} | — | — | — "
                f"| {_REGIME_KO.get(regime, regime)} "
                f"| {_REGIME_ENTRY.get(regime, '—')} |"
            )
        change = entry.get("change", 0.0)
        sign = "+" if change > 0 else ""
        return (
            f"| {label} | {entry.get('value', 'N/A')} "
            f"| {sign}{change} "
            f"| {entry.get('grade_emoji', '')} {entry.get('grade', 'N/A')} "
            f"| {_REGIME_KO.get(regime, regime)} "
            f"| {_REGIME_ENTRY.get(regime, '—')} |"
        )

    def _cnn_section(fg: dict) -> list[str]:
        if not fg:
            return []
        score   = fg.get("score", 0)
        prev    = fg.get("prev_score", score)
        change  = fg.get("change", 0.0)
        sign    = "+" if change > 0 else ""
        emoji   = fg.get("rating_emoji", "⚪")
        rating  = fg.get("rating_ko", "—")

        rows = [
            "## CNN Fear & Greed Index",
            "",
            f"> 수집: {updated} · 출처: [CNN Markets](https://edition.cnn.com/markets/fear-and-greed)",
            "",
            f"| 점수 | 전일比 | 등급 |",
            f"|------|--------|------|",
            f"| **{score}** / 100 | {sign}{change} | {emoji} **{rating}** |",
            "",
            "### 구성 지표 (7개)",
            "",
            "| 지표 | 점수 | 등급 |",
            "|------|------|------|",
        ]
        for comp in fg.get("components", []):
            s = comp.get("score")
            s_str = f"{s:.1f}" if s is not None else "—"
            rows.append(
                f"| {comp['label']} | {s_str} "
                f"| {comp['rating_emoji']} {comp['rating_ko']} |"
            )
        rows.append("")
        return rows

    lines = [
        "# 시장 현황",
        "",
        *_recent_analysis_section(),
        _TV_HEATMAP,
        "",
        *_sector_flow_section(sector, show_kr),
        *_theme_flow_section(sector, show_kr),
        *_trade_report_section(trade),
        DISCLAIMER,
        "",
        *_cnn_section(cnn_fg),
        "## VIX",
        "",
        f"> 수집: {updated} · `python monitor.py --scan` 실행 시 갱신",
        "",
        "| 지수 | 현재값 | 전일比 | 등급 | 시장 국면 | 신규 진입 |",
        "|------|--------|--------|------|---------|---------|",
        _row("VIX (미국 S&P500)", vix, us_r),
        *([_row("KOSPI (한국 코스피)", vkospi, kr_r)] if vkospi is not None else []),
        "",
        '??? info "📘 VIX 등급 기준"',
        "    | 등급 | VIX | 의미 |",
        "    |------|-----|------|",
        "    | 🔴 극공포 | > 40 | 패닉 매도 구간, 저점 매수 기회일 수 있음 |",
        "    | 🟠 공포   | 30–40 | 시장 불안 고조, 변동성 확대 |",
        "    | 🟡 주의   | 20–30 | 불확실성 존재, 선별적 접근 |",
        "    | ⚪ 중립   | 15–20 | 안정적 흐름, 정상 변동성 |",
        "    | 🟢 탐욕   | < 15  | 과열 주의, 변동성 낮음 |",
        "",
        '??? info "📘 시장 국면 해석"',
        "    S&P500 / KOSPI의 50·150·200일 MA 정렬 기반으로 판정합니다.",
        "",
        "    | 국면 | 한국어 | 신규 진입 |",
        "    |------|--------|---------|",
        "    | STRONG_UPTREND | 강한 상승 | ✅ 허용 |",
        "    | UPTREND | 상승 | ✅ 허용 |",
        "    | RANGING | 횡보 | ⚠️ 자제 |",
        "    | DOWNTREND | 하락 | 🚫 금지 |",
        "    | STRONG_DOWNTREND | 강한 하락 | 🚫 금지 |",
    ]
    return "\n".join(lines) + "\n"


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    snaps   = _collect_snapshots()          # 전체 히스토리 (파일 복사 완료)
    latest  = _latest_per_ticker(snaps)     # 인덱스·대시보드용: 종목당 최신 1건
    # 관찰 페이지 맨 위 「지금 상태」 카드가 최신 스냅샷을 쓴다 (2026-09-23)
    entries = _collect_watchlist({s["ticker"]: s for s in latest})
    alerts  = _scan_alerts()
    positions = _collect_positions()        # 현재 열린 매수 포지션
    names   = {ticker: name for ticker, _market, name, _fname in entries}
    # 워치리스트에서 뺀 종목의 옛 스냅샷은 목록·대시보드에서 제외한다 (2026-08-23).
    # 파일은 그대로 복사되므로 히스토리 URL과 백테스트 원자료는 보존된다.
    # 계기: 6월에 정리한 7종목(BMNR·CEG 등)이 최신 목록 사이에 6월 날짜로 남아
    # "스냅샷 갱신이 멈췄다"는 오해를 불렀다.
    retired = [s["ticker"] for s in latest if s["ticker"] not in names]
    latest  = [s for s in latest if s["ticker"] in names]

    OUT_POS.mkdir(parents=True, exist_ok=True)
    (OUT / "index.md").write_text(_dashboard(entries, latest, alerts, names, positions), encoding="utf-8")
    kr_watched = any(m in ("KRX", "KOSDAQ") for _t, m, _n, _f in entries)
    (OUT / "fear-index.md").write_text(_fear_index_page(latest, names, show_kr=kr_watched),
                                       encoding="utf-8")
    latest_map = {s["ticker"]: s for s in latest}
    (OUT_WL / "index.md").write_text(_watchlist_index(entries, latest_map), encoding="utf-8")
    # _collect_watchlist가 OUT_WL을 통째로 교체하므로 반드시 그 뒤에 쓴다
    charted = _write_chart_data(entries)
    (OUT_SNAP / "index.md").write_text(_snapshots_index(latest, names), encoding="utf-8")
    (OUT_ALERT / "index.md").write_text(_alerts_index(alerts, names), encoding="utf-8")
    (OUT_POS / "index.md").write_text(_positions_index(positions, names), encoding="utf-8")
    OUT_STRAT.mkdir(parents=True, exist_ok=True)
    (OUT_STRAT / "index.md").write_text(
        _strategies_index(_collect_strategy_perf(), names), encoding="utf-8")

    print(f"생성 완료: 관찰 {len(entries)}개 · 스냅샷 {len(latest)}종목({len(snaps)}건, "
          f"목록 제외 {len(retired)}종목) "
          f"· 알림 {len(alerts)}건 · 가상 포지션 {len(positions)}개 "
          f" · 차트 {charted}/{len(entries)}종목")


if __name__ == "__main__":
    main()
