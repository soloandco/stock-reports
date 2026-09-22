"""관찰 페이지 「거물 투자자(13F)」 절 (2026-09-22)."""
import gen

DATA = {"as_of": "2026-09-22", "period": "2026-06-30", "tickers": {
    "MSFT": {"famous": [{"name": "Buffett", "weight": 0.123, "new": True},
                        {"name": "Ackman", "weight": 0.05, "new": False}],
             "famous_holders": 2, "famous_new": 1, "conc_holders": 7, "conc_new": 2},
    "XLE": {"famous": [], "famous_holders": 0, "famous_new": 0, "conc_holders": 0, "conc_new": 0}}}


def test_block_shows_counts_and_rows():
    b = gen._superinvestor_block("MSFT", DATA)
    assert "## 거물 투자자 (13F)" in b
    assert "**2곳 보유**" in b and "신규 **1곳**" in b and "집중 투자 기관 7곳 보유(신규 2곳)" in b
    assert "| Buffett | 12.3% | 신규 |  |" in b and "| Ackman | 5.0% | 보유 |  |" in b
    assert "2026-06-30 기준" in b and "매수 신호가 아닙니다" in b


def test_block_without_holders_has_no_table():
    b = gen._superinvestor_block("XLE", DATA)
    assert "0곳 보유" in b and "| 투자자 |" not in b


def test_unknown_ticker_or_missing_file_gives_nothing():
    assert gen._superinvestor_block("NVDA", DATA) == ""
    assert gen._superinvestor_block("MSFT", {}) == ""


def test_block_goes_right_after_chart():
    text = "# T\n\n## 분석\n본문\n"
    out = gen._insert_chart_block(text, "MSFT", gen._superinvestor_block("MSFT", DATA))
    assert out.index("## 차트") < out.index("## 거물 투자자") < out.index("## 분석")


def test_long_list_is_cut():
    many = {"tickers": {"A": {"famous": [{"name": f"M{i}", "weight": 0.02, "new": False}
                                         for i in range(13)], "famous_holders": 13}}}
    b = gen._superinvestor_block("A", many)
    assert "| M9 |" in b and "| M10 |" not in b and "외 3곳" in b


HOME = {"period": "2026-06-30", "top_new": [
    {"ticker": "SPGI", "name": "S&P Global Inc.", "holders": 6,
     "buyers": [{"name": "Bill Ackman - Pershing Square", "weight": 0.054},
                {"name": "Triple Frond Partners", "weight": 0.042}]},
    {"ticker": "WBD", "name": "", "holders": 2,
     "buyers": [{"name": "Daniel Loeb - Third Point", "weight": 0.115},
                {"name": "David Einhorn - Greenlight Capital", "weight": 0.015}]}]}


def test_home_table_links_watched_tickers_only():
    h = gen._superinvestor_home(HOME, {"SPGI": "S&P 글로벌"})
    assert "## 거물 신규 매수 (13F)" in h and "2026-06-30 기준" in h and "종목** 2개" in h
    assert "| [**SPGI**](watchlist/SPGI.md)<br>S&P 글로벌 | Bill Ackman 5.4% · Triple Frond Partners 4.2% | 2 |" in h
    assert "| **WBD**<br> | Daniel Loeb 11.5% · David Einhorn 1.5% | 2 |" in h
    assert "매수 신호가 아닙니다" in h


def test_home_table_absent_without_data_and_empty_quarter():
    assert gen._superinvestor_home({}, {}) == ""
    assert "이번 분기에는 없습니다" in gen._superinvestor_home({"top_new": []}, {})


def test_home_table_is_on_dashboard(monkeypatch):
    monkeypatch.setattr(gen, "_load_superinvestors", lambda: HOME)
    md = gen._dashboard([], [], [], {}, [])
    assert "## 거물 신규 매수 (13F)" in md


def test_sec_title_cleanup():
    assert gen._sec_title("APPLIED MATERIALS INC /DE") == "Applied Materials Inc"
    assert gen._sec_title("VISA INC.") == "Visa Inc."
    assert gen._sec_title("Meta Platforms, Inc.") == "Meta Platforms, Inc."


def test_cost_cell():
    c = {"avg": 44.66, "low": 39.15, "high": 48.8, "known": True}
    assert gen._cost_cell(c, 255.0) == "$44.66 (+471%)<br>$39.15~$48.80"
    assert gen._cost_cell({"avg": 413.86, "low": 355.86, "high": 488.31, "known": True}, 372.0) ==         "$414 (-10%)<br>$356~$488"
    assert gen._cost_cell({"known": False, "since": "2018-12-31"}, 50.0) == "모름<br>첫 신고(2018-12) 전부터 보유"
    assert gen._cost_cell({"known": False}, 50.0) == "모름"
    assert gen._cost_cell(None, 50.0) == ""


def test_block_shows_cost_column():
    data = {"period": "2026-06-30", "tickers": {"AAPL": {
        "price": 255.0, "famous_holders": 1, "famous_new": 0, "conc_holders": 3, "conc_new": 0,
        "famous": [{"name": "Warren Buffett - Berkshire Hathaway", "weight": 0.22, "new": False,
                    "cost": {"avg": 44.66, "low": 39.15, "high": 48.8, "known": True}}]}}}
    b = gen._superinvestor_block("AAPL", data)
    assert "| 투자자 | 비중 | 구분 | 추정 평단 |" in b
    assert "| Warren Buffett - Berkshire Hathaway | 22.0% | 보유 | $44.66 (+471%)<br>$39.15~$48.80 |" in b
