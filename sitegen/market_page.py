"""「시장 현황」 페이지: 공포지수·섹터·테마·수출입 동향.

2026-10-02 gen.py 에서 나눴다. 다른 sitegen 모듈은 함수를 이름째 가져오지 않고
「모듈.이름」으로 부른다(테스트가 한 곳만 바꿔 끼워도 모든 호출에 먹게).
"""
from __future__ import annotations

import json

from sitegen import common, config as cfg





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


_FLOW_KO = {"매집": "돈 유입", "분산": "돈 유출", "중립": "중립"}


def _rank_table(title: str, ranking: list, entity_label: str) -> list[str]:
    """섹터/테마 신호 → 순위 표 (2026-11-05: 폰에서 넘치던 RS·매집일·분산일·비중 칸을 뺐다)."""
    if not ranking:
        return [f"### {title}", "", "_데이터 없음_", ""]
    rows = [f"### {title}", "", f"| 순위 | {entity_label} | 신호 |", "|---|---|---|"]
    for i, e in enumerate(ranking, 1):
        signal = e.get("signal", "")
        rows.append(f"| {i} | {e.get('name', '')} | {_SIGNAL_EMOJI.get(signal, '')} {_FLOW_KO.get(signal, signal)} |")
    return rows + [""]


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
            "    다음 스캔 때 채워집니다.",
            "",
        ]
        return lines

    updated = data.get("updated_at", "")
    lines += [
        f'<p class="m-fine">최근 20일 거래량으로 본 돈의 방향입니다. {updated} 기준</p>',
        *([">", "> 한·미는 통화·데이터 소스가 달라 **별도 순위**입니다. 두 시장 점수를 직접 비교하지 마세요."]
          if show_kr else []),
        "",
        *_rank_table("미국 (S&P 500 섹터 ETF)", data.get("us") or [], "섹터"),
        # 한국은 관찰 종목이 있을 때만 (2026-09-22: 09-05 한국 관찰 제외 뒤 쓰지 않는 칸)
        *(_rank_table("한국 (KODEX/TIGER 섹터 ETF)", data.get("kr") or [], "섹터")
          if show_kr else []),
    ]
    return lines


def _theme_flow_section(data: "dict | None", show_kr: bool = True) -> list[str]:
    """테마 바스켓 자금 흐름 섹션 마크다운 줄 생성."""
    lines = ["## 테마별 자금 흐름", ""]
    if not data or (not data.get("theme_us") and not data.get("theme_kr")):
        lines += [
            '!!! info "테마 데이터 없음"',
            "    다음 스캔 때 채워집니다.",
            "",
        ]
        return lines

    updated = data.get("updated_at", "")
    lines += [
        f'<p class="m-fine">돈이 어느 테마로 몰리는지 봅니다. {updated} 기준</p>',
        "",
        *_rank_table("미국 테마", data.get("theme_us") or [], "테마"),
        *(_rank_table("한국 테마", data.get("theme_kr") or [], "테마")
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


def _fear_index_page(names=None, show_kr: bool = True) -> str:
    """시장 현황: 공포·탐욕 → 변동성 → 섹터 → 테마 → 거물 매수 (2026-11-05 사용자 승인)."""
    from sitegen import home, watch_pages
    sector = _load_sector_flow()
    trade = _load_trade_report()
    names = names or {}
    tail = [_TV_HEATMAP, "",
            *_sector_flow_section(sector, show_kr),
            *_theme_flow_section(sector, show_kr),
            *_trade_report_section(trade),
            home._superinvestor_home(watch_pages._load_superinvestors(), names, link_prefix="../"), "",
            common.DISCLAIMER, ""]
    if not cfg.FEAR_INDEX_JSON.exists():
        return "\n".join(["# 시장 현황", "", *tail]) + "\n"

    data = json.loads(cfg.FEAR_INDEX_JSON.read_text(encoding="utf-8"))
    updated = data.get("updated_at", "")
    vix = data.get("vix")
    vkospi = data.get("vkospi")
    cnn_fg = data.get("cnn_fear_greed")

    def _row(label: str, entry) -> str:
        if entry is None:
            return f"| {label} | — | — | — |"
        change = entry.get("change", 0.0)
        sign = "+" if change > 0 else ""
        return (f"| {label} | {entry.get('value', 'N/A')} | {sign}{change} "
                f"| {entry.get('grade_emoji', '')} {entry.get('grade', 'N/A')} |")

    def _cnn_section(fg: dict) -> list[str]:
        if not fg:
            return []
        change = fg.get("change", 0.0)
        sign = "+" if change > 0 else ""
        rows = ["## 공포·탐욕 지수", "",
                f"**{fg.get('score', 0):.0f}** / 100 · {fg.get('rating_emoji', '⚪')} **{fg.get('rating_ko', '—')}** "
                f"· 어제보다 {sign}{change}", "",
                '??? note "구성 지표 7개"', "",
                "    | 지표 | 점수 | 등급 |", "    |------|------|------|"]
        for comp in fg.get("components", []):
            s = comp.get("score")
            s_str = f"{s:.1f}" if s is not None else "—"
            rows.append(f"    | {comp['label']} | {s_str} | {comp['rating_emoji']} {comp['rating_ko']} |")
        rows += ["", f'<p class="m-fine">{updated} 기준 · 출처 '
                 '<a href="https://edition.cnn.com/markets/fear-and-greed">CNN</a></p>', ""]
        return rows

    return "\n".join([
        "# 시장 현황", "",
        *_cnn_section(cnn_fg),
        "## 변동성", "",
        "| 지수 | 지금 | 어제보다 | 등급 |", "|------|------|------|------|",
        _row("VIX (미국)", vix),
        *([_row("코스피", vkospi)] if vkospi is not None else []),
        "",
        *tail,
    ]) + "\n"
