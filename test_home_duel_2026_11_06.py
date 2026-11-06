"""홈 「AI 대결」 수익률 순위 (2026-11-06 사용자 요청)."""
import json
import re
from pathlib import Path

from sitegen import config as cfg, home


def _write(tmp_path, monkeypatch, current, old=None):
    cur = tmp_path / "ai_duel_state.json"
    cur.write_text(json.dumps(current), encoding="utf-8")
    if old is not None:
        (tmp_path / "ai_duel_state.season1-20261106.json").write_text(json.dumps(old), encoding="utf-8")
    monkeypatch.setattr(cfg, "DUEL_STATE_JSON", cur)
    monkeypatch.setattr(cfg, "DUEL_DIR", tmp_path)


def test_current_season_ranked_by_equity(tmp_path, monkeypatch):
    _write(tmp_path, monkeypatch, {"history": [
        {"date": "2026-11-09", "opus": 10_100_000, "fable": 9_900_000, "gpt": 10_250_000,
         "rules": 10_000_000, "spy": 9_950_000}]})
    box = home._duel_box()
    names = re.findall(r"<span>\d\. ([^<]+)</span>", box)
    assert names == ["GPT", "Claude Opus", "규칙(스윙)", "SPY 보유", "Claude Fable"]
    assert "+2.50%" in box and "-1.00%" in box and "11-09 마감" in box


def test_empty_season_shows_last_season(tmp_path, monkeypatch):
    _write(tmp_path, monkeypatch, {"history": []}, {"history": [
        {"date": "2026-10-27", "claude": 10_000_000, "gpt": 10_000_000, "rules": 10_000_000, "spy": 10_000_000},
        {"date": "2026-11-05", "claude": 10_067_477, "gpt": 9_970_421, "rules": 9_807_689, "spy": 9_542_937}]})
    box = home._duel_box()
    assert "지난 시즌 10-27~11-05" in box and "새 시즌 준비 중" in box
    assert box.index("Claude") < box.index("GPT") < box.index("SPY")
    assert "+0.67%" in box and "-4.57%" in box


def test_no_file_gives_nothing(tmp_path, monkeypatch):
    monkeypatch.setattr(cfg, "DUEL_STATE_JSON", tmp_path / "none.json")
    monkeypatch.setattr(cfg, "DUEL_DIR", tmp_path)
    assert home._duel_box() == ""


def test_start_cash_matches_core():
    src = (Path(__file__).parent.parent / "core" / "ai_duel.py").read_text(encoding="utf-8")
    m = re.search(r"^START_CASH = ([\d_]+)", src, re.M)
    assert int(m.group(1).replace("_", "")) == home.DUEL_START_CASH
