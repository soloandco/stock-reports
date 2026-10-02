"""경로. 원고(../docs)·데이터(../data)를 읽어 사이트 원고(docs/)로 쓴다. 테스트는 이 경로를 바꿔 끼운다.

2026-10-02 gen.py 에서 나눴다. 다른 sitegen 모듈은 함수를 이름째 가져오지 않고
「모듈.이름」으로 부른다(테스트가 한 곳만 바꿔 끼워도 모든 호출에 먹게).
"""
from __future__ import annotations

from pathlib import Path


ROOT      = Path(__file__).parent.parent   # report-site/
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
# 관찰 페이지 「가격 수준」 재료 (2026-09-27). 주간 알림 점검이 만든다 (core/valuation_band.py)
VALUATION_JSON = ROOT.parent / "data" / "valuation_band.json"


# ── 관찰 페이지 캔들차트 ──────────────────────────────────────────────────
# 그림(PNG)이 아니라 숫자만 올리고 브라우저가 그린다. 관찰 페이지는 48종목이고
# 매일 갱신돼서 이미지로 커밋하면 한 번에 1.8MB씩 공개 저장소에 쌓인다
# (2026-08-29 실측: 종목당 37KB). 숫자는 종목당 약 6KB다.
OUT_WL_CHARTS = OUT_WL / "charts"
