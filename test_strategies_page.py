"""「방식별 기록」 페이지 (2026-09-19). 재료는 data/strategy_perf.json (monitor 가 만든다)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import gen

DATA = {
    "generated": "2026-09-19T08:00:00", "active": "book", "active_since": "2026-09-18T17:49:00",
    "min_n": 100,
    "periods": [
        {"strategy": "base", "start": "2026-09-04T02:10:16", "end": "2026-09-18T17:49:00",
         "active": {"closed": 3, "open": 4, "mean_r": -1.0, "stop_rate": 1.0},
         "other": {"closed": 0, "open": 0, "mean_r": None, "stop_rate": None}},
        {"strategy": "book", "start": "2026-09-18T17:49:00", "end": "2026-09-19T08:00:00",
         "active": {"closed": 0, "open": 0, "mean_r": None, "stop_rate": None},
         "other": {"closed": 0, "open": 1, "mean_r": None, "stop_rate": None}},
    ],
    "trades": [
        {"strategy": "base", "ts": "2026-09-19T05:40:00", "ticker": "PLTR", "pushed": False,
         "closed": False, "r": None, "result": "진행 중"},
        {"strategy": "base", "ts": "2026-09-09T05:40:00", "ticker": "GEV", "pushed": True,
         "closed": True, "r": -1.0, "result": "손절"},
    ],
}


def test_page_shows_active_strategy_periods_and_trades():
    md = gen._strategies_index(DATA, {"PLTR": "팔란티어"})
    assert md.startswith("# 방식별 기록")
    assert "지금 켜진 방식: 단타" in md and "09-18 17:49" in md
    assert "| 09-04~09-18 | 스윙(알림) | 3 · 진행 4 | -1.00R |" in md
    assert "| | 단타(기록만) | 0 | — |" in md
    assert "| 09-19 | PLTR | 스윙 · 기록만 | 진행 중 |" in md
    assert "| 09-09 | GEV | 스윙 | 손절 -1.00R |" in md
    assert "표본" in md


def test_tables_have_no_class_and_at_most_four_columns():
    md = gen._strategies_index(DATA, {})
    for line in md.splitlines():
        if line.startswith("|"):
            assert line.count("|") <= 5          # 모바일: 4열 이하
    assert "<table" not in md


def test_missing_data_renders_placeholder():
    md = gen._strategies_index({}, {})
    assert "# 방식별 기록" in md and "아직" in md
