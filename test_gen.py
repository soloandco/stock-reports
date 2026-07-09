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


def test_monthly_stats_excludes_open_notes():
    notes = [
        {"status": "open", "exit_date": "", "r_multiple": "", "outcome": ""},
        {"status": "closed", "exit_date": "2026-07-05", "r_multiple": "2.0", "outcome": "win"},
    ]
    stats = gen._monthly_stats(notes)
    assert len(stats) == 1
    assert stats[0]["month"] == "2026-07"
    assert stats[0]["count"] == 1


def test_monthly_stats_computes_win_rate_avg_and_sum():
    notes = [
        {"status": "closed", "exit_date": "2026-07-05", "r_multiple": "2.0", "outcome": "win"},
        {"status": "closed", "exit_date": "2026-07-10", "r_multiple": "-1.0", "outcome": "loss"},
        {"status": "closed", "exit_date": "2026-07-15", "r_multiple": "2.2", "outcome": "win"},
    ]
    stats = gen._monthly_stats(notes)
    assert len(stats) == 1
    s = stats[0]
    assert s["count"] == 3
    assert round(s["win_rate"], 1) == 66.7
    assert round(s["avg_r"], 2) == 1.07
    assert round(s["sum_r"], 2) == 3.2


def test_monthly_stats_groups_by_month_desc():
    notes = [
        {"status": "closed", "exit_date": "2026-06-01", "r_multiple": "1.0", "outcome": "win"},
        {"status": "closed", "exit_date": "2026-07-01", "r_multiple": "1.0", "outcome": "win"},
    ]
    stats = gen._monthly_stats(notes)
    assert [s["month"] for s in stats] == ["2026-07", "2026-06"]


def test_stat_cards_use_directory_urls_not_md():
    # MkDocs는 원시 HTML의 href를 재작성하지 않는다 → .md 링크는 배포 시 404.
    # 홈 상단 stat-card는 디렉터리 URL(use_directory_urls)로 링크해야 한다.
    html = gen._stat_cards([], [], [])
    assert "index.md" not in html
    assert 'href="watchlist/"' in html
    assert 'href="snapshots/"' in html
    assert 'href="alerts/"' in html
