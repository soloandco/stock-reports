"""모바일 내용 정리 (2026-09-23 사용자 결정).

폰에서 종목 페이지를 열면 5월에 손으로 쓴 메모(「TT 8/8 매수 후보 1순위」, 이미 없앤
「카톡 알림」)가 지금 판정보다 먼저 보였다. 관찰 54종목 중 35종목이 그랬다.
원본 워치리스트 파일은 그대로 두고 공개 사본만 고친다.

- 맨 위에 최신 스냅샷 기준 「지금 상태」 카드
- 손으로 쓴 메모는 「지난 분석 메모」로 접는다. 카톡 알림 절은 뺀다
- 긴 안내문은 한 줄만 보이고 나머지는 「자세히」로 접는다 (「매수 신호 아님」은 보이는 줄에 남긴다)
- 관찰 목록은 종목·기업명을 한 칸으로 합쳐 폰에서 경과 칸까지 보이게 한다
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import gen

SRC = (
    "---\n"
    "type: watchlist\n"
    "ticker: GOOGL\n"
    "market: NASDAQ\n"
    "title: Alphabet 관찰 종목\n"
    "updated: 2026-05-30\n"
    "---\n"
    "\n"
    "# Alphabet (GOOGL) — 관찰 종목\n"
    "\n"
    "> 역할: 대형 기술주 관찰\n"
    "\n"
    "## 현황 요약\n"
    "\n"
    "| 항목 | 값 |\n|---|---|\n| 현재 판정 | ★ 매수 후보 1순위 |\n"
    "\n"
    "## 카톡 알림 (monitor.py 자동 설정)\n"
    "\n"
    "| 알림 | 조건 |\n|---|---|\n| 매수 | TT 8/8 |\n"
    "\n"
    "## 결과 검증 로그\n"
    "\n"
    "기록 없음\n"
)

SNAP = {"ticker": "GOOGL", "created": "2026-09-23", "verdict": "매수관찰", "reason": "",
        "stage": "2", "tt": "6", "ttmax": 7, "price": "350.0", "market": "NASDAQ",
        "days": "3", "start_unknown": "", "stop": "332.0", "weekly_pos": "저항대아래",
        "weekly_pct": "16.2", "rr": "3.2", "fname": "GOOGL-2026-09-23.md"}


def _page(tmp_path, monkeypatch, latest=None):
    src, out = tmp_path / "src", tmp_path / "out"
    src.mkdir()
    monkeypatch.setattr(gen, "SRC_WL", src)
    monkeypatch.setattr(gen, "OUT_WL", out)
    monkeypatch.setattr(gen, "SUPERINV_JSON", tmp_path / "none.json")
    (src / "GOOGL-alphabet.md").write_text(SRC, encoding="utf-8")
    gen._collect_watchlist(latest)
    return (out / "GOOGL.md").read_text(encoding="utf-8")


def test_old_memo_is_folded_and_labelled_with_its_date(tmp_path, monkeypatch):
    page = _page(tmp_path, monkeypatch, {"GOOGL": SNAP})
    assert '??? note "지난 분석 메모 (작성 2026-05-30 · 지금 판정과 다를 수 있음)"' in page
    # 메모 안 절은 접힌 상자 안으로 들어간다 (들여쓰기)
    assert "\n    ## 현황 요약" in page
    assert "\n## 현황 요약" not in page
    assert "★ 매수 후보 1순위" in page


def test_kakao_section_is_dropped(tmp_path, monkeypatch):
    page = _page(tmp_path, monkeypatch, {"GOOGL": SNAP})
    assert "카톡" not in page
    assert "결과 검증 로그" in page      # 그 뒤 절은 남는다


def test_current_status_comes_before_chart_and_memo(tmp_path, monkeypatch):
    page = _page(tmp_path, monkeypatch, {"GOOGL": SNAP})
    assert page.index('class="m-sum') < page.index("## 차트") < page.index("지난 분석 메모")
    assert "> 역할: 대형 기술주 관찰" in page      # H1 아래 머리말은 그대로
    assert page.index("역할: 대형 기술주") < page.index('class="m-sum')


def test_status_card_uses_latest_snapshot_and_links_it(tmp_path, monkeypatch):
    page = _page(tmp_path, monkeypatch, {"GOOGL": SNAP})
    status = page.split("## 차트", 1)[0]
    assert "7개 중 6개 충족" in status and ">매수<" in status
    assert "기준일 2026-09-23" in status and "신호 3일째" in status
    # 손절 · 목표(5R) · 첫 저항. 목표 = 350 + (350-332)×5 = 440
    assert "$332.00" in status and "$440.00" in status and "목표 (5R)" in status
    # 관찰 페이지는 /watchlist/GOOGL/ 에 열린다
    assert 'href="../../snapshots/GOOGL-2026-09-23/"' in status
    # 차트에 손절선을 넘긴다 (매수 상태일 때만)
    assert 'data-stop="332.0000"' in page


def test_status_card_for_non_buy_shows_reason(tmp_path, monkeypatch):
    snap = {**SNAP, "verdict": "매수불가", "reason": "과열", "days": ""}
    page = _page(tmp_path, monkeypatch, {"GOOGL": snap})
    status = page.split("## 차트", 1)[0]
    assert "매수불가" in status and "과열" in status and "RSI가 90" in status
    assert "목표" not in status and "data-stop" not in page


def test_no_snapshot_means_no_status_section(tmp_path, monkeypatch):
    page = _page(tmp_path, monkeypatch, None)
    assert "m-sum" not in page
    assert "## 차트" in page and "지난 분석 메모" in page


def test_file_without_h2_is_left_alone(tmp_path, monkeypatch):
    src, out = tmp_path / "src", tmp_path / "out"
    src.mkdir()
    monkeypatch.setattr(gen, "SRC_WL", src)
    monkeypatch.setattr(gen, "OUT_WL", out)
    monkeypatch.setattr(gen, "SUPERINV_JSON", tmp_path / "none.json")
    (src / "X.md").write_text("---\ntype: watchlist\nticker: X\n---\n# X\n본문만\n", encoding="utf-8")
    gen._collect_watchlist()
    page = (out / "X.md").read_text(encoding="utf-8")
    assert "지난 분석 메모" not in page and "본문만" in page and "## 차트" in page


def test_chart_note_shows_one_line_and_folds_the_rest():
    block = gen._CHART_BLOCK
    summary = block.split("<summary>", 1)[1].split("</summary>", 1)[0]
    assert "무작위 선과 같았습니다" in summary and "매수 신호 아님" in summary
    assert "<details" in block and "층화 차이" in block.split("</summary>", 1)[1]


def test_13f_note_keeps_not_a_signal_visible():
    data = {"period": "2026-06-30", "tickers": {"MSFT": {"famous": [], "famous_holders": 0}}}
    b = gen._superinvestor_block("MSFT", data)
    summary = b.split("<summary>", 1)[1].split("</summary>", 1)[0]
    assert "매수 신호가 아닙니다" in summary
    assert "Dataroma" in b.split("</summary>", 1)[1]


def test_watchlist_is_card_rows_with_chips_not_table():
    entries = [("GS", "NYSE", "골드만삭스", "GS.md"), ("AMD", "NASDAQ", "AMD Inc", "AMD.md"),
               ("X", "NYSE", "엑스", "X.md")]
    latest = {"GS": {"verdict": "매수관찰", "reason": "", "stage": "2", "tt": "6",
                     "ttmax": 7, "price": "1074.51", "days": "2"},
              "AMD": {"verdict": "매수불가", "reason": "과열", "stage": "2", "tt": "7",
                      "ttmax": 7, "price": "623.77", "days": ""}}
    md = gen._watchlist_index(entries, latest)
    assert "| 종목 |" not in md                     # 표가 아니다
    assert 'href="GS/"' in md and "골드만삭스" in md and "2일째" in md
    assert "과열" in md and "분석 전" in md          # 스냅샷 없는 종목
    assert "전체 3</button>" in md and "매수 1</button>" in md and "매수불가 1</button>" in md
    # 매수가 매수불가보다 먼저, 새 신호 묶음 제목이 붙는다
    assert md.index('href="GS/"') < md.index('href="AMD/"') < md.index('href="X/"')
    assert "새 신호 <b>1</b>" in md
    assert '??? info' in md and "5일째까지만 유효" in md


def test_site_url_is_set_so_404_page_keeps_styles():
    import yaml
    cfg = yaml.safe_load((Path(__file__).parent / "mkdocs.yml").read_text(encoding="utf-8"))
    assert cfg["site_url"] == "https://soloandco.github.io/stock-reports/"
