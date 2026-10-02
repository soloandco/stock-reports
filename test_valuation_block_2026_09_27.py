"""관찰 페이지 「가격 수준」 절 (2026-09-27)."""
import gen

BAND = [float(x) for x in range(10, 111)]          # 0분위 10배 ~ 100분위 110배
DATA = {"as_of": "2026-09-27", "tickers": {
    "PLTR": {"ttm": 6.0e9, "shares": 2.4e9, "band": BAND, "band_from": "2023-09-01",
             "band_to": "2026-09-25", "n": 756, "growth": 92.7, "growth_q": "2026-06-30"}}}


def _snap(price, gap="15.7"):
    return {"price": str(price), "gap": gap, "market": "NASDAQ"}


def test_block_computes_ps_from_snapshot_price_and_places_it_in_band():
    # 스냅샷 가격 185 × 주식수 2.4B ÷ 매출 6B = 74배
    b = gen._valuation_block("PLTR", _snap(185.0), DATA)
    assert "## 가격 수준 (참고)" in b
    assert "**74배**" in b                        # 185 × 2.4B / 6B
    assert "하위 64%" in b and "보통" in b          # 74 는 10~110 밴드의 64분위
    assert "10~110배" in b
    assert "+92.7%" in b and "2026-06 분기" in b
    assert "+15.7%" in b


def test_labels_cheap_and_expensive_thirds():
    assert "싼 편" in gen._valuation_block("PLTR", _snap(50.0), DATA)       # 20배 → 10%
    assert "비싼 편" in gen._valuation_block("PLTR", _snap(250.0), DATA)    # 100배 → 90%


def test_outside_band_says_so():
    assert "3년 중 가장 낮은 수준보다 아래" in gen._valuation_block("PLTR", _snap(10.0), DATA)
    assert "3년 중 가장 높은 수준보다 위" in gen._valuation_block("PLTR", _snap(400.0), DATA)


def test_nothing_for_etf_missing_price_or_file():
    assert gen._valuation_block("XLK", _snap(100.0), DATA) == ""
    assert gen._valuation_block("PLTR", {"price": ""}, DATA) == ""
    assert gen._valuation_block("PLTR", None, DATA) == ""
    assert gen._valuation_block("PLTR", _snap(185.0), {}) == ""


def test_block_says_it_is_not_a_buy_signal():
    b = gen._valuation_block("PLTR", _snap(185.0), DATA)
    assert "매수 신호가 아닙니다" in b


def test_block_sits_between_chart_and_13f(tmp_path, monkeypatch):
    import json
    src, out = tmp_path / "src", tmp_path / "out"
    src.mkdir()
    monkeypatch.setattr("sitegen.config.SRC_WL", src)
    monkeypatch.setattr("sitegen.config.OUT_WL", out)
    (tmp_path / "v.json").write_text(json.dumps(DATA), encoding="utf-8")
    monkeypatch.setattr("sitegen.config.VALUATION_JSON", tmp_path / "v.json")
    (tmp_path / "si.json").write_text(json.dumps({"period": "x", "tickers": {"PLTR": {
        "famous": [], "famous_holders": 0, "famous_new": 0, "conc_holders": 0, "conc_new": 0}}}),
        encoding="utf-8")
    monkeypatch.setattr("sitegen.config.SUPERINV_JSON", tmp_path / "si.json")
    (src / "PLTR.md").write_text("---\ntype: watchlist\nticker: PLTR\n---\n# T\n\n## 분석\n본문\n",
                                 encoding="utf-8")
    snap = {"fname": "PLTR-2026-09-27.md", "verdict": "매수불가", "price": "185", "gap": "15.7",
            "market": "NASDAQ"}
    gen._collect_watchlist({"PLTR": snap})
    page = (out / "PLTR.md").read_text(encoding="utf-8")
    assert page.index("stock-chart") < page.index("## 가격 수준") < page.index("## 거물 투자자")


def test_block_carries_measured_result():
    """측정 결과(id 41)를 문구로 붙인다. 「싼 편」 라벨이 매수 근거로 읽히지 않게."""
    b = gen._valuation_block("PLTR", _snap(185.0), DATA)
    assert "+0.43R" in b and "+0.19R" in b and "판정·알림에는 쓰지 않습니다" in b
