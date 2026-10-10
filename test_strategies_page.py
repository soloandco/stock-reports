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


# ── RSI 반등 방식 (2026-10-10): 스윙·단타와 따로 켜고 끄는 세 번째 방식 ─────────
_MONEY = {"closed": 0, "closed_r": 0.0, "open": 0, "open_r": 0.0, "unvalued": 0,
          "total_r": 0.0, "total_won": 0.0}


def test_rsi_row_and_note_appear_when_on():
    data = {**DATA, "rsi_on": True, "seed_won": 1_000_000, "r_won": 10000.0,
            "money": {"base": dict(_MONEY), "book": dict(_MONEY),
                      "rsi": {**_MONEY, "closed": 1, "closed_r": -1.0, "open": 2, "open_r": 0.5,
                              "total_r": -0.5, "total_won": -5000.0}},
            "trades": [{"strategy": "rsi", "ts": "2026-10-10T06:00:00", "ticker": "AAA",
                        "pushed": True, "closed": False, "r": 0.25, "pct": 0.02, "result": "진행 중",
                        "entry": 100.0, "stop": 92.0, "targets": [140.0]}]}
    md = gen._strategies_index(data, {})
    assert "**RSI 방식**" in md and "지금 켜져 있습니다" in md
    assert "| RSI | 1건 -10,000원 | 2건 +5,000원 | **-5,000원** |" in md
    assert "| 10-10 | AAA<br>100.00 · 목표 140.00 · 손절 92.00 | RSI | 진행 중 +0.25R (+2.0%) |" in md


def test_rsi_is_absent_when_off_and_unrecorded():
    data = {**DATA, "rsi_on": False, "money": {"base": dict(_MONEY), "book": dict(_MONEY)}}
    md = gen._strategies_index(data, {})
    assert "RSI" not in md
