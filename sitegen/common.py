"""공용 도구와 상수: frontmatter 읽기, 판정 표시, 숫자·가격 표기, 신선도(D+N) 판정.

2026-10-02 gen.py 에서 나눴다. 다른 sitegen 모듈은 함수를 이름째 가져오지 않고
「모듈.이름」으로 부른다(테스트가 한 곳만 바꿔 끼워도 모든 호출에 먹게).
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path


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


def _fmt_price(market: str, value: float) -> str:
    """시장별 통화 표기 — KRX는 ₩ 정수, 그 외는 $ 소수 2자리."""
    if market.upper() in ("KRX", "KOSPI", "KOSDAQ"):
        return f"₩{value:,.0f}"
    return f"${value:,.2f}"


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


_STRAT_LABEL = {"base": "스윙", "book": "단타", "both": "스윙·단타"}


def _md(ts: str) -> str:
    """'2026-09-18T17:49:00' → '09-18'."""
    return str(ts)[5:10]
