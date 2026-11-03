"""시장 국면은 참고 표시다. 진입을 막는 것처럼 적지 않는다 (게이트는 2026-07-13 제거)."""
import json

from sitegen import market_page


def _page(tmp_path, monkeypatch, regime):
    path = tmp_path / "fear_index.json"
    path.write_text(json.dumps({"updated_at": "2026-11-03", "us_regime": regime,
                                "vix": {"value": 30.0, "change": 1.0, "grade": "공포", "grade_emoji": "🔴"}}),
                    encoding="utf-8")
    monkeypatch.setattr("sitegen.config.FEAR_INDEX_JSON", path)
    return market_page._fear_index_page()


def test_downtrend_row_says_reference_only(tmp_path, monkeypatch):
    page = _page(tmp_path, monkeypatch, "DOWNTREND")
    assert "| 하락 | ⚠️ 하락 위험 |" in page
    assert "알림을 막지 않습니다" in page


def test_page_has_no_gate_wording(tmp_path, monkeypatch):
    for regime in market_page._REGIME_ENTRY:
        page = _page(tmp_path, monkeypatch, regime)
        for word in ("금지", "허용", "자제", "신규 진입"):
            assert word not in page, (regime, word)
