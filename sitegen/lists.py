"""스냅샷·노트·가상 포지션·알림 목록 페이지.

2026-10-02 gen.py 에서 나눴다. 다른 sitegen 모듈은 함수를 이름째 가져오지 않고
「모듈.이름」으로 부른다(테스트가 한 곳만 바꿔 끼워도 모든 호출에 먹게).
"""
from __future__ import annotations

import json
import shutil

from sitegen import common, config as cfg


SNAP_FILTERS = """\
<div class="snap-filters">
<label class="sf-label" for="sf-verdict">판정</label>
<select class="sf-select" id="sf-verdict" data-f="verdict">
<option value="">전체</option>
<option value="buy">매수</option>
<option value="nobuy">매수불가</option>
</select>
<label class="sf-label" for="sf-stage">Stage</label>
<select class="sf-select" id="sf-stage" data-f="stage">
<option value="">전체</option>
<option value="1">1</option>
<option value="2">2</option>
<option value="3">3</option>
<option value="4">4</option>
</select>
</div>
"""


def _collect_snapshots() -> list[dict]:
    """스냅샷 복사 + 메타 dict 리스트 반환.

    _reset_dir 대신 증분 복사 — 이미 있는 파일은 유지하고 새/변경 파일만 덮어씀.
    reset하면 auto-deploy 타이밍에 따라 일부 파일이 누락·삭제될 수 있음.
    """
    cfg.OUT_SNAP.mkdir(parents=True, exist_ok=True)
    snaps = []
    for md in sorted(cfg.SRC_SNAP.glob("*.md")):
        fm = common._frontmatter(md.read_text(encoding="utf-8"))
        shutil.copy(md, cfg.OUT_SNAP / md.name)
        snaps.append({
            "ticker":  fm.get("ticker", md.stem),
            "created": fm.get("created", ""),
            "verdict": fm.get("verdict", ""),
            "reason":  fm.get("verdict-reason", ""),
            "stage":   fm.get("stage", ""),
            "tt":      fm.get("trend-template-score", ""),
            # 점수 분모. 2026-09-10 에 조건 4 를 빼면서 7 이 됐다.
            # 이 줄이 없는 과거 스냅샷은 8조건 시절이므로 8 로 읽는다 —
            # 기본값을 7 로 두면 옛 기록이 소급으로 틀린 분모를 갖는다.
            "ttmax":   fm.get("tt-max", 8),
            "price":   fm.get("price", ""),
            "market":  fm.get("market", ""),
            "days":    fm.get("candidate-days", ""),   # 매수 상태 경과 거래일 (구형 스냅샷은 "")
            "start_unknown": fm.get("candidate-start-unknown", ""),  # 등록 전부터 매수 상태
            "gap":     fm.get("sma50-gap-pct", ""),    # SMA50 이격 %
            # 홈 「오늘의 결론」 카드용 (2026-09-03) — 값이 없는 구형 스냅샷은 ""
            "stop":       fm.get("stop-price", ""),
            "weekly_pos": fm.get("weekly-position", ""),
            "weekly_pct": fm.get("weekly-overhead-pct", ""),
            "rr":         fm.get("real-rr", ""),
            # 관찰 페이지 결론 카드용 (2026-09-23)
            "since":      fm.get("candidate-since", ""),
            "wprice":     fm.get("weekly-overhead-price", ""),
            "fname":   md.name,
        })
    # 분석일 내림차순(동일 날짜는 종목 오름차순 — 안정 정렬)
    snaps.sort(key=lambda s: s["ticker"])
    snaps.sort(key=lambda s: s["created"], reverse=True)
    return snaps


def _collect_notes() -> list[dict]:
    """docs/notes/*.md 중 type=trade-note만 복사 + 메타 dict 리스트 반환.

    entry_date 내림차순. 템플릿(type 없음)은 건너뛴다. 알림 디렉터리와 같은
    이유로 reset 없이 증분 복사 — 청산 전 노트가 배포 타이밍에 유실되면 안 됨.
    """
    cfg.OUT_NOTES.mkdir(parents=True, exist_ok=True)
    notes = []
    for md in sorted(cfg.SRC_NOTES.glob("*.md")):
        fm = common._frontmatter(md.read_text(encoding="utf-8"))
        if fm.get("type") != "trade-note":
            continue
        shutil.copy(md, cfg.OUT_NOTES / md.name)
        notes.append({
            "ticker":     fm.get("ticker", md.stem),
            "name":       fm.get("name", ""),
            "entry_date": fm.get("entry_date", ""),
            "status":     fm.get("status", "open"),
            "exit_date":  fm.get("exit_date", ""),
            "r_multiple": fm.get("r_multiple", ""),
            "outcome":    fm.get("outcome", ""),
            "fname":      md.name,
        })
    notes.sort(key=lambda n: n["entry_date"], reverse=True)
    return notes


def _monthly_stats(notes: list[dict]) -> list[dict]:
    """청산된 노트를 exit_date의 YYYY-MM으로 그룹핑해 승률·평균R·합계R 계산.

    합계 R은 단리 합산(동시 포지션 가능성 때문에 복리 계산은 부정확).
    월 내림차순 정렬.
    """
    by_month: dict[str, list[dict]] = {}
    for n in notes:
        if n.get("status") != "closed" or not n.get("exit_date"):
            continue
        month = n["exit_date"][:7]
        by_month.setdefault(month, []).append(n)

    stats = []
    for month, group in by_month.items():
        count = len(group)
        wins = sum(1 for n in group if n.get("outcome") == "win")
        r_values = [float(n["r_multiple"]) for n in group if n.get("r_multiple")]
        stats.append({
            "month":    month,
            "count":    count,
            "win_rate": (wins / count * 100) if count else 0.0,
            "avg_r":    (sum(r_values) / len(r_values)) if r_values else 0.0,
            "sum_r":    sum(r_values),
        })
    stats.sort(key=lambda s: s["month"], reverse=True)
    return stats


def _latest_per_ticker(snaps: list[dict]) -> list[dict]:
    """종목당 최신 스냅샷 1건만 반환.

    snaps은 날짜 내림차순 정렬 상태여야 한다 (_collect_snapshots 반환값).
    파일은 모두 복사되므로 히스토리 URL은 그대로 유지된다.
    """
    seen: set[str] = set()
    result = []
    for s in snaps:
        if s["ticker"] not in seen:
            seen.add(s["ticker"])
            result.append(s)
    return result


def _collect_positions() -> list[dict]:
    """현재 열린 매수 포지션을 core.positions로 복원해 dict 리스트로 반환.

    진입가 = 첫 매수전환 스냅샷가, 현재가 = 최신 스냅샷가(라이브 fetch 없음).
    core 미탑재(스냅샷 없음 등)면 빈 리스트. 렌더러는 plain dict만 받아 테스트 가능.
    """
    import sys
    if str(cfg.ROOT.parent) not in sys.path:
        sys.path.insert(0, str(cfg.ROOT.parent))
    try:
        from core.outcome import load_snapshot_series
        from core.positions import build_open_positions
        from core.scanner import _latest_snapshot_path
    except ImportError:
        return []

    snaps_by_ticker, market_by_ticker = load_snapshot_series(cfg.SRC_SNAP)
    positions = build_open_positions(snaps_by_ticker, market_by_ticker)
    return [{
        "ticker":        p.ticker,
        "market":        p.market,
        "verdict":       p.verdict,
        "entry_date":    p.entry_date.isoformat(),
        "current_date":  p.current_date.isoformat(),
        "snapshot_file": _latest_snapshot_path(p.ticker, cfg.SRC_SNAP).name,
        "entry_price":   p.entry_price,
        "stop_price":    p.stop_price,
        "current_price": p.current_price,
        "return_pct":    p.return_pct,
        "r_multiple":    p.r_multiple,
        "to_stop_pct":   p.to_stop_pct,
        "to_target_pct": p.to_target_pct,
        "days_held":     p.days_held,
        "days_held_basis": p.days_held_basis,
    } for p in positions]


def _scan_alerts() -> list[dict]:
    """alerts/ 의 알림 페이지(uid.md) 메타를 최신순으로 반환. (삭제하지 않음)"""
    cfg.OUT_ALERT.mkdir(parents=True, exist_ok=True)
    alerts = []
    for md in cfg.OUT_ALERT.glob("*.md"):
        if md.name == "index.md":
            continue
        fm = common._frontmatter(md.read_text(encoding="utf-8"))
        alerts.append({
            "created": fm.get("created", ""),
            "ticker":  fm.get("ticker", md.stem),
            "alert":   fm.get("alert", fm.get("title", "")),
            "fname":   md.name,
        })
    alerts.sort(key=lambda a: a["created"], reverse=True)
    return alerts


def _snapshots_index(snaps, names) -> str:
    lines = [
        "# 분석 스냅샷",
        "",
        "특정 시점의 **판정 기록**(최신순). 판정 어휘 — "
        "**매수**(Stage 2 + TT 5/7 이상) · "
        "**매수불가**(사유: 과열·시장국면·변동성과대·하락국면·천장권·기준미달).",
        "",
        SNAP_FILTERS,
        # 관찰 종목과 같은 원칙 — 판정을 앞으로, 분석일은 뒤로 (2026-07-19)
        "| 종목 | 기업명 | 판정 | Stage | TT | 분석일 |",
        "|------|--------|------|-------|----|--------|",
    ]
    for s in snaps:
        name = names.get(s['ticker'], '')
        lines.append(
            f"| [{s['ticker']}]({s['fname']}) | [{name}]({s['fname']}) "
            f"| {common._verdict_cell(s['verdict'], s['reason'])} "
            f"| {s['stage']} | {s['tt']}/{s.get('ttmax', 8)} | {s['created']} |"
        )
    return "\n".join(lines) + "\n"


def _alerts_index(alerts, names) -> str:
    lines = [
        "# 알림",
        "",
        "관찰 종목이 임계선을 넘은 **순간**에 자동 기록되는 이벤트(최신순). "
        "유형 — 📈 매수신호 · 👀 매수근접 · 📉 매도신호 · 🚨 손절경고.",
        "",
    ]
    if not alerts:
        lines += [
            '!!! info "아직 발생한 알림이 없습니다"',
            "    관찰 종목이 매수·매도·손절 조건을 충족하면 이곳에 자동으로 기록됩니다.",
        ]
        return "\n".join(lines) + "\n"
    lines += ["| 발생일 | 종목 | 기업명 | 유형 |", "|--------|------|--------|------|"]
    for a in alerts:
        lines.append(f"| {a['created']} | [{a['ticker']}]({a['fname']}) | [{names.get(a['ticker'], '')}]({a['fname']}) | {a['alert']} |")
    return "\n".join(lines) + "\n"


_SEED_PANEL = """\
<div class="seed-panel">
<label>시드 (원): <input type="number" id="seed-input" min="0" step="100000" placeholder="예: 10000000"></label>
&nbsp;&nbsp;<label>트레이드당 리스크: <input type="number" id="risk-input" min="0.1" step="0.1" value="1" style="width:4.5em"> %</label>
<p class="seed-hint">💡 시드를 입력하면 종목별 <b>주수·손익(원)</b>과 아래 <b>포트폴리오 요약</b>이 계산됩니다. 시드는 이 브라우저에만 저장되며 서버·공개 저장소에 올라가지 않습니다.</p>
<div id="seed-summary"></div>
</div>
"""


def _positions_index(positions: list[dict], names: dict) -> str:
    """열린 매수 포지션의 진입가 대비 현재 수익률·R 표(진입 R-배수 내림차순)."""
    lines = [
        "# 가상 포지션",
        "",
        '!!! info "알림 기준 성적은 방식별 기록에 있습니다"',
        "    이 페이지는 과거 **판정 기록**에서 매수 전환을 다시 만든 가상 포지션입니다. 알림이 나가지 않은 전환도 "
        "들어가서 건수가 [방식별 기록](../strategies/index.md)보다 많습니다. 실제로 알림이 나간 추천의 "
        "추천가·목표가·손절가와 「추천대로 했다면」 금액은 방식별 기록에서 보세요.",
        "",
        "현재 **매수** 판정인 종목의 진입가 대비 현재 수익률·R-배수. "
        "진입가 = 비매수→매수로 전환된 **첫 스냅샷 가격**, 현재가 = **최신 스냅샷 가격**입니다.",
        "",
        '!!! warning "가정된 진입 (실제 체결 아님)"',
        "    진입가는 판정이 매수로 바뀐 시점의 분석용 스냅샷 가격이며, 실제 매매 체결가가 "
        "아닙니다. R-배수·수익률은 그 가정 진입가 기준의 참고 수치입니다.",
        "",
        '??? info "📘 R이 뭔가요? (수익률 %와 뭐가 다른가요)"',
        "    **R = 이 매매에서 각오한 손실폭(진입가→손절가)을 1로 봤을 때, 지금 얼마나 벌었나**를 나타내는 숫자입니다.",
        "",
        "    - **1R** = 진입가 − 손절가 (각오한 최대 손실폭)",
        "    - **R배수** = 지금 이익 ÷ 1R",
        "",
        "    예시 — $100에 사서 손절을 $90에 뒀다면 1R = $10.",
        "    현재가 $110이면 이익 $10 → **+1.0R** (각오한 손실만큼 벌었다는 뜻). "
        "현재가가 $90까지 내려가 손절되면 **−1.0R**.",
        "",
        "    **왜 수익률 %만으로는 부족한가?** 종목마다 손절폭이 다르기 때문입니다. "
        "+6% 올라도 손절이 −25% 멀리 있으면 +0.2R에 불과하고, +4%라도 손절이 −9%로 가까우면 +0.8R입니다. "
        "**R은 '감수한 위험 대비' 성과라, 종목이 달라도 같은 잣대로 비교**할 수 있습니다.",
        "",
        "    | R 값 | 의미 |",
        "    |------|------|",
        f"    | **+{common.REWARD_RATIO:g}R** | 목표 도달 ({common.REWARD_RATIO:g}:1 리워드) |",
        "    | **+1.5R** | 손절선을 본전으로 올릴 때 |",
        "    | **+1R** | 각오한 위험만큼 벌었다 |",
        "    | **0R** | 본전 |",
        "    | **−1R** | 손절 도달 (청산) |",
        "",
    ]
    if not positions:
        lines += [
            '!!! info "열린 포지션 없음"',
            "    현재 매수 판정인 종목이 없습니다. "
            "`python monitor.py --scan` 으로 스냅샷을 갱신하세요.",
        ]
        return "\n".join(lines) + "\n"

    rows = sorted(positions, key=lambda p: p["r_multiple"], reverse=True)
    lines += [
        _SEED_PANEL,
        "",
        "| 종목 | 판정 | 진입일 | 진입가 | 현재가 | 수익률 | R | 손절까지 | 타겟까지 | 보유 | 주수 | 손익(원) |",
        "|------|------|--------|--------|--------|--------|---|---------|---------|------|------|---------|",
    ]
    for p in rows:
        t = p["ticker"]
        name = names.get(t, "")
        snapshot_file = p.get("snapshot_file") or f"{t}-{p['current_date']}.md"
        link = f"../snapshots/{snapshot_file}"
        dot = "🟢" if p["r_multiple"] > 0 else ("🔴" if p["r_multiple"] < 0 else "⚪")
        duration = f"{p['days_held']}일"
        if p.get("days_held_basis") == "observation":
            duration = f"관측 {duration}"
        lines.append(
            f"| [**{t}**]({link}) {name} | {common._verdict_cell(p['verdict'], '')} "
            f"| {p['entry_date'][5:]} "
            f"| {common._fmt_price(p['market'], p['entry_price'])} "
            f"| {common._fmt_price(p['market'], p['current_price'])} "
            f"| {dot} {p['return_pct']:+.1f}% "
            f"| {p['r_multiple']:+.1f}R "
            f"| {p['to_stop_pct']:+.1f}% "
            f"| {p['to_target_pct']:+.1f}% "
            f"| {duration} "
            f'| <span class="js-shares" data-ticker="{t}">—</span> '
            f'| <span class="js-pnl" data-ticker="{t}">—</span> |'
        )

    n = len(rows)
    avg_r = sum(p["r_multiple"] for p in rows) / n
    wins = sum(1 for p in rows if p["r_multiple"] > 0)
    pos_data = [{"ticker": p["ticker"], "entry": p["entry_price"],
                 "stop": p["stop_price"], "current": p["current_price"],
                 "r": p["r_multiple"]} for p in rows]
    lines += [
        "",
        f"**합계** {n}포지션 · 평균 {avg_r:+.1f}R · 양의 R {wins}/{n}",
        "",
        '<script type="application/json" id="pos-data">',
        json.dumps(pos_data, ensure_ascii=False),
        "</script>",
        "",
        common.DISCLAIMER,
    ]
    return "\n".join(lines) + "\n"
