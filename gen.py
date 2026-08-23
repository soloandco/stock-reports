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
OUT_PERF  = OUT / "performance"
FEAR_INDEX_JSON = ROOT.parent / "data" / "fear_index.json"
SECTOR_JSON = ROOT.parent / "data" / "sector_strength.json"
TRADE_REPORT_JSON = ROOT.parent / "data" / "trade_report.json"
COMPLETED_TRADES_JSON = ROOT.parent / "data" / "completed_trades.json"

# 매수후보 추천 유효기간(거래일). 이 값을 넘긴 후보는 '만료'로 표시된다.
# core.notifier.CANDIDATE_FRESH_MAX_DAYS와 같아야 한다 — 이 스크립트는 공개 저장소에
# 있어 core를 런타임 의존하지 않으므로 값을 복제하고, 일치 여부는 테스트로 강제한다
# (test_gen.py::test_expiry_threshold_matches_core, 2026-08-11).
CANDIDATE_FRESH_MAX_DAYS = 5

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
<option value="cand">매수후보</option>
<option value="watch">매수관찰</option>
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

WL_FILTERS = """\
<div class="snap-filters">
<label class="sf-label" for="sf-market">시장</label>
<select class="sf-select" id="sf-market" data-f="market">
<option value="">전체</option>
<option value="KRX">KRX</option>
<option value="KOSDAQ">KOSDAQ</option>
<option value="NASDAQ">NASDAQ</option>
<option value="NYSE">NYSE</option>
</select>
<label class="sf-label" for="sf-verdict">판정</label>
<select class="sf-select" id="sf-verdict" data-f="verdict">
<option value="">전체</option>
<option value="cand">매수후보</option>
<option value="watch">매수관찰</option>
<option value="nobuy">매수불가</option>
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


_VERDICT_KIND  = {"매수후보": "cand", "매수관찰": "watch", "매수불가": "nobuy"}
_VERDICT_ORDER = {"매수후보": 0, "매수관찰": 1, "매수불가": 2}


def _verdict_cell(verdict: str, reason: str) -> str:
    """판정을 색상 배지 HTML로 렌더 (사유는 옆에 옅은 글씨).

    md_in_html 확장으로 표 셀 내 인라인 HTML이 렌더된다. .verdict-sort span은
    Tablesort가 textContent로 정렬할 때 우선순위 숫자(0/1/2)를 앞에 붙여
    매수후보→매수관찰→매수불가 순서를 강제한다.
    """
    kind = _VERDICT_KIND.get(verdict, "nobuy")
    sort_key = _VERDICT_ORDER.get(verdict, 9)
    badge = f'<span class="verdict-sort">{sort_key}</span><span class="verdict verdict-{kind}">{verdict}</span>'
    if reason:
        return f'{badge} <span class="verdict-reason">({reason})</span>'
    return badge


def _candidate_days_cell(days: str) -> str:
    """candidate-days 프론트매터 → 'D+N' 셀 (임계 초과는 '만료' — 재전환 대기).

    매수후보가 아니거나 구형 스냅샷이면 빈 문자열.
    임계는 CANDIDATE_FRESH_MAX_DAYS (모듈 상단, core와 동기화 대상).
    """
    try:
        n = int(days)
    except (TypeError, ValueError):
        return ""
    return f"D+{n} 만료" if n > CANDIDATE_FRESH_MAX_DAYS else f"D+{n}"


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
                    "entry_stop", "trail_stop", "alert_above", "shares"}
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


def _collect_watchlist() -> list[tuple[str, str, str, str]]:
    """type=watchlist 만 복사하고 (ticker, market, name, fname) 리스트 반환.

    출력 파일명은 {ticker}.md (ASCII only) — 한글 파일명은 GitHub Pages에서
    URL 인코딩 불일치로 404가 발생하므로 여기서 강제 변환한다.

    원자적 교체: 임시 디렉터리에 복사 완료 후 OUT_WL과 스왑 — 크래시 시
    기존 OUT_WL을 손상시키지 않는다.
    """
    tmp = OUT_WL.parent / f"{OUT_WL.name}_tmp"
    _reset_dir(tmp)
    entries = []
    for md in sorted(SRC_WL.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        fm = _frontmatter(text)
        if fm.get("type") != "watchlist":
            continue
        ticker = fm.get("ticker", md.stem)
        out_name = f"{ticker}.md"   # ASCII-only: 한글 파일명 → 티커만
        # 실계좌 필드·private 블록 제거 후 복사 — 원본(비공개)은 그대로 유지
        (tmp / out_name).write_text(_sanitize_public_md(text), encoding="utf-8")
        entries.append((ticker, fm.get("market", ""),
                        _company_name(fm.get("title", "")), out_name))
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
            "price":   fm.get("price", ""),
            "market":  fm.get("market", ""),
            "days":    fm.get("candidate-days", ""),   # 매수후보 경과 거래일 (구형 스냅샷은 "")
            "gap":     fm.get("sma50-gap-pct", ""),    # SMA50 이격 %
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
    """현재 열린 매수후보/관찰 포지션을 core.positions로 복원해 dict 리스트로 반환.

    진입가 = 첫 매수전환 스냅샷가, 현재가 = 최신 스냅샷가(라이브 fetch 없음).
    core 미탑재(스냅샷 없음 등)면 빈 리스트. 렌더러는 plain dict만 받아 테스트 가능.
    """
    import sys
    if str(ROOT.parent) not in sys.path:
        sys.path.insert(0, str(ROOT.parent))
    try:
        from core.outcome import load_snapshot_series
        from core.positions import build_open_positions
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
        "entry_price":   p.entry_price,
        "stop_price":    p.stop_price,
        "current_price": p.current_price,
        "return_pct":    p.return_pct,
        "r_multiple":    p.r_multiple,
        "to_stop_pct":   p.to_stop_pct,
        "to_target_pct": p.to_target_pct,
        "days_held":     p.days_held,
    } for p in positions]


def _collect_completed_trades() -> dict:
    """data/completed_trades.json 로드 (--completed-trades 산출물). 없으면 {}."""
    if not COMPLETED_TRADES_JSON.exists():
        return {}
    try:
        return json.loads(COMPLETED_TRADES_JSON.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


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

def _stat_cards(entries, snaps, alerts, positions=None) -> str:
    n_watch  = len(entries)
    n_cand   = sum(1 for s in snaps if s["verdict"] == "매수후보")
    n_obs    = sum(1 for s in snaps if s["verdict"] == "매수관찰")
    n_snaps  = len(snaps)
    n_alerts = len(alerts)
    n_pos    = len(positions or [])
    return (
        # 주의: 원시 HTML href는 MkDocs가 재작성하지 않으므로 .md가 아니라
        # 디렉터리 URL(use_directory_urls)로 직접 링크한다. .md면 배포 시 404.
        '<div class="stat-grid">'
        f'<a class="stat-card" href="watchlist/">'
        f'<div class="stat-card__num">{n_watch}</div>'
        f'<div class="stat-card__label">관찰 종목</div></a>'
        f'<a class="stat-card stat-card--cand" href="snapshots/">'
        f'<div class="stat-card__num">{n_cand}</div>'
        f'<div class="stat-card__label">매수후보</div></a>'
        f'<a class="stat-card stat-card--watch" href="snapshots/">'
        f'<div class="stat-card__num">{n_obs}</div>'
        f'<div class="stat-card__label">매수관찰</div></a>'
        f'<a class="stat-card" href="positions/">'
        f'<div class="stat-card__num">{n_pos}</div>'
        f'<div class="stat-card__label">오픈 포지션</div></a>'
        f'<a class="stat-card" href="performance/">'
        f'<div class="stat-card__num">📈</div>'
        f'<div class="stat-card__label">전략 성과</div></a>'
        f'<a class="stat-card" href="snapshots/">'
        f'<div class="stat-card__num">{n_snaps}</div>'
        f'<div class="stat-card__label">스냅샷</div></a>'
        f'<a class="stat-card" href="alerts/">'
        f'<div class="stat-card__num">{n_alerts}</div>'
        f'<div class="stat-card__label">알림</div></a>'
        '</div>'
    )


def _dashboard(entries, snaps, alerts, names, positions=None) -> str:
    lines = [
        "# 주식 분석 리포트",
        "",
        "Weinstein 스테이지 · Minervini Trend Template · Turtle ATR 3레이어 프레임워크 기반 종목 분석.",
        "",
        _stat_cards(entries, snaps, alerts, positions),
        "",
        "## 바로 가기",
        "",
        f"- 📋 **관찰 종목** {len(entries)}개 — [목록 보기](watchlist/index.md)",
        f"- 💹 **오픈 포지션** {len(positions or [])}개 — [수익률·R·시드 계산 보기](positions/index.md)",
        "- 📈 **전략 성과** — [손익비·기대값·승률 보기](performance/index.md)",
        f"- 📊 **분석 스냅샷** {len(snaps)}건 — [최신순 보기](snapshots/index.md)",
        f"- 🔔 **알림** {len(alerts)}건 — [타임라인 보기](alerts/index.md)" if alerts else "- 🔔 **알림** 없음",
        "- 📊 **시장 현황** — [VIX · Fear&Greed · 섹터 흐름](fear-index.md)",
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
        '??? info "📘 TT (Trend Template — Minervini 8조건)란?"',
        "    Mark Minervini가 정의한 상승 구조 체크리스트. **충족 조건 수 / 8** 로 점수화.",
        "",
        "    | # | 조건 |",
        "    |---|------|",
        "    | 1 | 현재가 > 150일 MA, 200일 MA |",
        "    | 2 | 150일 MA > 200일 MA |",
        "    | 3 | 200일 MA 최소 1개월째 상승 중 |",
        "    | 4 | 50일 MA > 150일 MA, 200일 MA |",
        "    | 5 | 현재가 > 50일 MA |",
        "    | 6 | 현재가 ≥ 52주 저점 × 1.25 (+25% 이상) |",
        "    | 7 | 현재가 ≥ 52주 고점 × 0.75 (-25% 이내) |",
        "    | 8 | RS Rating(상대강도 등급) ≥ 70 |",
        "",
        "    **8/8**: 매수후보 조건 충족 · **6~7/8**: 매수관찰 · **5/8 이하**: 기준미달",
        "",
        '??? info "📘 진입 게이팅 — 점수가 만점이어도 매수불가가 되는 4가지"',
        "    Stage·TT 점수와 별개로, 아래 조건에 걸리면 매수후보에서 제외됩니다 (2026-06-11 도입).",
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


def _watchlist_index(entries, latest_by_ticker=None) -> str:
    """관찰 종목 목록 — 최신 스냅샷의 판정·Stage·TT·현재가를 병기.

    컬럼 순서 주의: 판정=4번째(cells[3])·Stage=5번째(cells[4])는
    tablesort.js의 필터 인덱스와 맞춰져 있다 (스냅샷 인덱스와 동일 규약).
    """
    latest_by_ticker = latest_by_ticker or {}
    lines = [
        "# 관찰 종목",
        "",
        "모니터링 대상 종목. 30분 폴링으로 상태 변화 시 [알림](../alerts/index.md)이 발송됩니다. "
        "판정·Stage·TT·현재가는 각 종목의 **최신 분석 스냅샷** 기준입니다. "
        "**경과**는 매수후보 연속 경과 거래일(D+N) — 전환일이 D+0이며, "
        f"매수 추천은 **D+{CANDIDATE_FRESH_MAX_DAYS}까지만 유효**합니다. "
        "이를 넘기면 '만료'로 표시되고 "
        "푸시 알림도 나가지 않습니다(백테스트상 지연 진입은 기대값 감쇠 — 비매수로 "
        "내려갔다 재전환하면 D+0 새 추천으로 부활). "
        "이격·실질 손익비 등 진입 타이밍 상세는 각 종목 스냅샷의 '진입 · 손절 · 타겟' 표에 있습니다.",
        "",
        WL_FILTERS,
        # 컬럼 순서 = 폰 폭 우선순위 (2026-07-19): 종목·기업명·판정·현재가가
        # 앞 4열(≈324px)이라 스크롤 없이 보이고, 보조 지표는 오른쪽으로 밀린다.
        # 필터는 헤더 이름으로 열을 찾으므로(tablesort.js) 순서를 바꿔도 안전하다.
        # 경과 = 매수후보 연속 경과 거래일 D+N (후보만 표시, 임계 초과는 '만료')
        "| 종목 | 기업명 | 판정 | 현재가 | 경과 | Stage | TT | 시장 |",
        "|------|--------|------|-------:|------|-------|----|------|",
    ]
    for ticker, market, name, fname in sorted(entries):
        s = latest_by_ticker.get(ticker)
        if s:
            verdict = _verdict_cell(s["verdict"], s["reason"])
            stage, tt = s["stage"], f"{s['tt']}/8" if s["tt"] else ""
            price = _fmt_price_str(s["price"], market)
            days = _candidate_days_cell(s.get("days", ""))
        else:
            verdict = stage = tt = price = days = ""
        lines.append(f"| [**{ticker}**]({fname}) | [{name}]({fname}) "
                     f"| {verdict} | {price} | {days} | {stage} | {tt} | {market} |")
    return "\n".join(lines) + "\n"


def _snapshots_index(snaps, names) -> str:
    lines = [
        "# 분석 스냅샷",
        "",
        "특정 시점의 **판정 기록**(최신순). 판정 어휘 — "
        "**매수후보**(Stage 2 + TT 8/8) · **매수관찰**(Stage 2 + TT 6~7) · "
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
            f"| {s['stage']} | {s['tt']}/8 | {s['created']} |"
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
        "# 오픈 포지션",
        "",
        "현재 **매수후보/매수관찰** 판정인 종목의 진입가 대비 현재 수익률·R-배수. "
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
        "    | **+3R** | 목표 도달 (3:1 리워드) |",
        "    | **+1.5R** | 손절선을 본전으로 올릴 때 |",
        "    | **+1R** | 각오한 위험만큼 벌었다 |",
        "    | **0R** | 본전 |",
        "    | **−1R** | 손절 도달 (청산) |",
        "",
    ]
    if not positions:
        lines += [
            '!!! info "열린 포지션 없음"',
            "    현재 매수후보/매수관찰 판정인 종목이 없습니다. "
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
        link = f"../snapshots/{t}-{p['current_date']}.md"
        dot = "🟢" if p["r_multiple"] > 0 else ("🔴" if p["r_multiple"] < 0 else "⚪")
        lines.append(
            f"| [**{t}**]({link}) {name} | {_verdict_cell(p['verdict'], '')} "
            f"| {p['entry_date'][5:]} "
            f"| {_fmt_price(p['market'], p['entry_price'])} "
            f"| {_fmt_price(p['market'], p['current_price'])} "
            f"| {dot} {p['return_pct']:+.1f}% "
            f"| {p['r_multiple']:+.1f}R "
            f"| {p['to_stop_pct']:+.1f}% "
            f"| {p['to_target_pct']:+.1f}% "
            f"| {p['days_held']}일 "
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


def _performance_index(data: dict) -> str:
    """완결 트레이드 기준 verdict별 손익비·기대값·승률(CI) 성과 페이지."""
    generated = data.get("generated", "")
    summary = data.get("summary", {})
    n_trades = len(data.get("trades", []))

    lines = [
        "# 전략 성과",
        "",
        "**완결된 트레이드**(손절·목표달성·시간청산)를 판정(매수후보/매수관찰)별로 집계한 "
        "승률·손익비·기대값입니다. 진입가·손절가는 분석 스냅샷 기준이며, 미청산 오픈 포지션은 "
        "제외됩니다(청산돼야 집계).",
        "",
        '!!! warning "표본이 작습니다 — 우열 단정 금지"',
        "    이 수치는 워치리스트의 실현 트레이드 기반이라 표본이 작고 생존편향이 있습니다. "
        "**승률 옆 신뢰구간(CI)이 넓으면 통계적으로 의미 없는 노이즈**입니다. "
        "전략 우열의 더 정직한 추정은 유니버스 PIT 백테스트(shadow-backfill)이며, 이 표는 "
        "실제 관찰 종목의 사후 성과 기록으로만 읽으세요.",
        "",
    ]

    if not summary:
        lines += [
            '!!! info "아직 완결된 트레이드가 없습니다"',
            "    현재 진입 이벤트가 모두 **미청산**(손절·목표·60일 보유 미도달) 상태입니다. "
            "포지션이 청산되면 이 표가 자동으로 채워집니다.",
            "",
            f"> 기준일: {generated or '—'}",
            "",
            DISCLAIMER,
        ]
        return "\n".join(lines) + "\n"

    lines += [
        "| 판정 | n | 승률 (95% CI) | 손익비 | 기대값 | 손절 | 목표 | 시간청산 | 독립진입일 |",
        "|------|---|--------------|--------|--------|------|------|---------|-----------|",
    ]
    for verdict in sorted(summary, key=lambda v: _VERDICT_ORDER.get(v, 9)):
        s = summary[verdict]
        payoff = s.get("payoff_ratio")
        payoff_str = f"{payoff:.2f}" if payoff is not None else "n/a"
        ci_lo = s.get("win_rate_ci_low", 0.0) * 100
        ci_hi = s.get("win_rate_ci_high", 0.0) * 100
        lines.append(
            f"| {_verdict_cell(verdict, '')} | {s['n']} "
            f"| {s['win_rate']*100:.0f}% ({ci_lo:.0f}–{ci_hi:.0f}%) "
            f"| {payoff_str} | {s['expectancy']:+.2f}R "
            f"| {s['stop_rate']*100:.0f}% | {s['target_rate']*100:.0f}% "
            f"| {s['time_exit_rate']*100:.0f}% | {s.get('distinct_entry_days','—')} |"
        )
    lines += [
        "",
        f"> 완결 트레이드 {n_trades}건 · 기준일: {generated} · "
        "`python monitor.py --completed-trades` 로 갱신",
        "",
        '??? info "📘 손익비·기대값이 뭔가요?"',
        "    - **손익비** = 평균 이익(R) ÷ 평균 손실(R). 2.0이면 이길 때 질 때의 2배를 번다는 뜻.",
        "    - **기대값** = 승률×평균이익 − 패률×평균손실. **한 번 매매당 기대 R**. 양수면 장기적으로 우위.",
        "    - **독립진입일** = 서로 다른 날 진입한 건수. n보다 훨씬 작으면 같은 날 몰린 상관 표본이라 "
        "실제 정보량은 적습니다.",
        "",
        DISCLAIMER,
    ]
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


def _sector_flow_section(data: "dict | None") -> list[str]:
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
        ">",
        "> 한·미는 통화·데이터 소스가 달라 **별도 순위**입니다. 두 시장 점수를 직접 비교하지 마세요.",
        "",
        *_rank_table("미국 (S&P 500 섹터 ETF)", data.get("us") or [], "섹터", show_vol_share=True),
        *_rank_table("한국 (KODEX/TIGER 섹터 ETF)", data.get("kr") or [], "섹터", show_vol_share=True),
    ]
    return lines


def _theme_flow_section(data: "dict | None") -> list[str]:
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
        "> **KR**: 전력(4종)·기판(5종)·피지컬AI(3종) 균등가중 바스켓",
        "",
        *_rank_table("미국 테마", data.get("theme_us") or [], "테마", show_vol_share=False),
        *_rank_table("한국 테마", data.get("theme_kr") or [], "테마", show_vol_share=False),
    ]
    return lines


def _trade_report_section(data: "dict | None") -> list[str]:
    """수출입 동향 보도자료 → 대시보드 섹션 마크다운."""
    lines = ["## 수출입 동향 (산업통상자원부)", ""]
    if not data:
        lines += [
            '!!! info "수출입 동향 데이터 없음"',
            "    보도자료 PDF를 업로드 후 `python monitor.py --trade-report <파일경로>` 를 실행하면 자동 갱신됩니다.",
            "",
        ]
        return lines

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


def _fear_index_page(latest=None, names=None) -> str:
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
                f"| {s['stage']} | {s['tt']}/8 |"
            )
        rows += ["", "[→ 전체 스냅샷](snapshots/index.md)", ""]
        return rows

    if not FEAR_INDEX_JSON.exists():
        return (
            "# 시장 현황\n\n"
            + "\n".join(_recent_analysis_section()) + "\n"
            + _TV_HEATMAP
            + "\n"
            + "\n".join(_sector_flow_section(sector))
            + "\n"
            + "\n".join(_theme_flow_section(sector))
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
        *_sector_flow_section(sector),
        *_theme_flow_section(sector),
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

    entries = _collect_watchlist()
    snaps   = _collect_snapshots()          # 전체 히스토리 (파일 복사 완료)
    latest  = _latest_per_ticker(snaps)     # 인덱스·대시보드용: 종목당 최신 1건
    alerts  = _scan_alerts()
    positions = _collect_positions()        # 현재 열린 매수후보/관찰 포지션
    perf    = _collect_completed_trades()   # 완결 트레이드 손익비 성과
    names   = {ticker: name for ticker, _market, name, _fname in entries}
    # 워치리스트에서 뺀 종목의 옛 스냅샷은 목록·대시보드에서 제외한다 (2026-08-23).
    # 파일은 그대로 복사되므로 히스토리 URL과 백테스트 원자료는 보존된다.
    # 계기: 6월에 정리한 7종목(BMNR·CEG 등)이 최신 목록 사이에 6월 날짜로 남아
    # "스냅샷 갱신이 멈췄다"는 오해를 불렀다.
    retired = [s["ticker"] for s in latest if s["ticker"] not in names]
    latest  = [s for s in latest if s["ticker"] in names]

    OUT_POS.mkdir(parents=True, exist_ok=True)
    OUT_PERF.mkdir(parents=True, exist_ok=True)
    (OUT / "index.md").write_text(_dashboard(entries, latest, alerts, names, positions), encoding="utf-8")
    (OUT / "fear-index.md").write_text(_fear_index_page(latest, names), encoding="utf-8")
    latest_map = {s["ticker"]: s for s in latest}
    (OUT_WL / "index.md").write_text(_watchlist_index(entries, latest_map), encoding="utf-8")
    (OUT_SNAP / "index.md").write_text(_snapshots_index(latest, names), encoding="utf-8")
    (OUT_ALERT / "index.md").write_text(_alerts_index(alerts, names), encoding="utf-8")
    (OUT_POS / "index.md").write_text(_positions_index(positions, names), encoding="utf-8")
    (OUT_PERF / "index.md").write_text(_performance_index(perf), encoding="utf-8")

    print(f"생성 완료: 관찰 {len(entries)}개 · 스냅샷 {len(latest)}종목({len(snaps)}건, "
          f"목록 제외 {len(retired)}종목) "
          f"· 알림 {len(alerts)}건 · 오픈 포지션 {len(positions)}개 "
          f"· 완결 트레이드 {len(perf.get('trades', []))}건")


if __name__ == "__main__":
    main()
