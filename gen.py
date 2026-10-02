"""워치리스트·스냅샷·알림을 MkDocs 사이트 docs/로 변환·생성.

소스(메인 저장소):
  ../docs/watchlist/*.md            관찰 종목 (type=watchlist)
  ../docs/watchlist/snapshots/*.md  분석 스냅샷

출력(이 저장소 docs/):
  index.md            홈 포털 (바로 가기 + 용어 설명)
  watchlist/index.md  관찰 종목 목록  + 종목 상세 페이지 복사본
  snapshots/index.md  분석 스냅샷 목록 + 스냅샷 상세 페이지 복사본
  alerts/index.md     알림 타임라인 (이벤트 기록)

알림 상세(alerts/{uid}.md)는 monitor.py가 직접 push하므로 이 스크립트는
**삭제하지 않고** 인덱스만 다시 만든다. (과거 _reset_dir(OUT)가 alerts/를
통째로 지우던 버그를 회피 — 워치리스트/스냅샷 디렉터리만 재생성한다.)

판정 어휘·메뉴 구조 설명: ../docs/verdict-taxonomy.md
"""
from __future__ import annotations

import importlib
import sys
import types
from pathlib import Path

# 파일 경로로 직접 불러와도(tests/test_gen_home.py) 옆의 sitegen 을 찾게 한다
_HERE = str(Path(__file__).resolve().parent)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from sitegen import config as cfg, home, lists, market_page, strategies, watch_pages  # noqa: E402

# ── 옛 이름 안내 (2026-10-02 분할) ──────────────────────────────
# 본체는 sitegen/ 패키지로 옮겼다. `gen.X` 를 읽으면 X 가 지금 있는 모듈에서 그 순간의 값을
# 가져온다. `gen.X` 를 바꿔 끼우려 하면 오류를 낸다. 여기 바꿔 봐야 부르는 쪽엔 안 먹어서
# 테스트가 실제 사이트 원고(docs/)에 쓰게 된다(2026-08-09 공개 저장소 작업트리 오염과 같은 구조).
_HOMES_BY_MODULE = {
    "sitegen.common": (
        "CANDIDATE_FRESH_MAX_DAYS", "DISCLAIMER", "MAX_HOLD_DAYS", "REWARD_RATIO", "_BUY_DISPLAY",
        "_BUY_STATES", "_STRAT_LABEL", "_VERDICT_KIND", "_VERDICT_ORDER", "_candidate_days_cell",
        "_company_name", "_display_verdict", "_fmt_price", "_fmt_price_str", "_frontmatter",
        "_is_expired", "_md", "_num", "_pct_text", "_reset_dir", "_signal_label", "_truthy",
        "_verdict_cell",
    ),
    "sitegen.config": (
        "FEAR_INDEX_JSON", "OUT", "OUT_ALERT", "OUT_NOTES", "OUT_POS", "OUT_SNAP", "OUT_STRAT",
        "OUT_WL", "OUT_WL_CHARTS", "ROOT", "SECTOR_JSON", "SRC_NOTES", "SRC_SNAP", "SRC_WL",
        "STRATEGY_PERF_JSON", "SUPERINV_JSON", "TRADE_REPORT_JSON", "VALUATION_JSON",
    ),
    "sitegen.home": (
        "HOME_NEW_ROWS", "NEAR_RESIST_PCT", "PICK_MAX_CARDS", "_PICK_WEEKLY_RANK", "_WEEKDAY_KO",
        "_alert_name", "_basis_label", "_conclusion_section", "_dashboard", "_first_resist",
        "_fresh_card", "_load_fear_index", "_market_line", "_pick_priority", "_recent_alerts",
        "_sec_title", "_stop_pct", "_strategy_box", "_superinvestor_home",
    ),
    "sitegen.lists": (
        "SNAP_FILTERS", "_SEED_PANEL", "_alerts_index", "_collect_notes", "_collect_positions",
        "_collect_snapshots", "_latest_per_ticker", "_monthly_stats", "_positions_index",
        "_scan_alerts", "_snapshots_index",
    ),
    "sitegen.market_page": (
        "_REGIME_ENTRY", "_REGIME_KO", "_SIGNAL_EMOJI", "_TV_HEATMAP", "_fear_index_page",
        "_load_sector_flow", "_load_trade_report", "_rank_table", "_sector_flow_section",
        "_theme_flow_section", "_trade_report_section",
    ),
    "sitegen.strategies": (
        "_collect_strategy_perf", "_strat_cell", "_strategies_index",
    ),
    "sitegen.watch_pages": (
        "SUPERINV_FIRST", "SUPERINV_ROWS", "VAL_EVIDENCE", "_CHART_BLOCK", "_KAKAO_SECTION_RE",
        "_PRIVATE_BLOCK_RE", "_PRIVATE_FM_KEYS", "_REASON_KO", "_SELL_KO", "_STAGE_KO",
        "_VAL_CHEAP", "_VAL_DEAR", "_WL_GROUPS", "_WL_GROUP_OF", "_chart_attrs", "_checks",
        "_collect_watchlist", "_cost_cell", "_fold_old_memo", "_load_superinvestors",
        "_load_valuation", "_sanitize_public_md", "_split_at_first_h2", "_status_section",
        "_superinvestor_block", "_usd", "_valuation_block", "_watchlist_index", "_wl_sub",
        "_write_chart_data",
    ),
}
_HOMES = {n: m for m, ns in _HOMES_BY_MODULE.items() for n in ns}


def __getattr__(name: str):
    mod = _HOMES.get(name)
    if mod is None:
        raise AttributeError(f"module 'gen' has no attribute {name!r}")
    return getattr(importlib.import_module(mod), name)


class _Facade(types.ModuleType):
    def __setattr__(self, name, value):
        if name in _HOMES:
            raise AttributeError(
                f"gen.{name} 는 바꿔 끼울 수 없다. {_HOMES[name]}.{name} 을 바꿀 것 "
                f"(gen 은 실행 입구일 뿐이라 여기 바꾸면 부르는 쪽에 안 먹는다)")
        if not name.startswith("__") and name not in self.__dict__:
            raise AttributeError(f"gen 에 {name} 이 없다. 새로 만들어 끼워도 부르는 쪽에 안 먹는다")
        super().__setattr__(name, value)


# 파일 경로로 직접 불러오면 sys.modules 에 없다. 그때는 안내 장치 없이 읽기만 된다
if __name__ in sys.modules:
    sys.modules[__name__].__class__ = _Facade


def main():
    cfg.OUT.mkdir(parents=True, exist_ok=True)

    snaps   = lists._collect_snapshots()          # 전체 히스토리 (파일 복사 완료)
    latest  = lists._latest_per_ticker(snaps)     # 인덱스·대시보드용: 종목당 최신 1건
    # 관찰 페이지 맨 위 「지금 상태」 카드가 최신 스냅샷을 쓴다 (2026-09-23)
    entries = watch_pages._collect_watchlist({s["ticker"]: s for s in latest})
    alerts  = lists._scan_alerts()
    positions = lists._collect_positions()        # 현재 열린 매수 포지션
    names   = {ticker: name for ticker, _market, name, _fname in entries}
    # 워치리스트에서 뺀 종목의 옛 스냅샷은 목록·대시보드에서 제외한다 (2026-08-23).
    # 파일은 그대로 복사되므로 히스토리 URL과 백테스트 원자료는 보존된다.
    # 계기: 6월에 정리한 7종목(BMNR·CEG 등)이 최신 목록 사이에 6월 날짜로 남아
    # "스냅샷 갱신이 멈췄다"는 오해를 불렀다.
    retired = [s["ticker"] for s in latest if s["ticker"] not in names]
    latest  = [s for s in latest if s["ticker"] in names]

    cfg.OUT_POS.mkdir(parents=True, exist_ok=True)
    (cfg.OUT / "index.md").write_text(home._dashboard(entries, latest, alerts, names, positions), encoding="utf-8")
    kr_watched = any(m in ("KRX", "KOSDAQ") for _t, m, _n, _f in entries)
    (cfg.OUT / "fear-index.md").write_text(market_page._fear_index_page(latest, names, show_kr=kr_watched),
                                       encoding="utf-8")
    latest_map = {s["ticker"]: s for s in latest}
    (cfg.OUT_WL / "index.md").write_text(watch_pages._watchlist_index(entries, latest_map), encoding="utf-8")
    # _collect_watchlist가 OUT_WL을 통째로 교체하므로 반드시 그 뒤에 쓴다
    charted = watch_pages._write_chart_data(entries)
    (cfg.OUT_SNAP / "index.md").write_text(lists._snapshots_index(latest, names), encoding="utf-8")
    (cfg.OUT_ALERT / "index.md").write_text(lists._alerts_index(alerts, names), encoding="utf-8")
    (cfg.OUT_POS / "index.md").write_text(lists._positions_index(positions, names), encoding="utf-8")
    cfg.OUT_STRAT.mkdir(parents=True, exist_ok=True)
    (cfg.OUT_STRAT / "index.md").write_text(
        strategies._strategies_index(strategies._collect_strategy_perf(), names), encoding="utf-8")

    print(f"생성 완료: 관찰 {len(entries)}개 · 스냅샷 {len(latest)}종목({len(snaps)}건, "
          f"목록 제외 {len(retired)}종목) "
          f"· 알림 {len(alerts)}건 · 가상 포지션 {len(positions)}개 "
          f" · 차트 {charted}/{len(entries)}종목")


if __name__ == "__main__":
    main()
