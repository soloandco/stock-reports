"""「시장 현황」 페이지: 공포지수·섹터·테마·수출입 동향.

2026-10-02 gen.py 에서 나눴다. 다른 sitegen 모듈은 함수를 이름째 가져오지 않고
「모듈.이름」으로 부른다(테스트가 한 곳만 바꿔 끼워도 모든 호출에 먹게).
"""
from __future__ import annotations

import json

from sitegen import common, config as cfg


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
    if not cfg.TRADE_REPORT_JSON.exists():
        return None
    try:
        return json.loads(cfg.TRADE_REPORT_JSON.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def _load_sector_flow() -> "dict | None":
    """data/sector_strength.json 로드. 없거나 오류면 None."""
    if not cfg.SECTOR_JSON.exists():
        return None
    try:
        return json.loads(cfg.SECTOR_JSON.read_text(encoding="utf-8"))
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
        top5 = sorted(latest[:5], key=lambda s: common._VERDICT_ORDER.get(s['verdict'], 9))
        for s in top5:
            name = names.get(s['ticker'], '')
            rows.append(
                f"| [**{s['ticker']}**](snapshots/{s['fname']}) | [{name}](snapshots/{s['fname']}) | {s['created']} | {common._verdict_cell(s['verdict'], s['reason'])} "
                f"| {s['stage']} | {s['tt']}/{s.get('ttmax', 8)} |"
            )
        rows += ["", "[→ 전체 스냅샷](snapshots/index.md)", ""]
        return rows

    if not cfg.FEAR_INDEX_JSON.exists():
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

    data = json.loads(cfg.FEAR_INDEX_JSON.read_text(encoding="utf-8"))
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
        common.DISCLAIMER,
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
