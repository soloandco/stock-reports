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
    assert "| Buffett | 12.3% | 신규 |" in b and "| Ackman | 5.0% | 보유 |" in b
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
