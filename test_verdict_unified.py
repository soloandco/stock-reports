"""사이트에서 매수후보·매수관찰이 「매수」 하나로 보인다 (2026-09-04 사용자 결정).

두 등급을 나눌 근거가 측정에 없다 (충족 조건 8개 +0.148R < 7개 +0.189R <
6개 +0.208R, n=13,187). 저장 값은 그대로 두고 표시·필터·정렬만 합친다.
"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import gen


def _snap(ticker, verdict, **kw):
    d = dict(ticker=ticker, verdict=verdict, fname=f"{ticker}-2026-09-04.md",
             created="2026-09-04", stage="2", tt="7", price="100", stop="94",
             weekly_pos="저항대아래", weekly_pct="5.0", rr="1.2", days="")
    d.update(kw)
    return d


# ── 표의 판정 배지 ────────────────────────────────────────────────────────
@pytest.mark.parametrize("stored", ["매수후보", "매수관찰"])
def test_badge_shows_merged_name(stored):
    html = gen._verdict_cell(stored, "")
    assert ">매수<" in html
    assert stored not in html          # 옛 등급 이름이 화면에 남지 않는다


@pytest.mark.parametrize("stored", ["매수후보", "매수관찰"])
def test_badge_uses_one_css_class(stored):
    """필터가 클래스명으로 걸리므로 두 등급이 같은 클래스여야 한다."""
    assert "verdict-buy" in gen._verdict_cell(stored, "")


def test_badge_keeps_reason():
    assert "(변동성과대)" in gen._verdict_cell("매수관찰", "변동성과대")


def test_non_buy_badges_unchanged():
    assert ">매수불가<" in gen._verdict_cell("매수불가", "")
    assert "verdict-nobuy" in gen._verdict_cell("매수불가", "")


def test_buy_sorts_ahead_of_nobuy():
    assert gen._VERDICT_ORDER["매수후보"] == gen._VERDICT_ORDER["매수관찰"]
    assert gen._VERDICT_ORDER["매수후보"] < gen._VERDICT_ORDER["매수불가"]


# ── 필터 드롭다운 ────────────────────────────────────────────────────────
def test_filter_has_one_buy_option():
    html = gen.SNAP_FILTERS
    assert '<option value="buy">매수</option>' in html
    assert "매수후보" not in html and "매수관찰" not in html
    assert html.count('<option value="buy">') == 1


def test_watchlist_filter_matches_snapshot_filter():
    """두 인덱스의 필터가 어긋나면 한쪽만 조용히 안 걸린다."""
    assert '<option value="buy">매수</option>' in gen.WL_FILTERS
    assert "매수관찰" not in gen.WL_FILTERS


# ── 홈 결론 카드 ─────────────────────────────────────────────────────────
def test_conclusion_lead_counts_buys_as_one_group():
    snaps = [_snap("AAA", "매수후보"), _snap("BBB", "매수관찰"), _snap("CCC", "매수불가")]
    out = gen._conclusion_section(snaps, {}, [])
    assert "매수 <b>2</b>" in out
    assert "매수후보" not in out and "매수관찰" not in out


def test_conclusion_empty_message_has_no_grade_names():
    out = gen._conclusion_section([_snap("CCC", "매수불가")], {}, [])
    assert "매수후보" not in out and "매수관찰" not in out


def test_pick_priority_does_not_favor_the_old_top_grade():
    """등급으로 앞세우지 않는다 — 8/8이 더 낫다는 근거가 없다."""
    watch_fresh = _snap("AAA", "매수관찰", weekly_pos="신고가영역")
    cand_worse  = _snap("BBB", "매수후보", weekly_pos="저항대아래")
    assert gen._pick_priority(watch_fresh) < gen._pick_priority(cand_worse)


# ── 홈 숫자 카드 ─────────────────────────────────────────────────────────
def test_stat_cards_have_one_buy_tile():
    snaps = [_snap("AAA", "매수후보"), _snap("BBB", "매수관찰"), _snap("CCC", "매수불가")]
    html = gen._stat_cards(entries=[1, 2, 3], snaps=snaps, alerts=[], positions=[])
    assert '<div class="stat-card__label">매수</div>' in html
    assert "매수후보" not in html and "매수관찰" not in html
    assert '<div class="stat-card__num">2</div>' in html


def test_css_defines_the_merged_badge():
    """배지 클래스가 CSS에 없으면 색 없는 배지가 나간다."""
    css = (Path(__file__).parent / "docs/stylesheets/verdict.css").read_text(encoding="utf-8")
    assert ".verdict-buy" in css
    assert ".stat-card--buy" in css
