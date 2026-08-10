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


def test_collect_watchlist_strips_private_fields_and_blocks(tmp_path, monkeypatch):
    # 실계좌 프론트매터 필드(held/buy_price 등)와 <!-- private --> 본문 블록은
    # 공개 복사본에서 제거돼야 한다 — "리포트만 공개" 정책 (2026-07-16)
    src = tmp_path / "src"
    out = tmp_path / "out"
    src.mkdir()
    monkeypatch.setattr(gen, "SRC_WL", src)
    monkeypatch.setattr(gen, "OUT_WL", out)

    (src / "MSFT-x.md").write_text(
        "---\n"
        "type: watchlist\n"
        "ticker: MSFT\n"
        "market: NASDAQ\n"
        "title: Microsoft 관찰 종목\n"
        "held: true\n"
        "buy_price: 371.86\n"
        "alert_above: 12.52\n"
        "---\n"
        "# 메모\n"
        "\n"
        "<!-- private -->\n"
        "실제 매수가 $371.86로 보유 중 등록.\n"
        "<!-- /private -->\n"
        "공개 분석 문단.\n",
        encoding="utf-8")

    entries = gen._collect_watchlist()
    assert [e[0] for e in entries] == ["MSFT"]

    pub = (out / "MSFT.md").read_text(encoding="utf-8")
    assert "held" not in pub
    assert "buy_price" not in pub
    assert "alert_above" not in pub
    assert "371.86" not in pub
    assert "공개 분석 문단." in pub
    assert "ticker: MSFT" in pub


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
    assert 'href="positions/"' in html


# ── 오픈 포지션 페이지 ──────────────────────────────────────────────────────

def _pos(ticker: str, r: float, **over) -> dict:
    base = {
        "ticker": ticker, "market": "NASDAQ", "verdict": "매수후보",
        "entry_date": "2026-06-30", "current_date": "2026-07-09",
        "entry_price": 100.0, "stop_price": 90.0, "current_price": 100.0 + r * 10,
        "return_pct": r * 10, "r_multiple": r,
        "to_stop_pct": -10.0, "to_target_pct": 20.0, "days_held": 9,
    }
    base.update(over)
    return base


def test_positions_index_sorts_by_r_desc():
    md = gen._positions_index([_pos("LOW", 0.5), _pos("HIGH", 2.5)], {})
    assert md.index("HIGH") < md.index("LOW")


def test_positions_index_empty_shows_notice():
    md = gen._positions_index([], {})
    assert "열린 포지션 없음" in md


def test_positions_index_has_r_explainer():
    # 공개 페이지에 R 개념 설명(접이식)이 항상 있어야 한다 — 초보 열람자 대상.
    md = gen._positions_index([], {})
    assert "R이 뭔가요" in md
    assert "각오한" in md          # 손절폭 설명
    assert "+1.5R" in md           # 규칙 트리거 표


def test_positions_index_footer_aggregates():
    md = gen._positions_index([_pos("A", 2.0), _pos("B", -1.0)], {})
    assert "2포지션" in md
    assert "양의 R 1/2" in md


def test_positions_index_krw_currency():
    md = gen._positions_index([_pos("005930", 1.0, market="KRX",
                                     entry_price=70000, current_price=80000)], {})
    assert "₩70,000" in md
    assert "₩80,000" in md


def test_positions_index_links_to_dated_snapshot():
    md = gen._positions_index([_pos("NVDA", 1.0)], {})
    assert "../snapshots/NVDA-2026-07-09.md" in md


def test_fmt_price_us_vs_kr():
    assert gen._fmt_price("NASDAQ", 181.05) == "$181.05"
    assert gen._fmt_price("KRX", 70000) == "₩70,000"


def test_positions_index_embeds_sizing_data():
    # JS 사이징 계산에 필요한 stop/current/r 이 pos-data JSON에 실려야 한다.
    import json as _json
    md = gen._positions_index([_pos("NVDA", 1.0, stop_price=90.0)], {})
    assert 'id="pos-data"' in md
    assert 'id="seed-input"' in md           # 시드 입력창
    assert 'class="js-shares"' in md          # 주수 placeholder
    assert 'class="js-pnl"' in md             # 손익(원) placeholder
    payload = md.split('id="pos-data">')[1].split("</script>")[0]
    data = _json.loads(payload)
    assert data[0]["stop"] == 90.0
    assert data[0]["current"] == 110.0        # entry 100 + r*10
    assert data[0]["r"] == 1.0


# ── 전략 성과 페이지 ────────────────────────────────────────────────────────

def _summary(**over):
    base = {
        "n": 10, "win_rate": 0.6, "win_rate_ci_low": 0.31, "win_rate_ci_high": 0.83,
        "avg_win_r": 2.0, "avg_loss_r": 1.0, "payoff_ratio": 2.0, "expectancy": 0.8,
        "stop_rate": 0.4, "target_rate": 0.5, "time_exit_rate": 0.1, "data_end_rate": 0.0,
        "distinct_tickers": 8, "distinct_entry_days": 6,
    }
    base.update(over)
    return base


def test_performance_index_empty_shows_reason():
    md = gen._performance_index({"generated": "2026-07-09", "trades": [], "summary": {}})
    assert "아직 완결된 트레이드" in md
    assert "미청산" in md


def test_performance_index_renders_payoff_and_ci():
    md = gen._performance_index({
        "generated": "2026-07-09", "trades": [{}] * 10,
        "summary": {"매수후보": _summary()},
    })
    assert "손익비" in md
    assert "2.00" in md                        # payoff_ratio
    assert "31–83%" in md                      # Wilson CI
    assert "+0.80R" in md                      # expectancy
    assert "표본이 작습니다" in md              # 소표본 경고


def test_performance_index_payoff_none_shows_na():
    md = gen._performance_index({
        "generated": "2026-07-09", "trades": [{}] * 3,
        "summary": {"매수관찰": _summary(payoff_ratio=None)},
    })
    assert "n/a" in md


def test_collect_completed_trades_missing_returns_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(gen, "COMPLETED_TRADES_JSON", tmp_path / "nope.json")
    assert gen._collect_completed_trades() == {}


def test_stat_cards_include_performance_link():
    html = gen._stat_cards([], [], [])
    assert 'href="performance/"' in html


def test_candidate_days_cell():
    """경과 컬럼 셀 — 후보만 D+N, D+5 초과는 '만료', 구형/비후보는 빈칸 (2026-08-07).

    임계 5는 core.notifier.CANDIDATE_FRESH_MAX_DAYS와 같아야 한다.
    """
    from gen import _candidate_days_cell
    assert _candidate_days_cell("4") == "D+4"
    assert _candidate_days_cell(5) == "D+5"
    assert _candidate_days_cell(6) == "D+6 만료"
    assert _candidate_days_cell(18) == "D+18 만료"
    assert _candidate_days_cell("") == ""
    assert _candidate_days_cell(None) == ""


def test_watchlist_index_has_days_column():
    from gen import _watchlist_index
    entries = [("GS", "NYSE", "골드만삭스", "GS.md")]
    latest = {"GS": {"verdict": "매수후보", "reason": "", "stage": "2",
                     "tt": "8", "price": "1074.51", "days": "18"}}
    md = _watchlist_index(entries, latest)
    assert "| 경과 |" in md
    assert "D+18 만료" in md
