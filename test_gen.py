"""gen.py 노트 수집·집계 테스트."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import gen


def _write_note(path: Path, **fm) -> None:
    lines = ["---"]
    for k, v in fm.items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    lines.append("본문")
    path.write_text("\n".join(lines), encoding="utf-8")


def test_collect_notes_returns_trade_notes_only(tmp_path, monkeypatch):
    src = tmp_path / "src"
    out = tmp_path / "out"
    src.mkdir()
    monkeypatch.setattr(gen, "SRC_NOTES", src)
    monkeypatch.setattr(gen, "OUT_NOTES", out)

    _write_note(src / "2026-07-01-PLTR.md", type="trade-note", ticker="PLTR",
                entry_date="2026-07-01", status="open")
    _write_note(src / "TEMPLATE.md", title="템플릿")  # type 없음 → 제외

    notes = gen._collect_notes()

    assert len(notes) == 1
    assert notes[0]["ticker"] == "PLTR"
    assert notes[0]["status"] == "open"
    assert (out / "2026-07-01-PLTR.md").exists()
    assert not (out / "TEMPLATE.md").exists()


def test_collect_notes_sorted_by_entry_date_desc(tmp_path, monkeypatch):
    src = tmp_path / "src"
    out = tmp_path / "out"
    src.mkdir()
    monkeypatch.setattr(gen, "SRC_NOTES", src)
    monkeypatch.setattr(gen, "OUT_NOTES", out)

    _write_note(src / "2026-06-01-AAA.md", type="trade-note", ticker="AAA",
                entry_date="2026-06-01", status="closed")
    _write_note(src / "2026-07-01-BBB.md", type="trade-note", ticker="BBB",
                entry_date="2026-07-01", status="open")

    notes = gen._collect_notes()

    assert [n["ticker"] for n in notes] == ["BBB", "AAA"]
