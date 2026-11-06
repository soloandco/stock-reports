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


def test_page_shows_only_pushed_recommendations_and_links_research():
    md = gen._strategies_index(DATA, {"PLTR": "팔란티어"})
    assert md.startswith("# 추천 기록")
    assert "| 09-09 | GEV | 스윙 | 손절 |" in md
    assert "PLTR" not in md                 # 기록만 한 추천은 연구 페이지 몫이다
    assert "R" not in md.split("## 더 보기")[0].replace("RSI", "")
    assert "(research.md)" in md and "../positions/index.md" in md


def test_research_page_keeps_period_table_and_switch_guide():
    md = gen._research_index(DATA)
    assert md.startswith("# 과거 비교 연구")
    assert "지금 켜진 방식: 단타" in md and "09-18 17:49" in md
    assert "| 09-04~09-18 | 스윙(알림) | 3 · 진행 4 | -1.00R |" in md
    assert "| | 단타(기록만) | 0 | — |" in md
    assert "/200건" in md and "「RSI 켜」" in md


def test_tables_have_no_class_and_at_most_four_columns():
    md = gen._strategies_index(DATA, {})
    for line in md.splitlines():
        if line.startswith("|"):
            assert line.count("|") <= 5          # 모바일: 4열 이하
    assert "<table" not in md


def test_missing_data_renders_placeholder():
    md = gen._strategies_index({}, {})
    assert "# 추천 기록" in md and "아직" in md


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
    assert "| RSI | 1건<br>-10,000 | 2건<br>+5,000 | **-5,000** |" in md
    assert "| 10-10 | AAA<br>100.00 · 목표 140.00 · 손절 92.00 | RSI | 진행 중 +2.0% |" in md


def test_rsi_is_absent_when_off_and_unrecorded():
    data = {**DATA, "rsi_on": False, "money": {"base": dict(_MONEY), "book": dict(_MONEY)}}
    md = gen._strategies_index(data, {})
    # 과거 연구 표에 RSI가 있어도 운영 RSI 안내는 켜지지 않아야 한다.
    assert "**RSI 방식**" not in md


def test_money_table_uses_capped_won_from_data():
    """분석 코드가 시드 상한까지 반영한 금액(closed_won 등)을 넘기면 그 값을 쓴다 (2026-10-16)."""
    money = {"book": {"closed": 1, "closed_r": -6.53, "closed_won": -35237.0,
                      "open": 0, "open_r": 0.0, "open_won": 0.0, "total_won": -35237.0}}
    md = gen._strategies_index({**DATA, "money": money, "seed_won": 1_000_000, "r_won": 10_000}, {})
    assert "1건<br>-35,237" in md and "-65,300" not in md


def test_money_table_old_data_falls_back_to_r():
    money = {"base": {"closed": 1, "closed_r": -1.0, "open": 0, "open_r": 0.0, "total_won": -10000.0}}
    md = gen._strategies_index({**DATA, "money": money, "seed_won": 1_000_000, "r_won": 10_000}, {})
    assert "1건<br>-10,000" in md


def test_money_table_shows_pending_and_home_matches():
    """체결 대기를 표와 홈이 같은 숫자로 말한다 (2026-11-07 unslop 002)."""
    from sitegen import home
    money = {"base": {"closed": 1, "closed_r": 0.0, "open": 2, "open_r": 0.0, "pending": 3, "total_won": 0.0}}
    md = gen._strategies_index({**DATA, "money": money, "seed_won": 1_000_000, "r_won": 10_000}, {})
    assert "2건<br>+0<br>대기 3건" in md
    assert "| 방식 | 끝남 (원) | 진행 중 (원) | 합계 (원) |" in md
    box = home._strategy_box({"money": money})
    assert "진행 2 · 대기 3" in box
