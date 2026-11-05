"""「방식별 기록」 페이지.

2026-10-02 gen.py 에서 나눴다. 다른 sitegen 모듈은 함수를 이름째 가져오지 않고
「모듈.이름」으로 부른다(테스트가 한 곳만 바꿔 끼워도 모든 호출에 먹게).
"""
from __future__ import annotations

import json

from sitegen import common, config as cfg, strategy_comparison


def _collect_strategy_perf() -> dict:
    """data/strategy_perf.json 로드. 없거나 깨졌으면 {} (페이지는 안내문으로 그린다)."""
    try:
        return json.loads(cfg.STRATEGY_PERF_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _strat_cell(s: dict) -> tuple[str, str]:
    done = str(s.get("closed", 0))
    if s.get("open"):
        done += f" · 진행 {s['open']}"
    r = s.get("mean_r")
    return done, (f"{r:+.2f}R" if r is not None else "—")


def _cash_account_lines(a: dict) -> list[str]:
    """공개 고정 시드로 계산한 계좌. 개인 잔고·설정은 읽거나 노출하지 않는다."""
    if not a:
        return []
    lines = ["## 한 계좌로 따라갔다면", ""]
    if a["complete"]:
        lines += [f"**{a['return_pct']:+.2%}** · 순자산 {a['equity']:,.0f}원", ""]
    else:
        lines += [f"**계산 보류: 평가 못 한 보유 {a['unvalued']}건 · 기록 오류 {a['invalid']}건**", ""]
    lines += [f"{a['start']}부터 {a['seed']:,.0f}원으로 시작한 가상 계좌입니다. 실제 계좌가 아닙니다.", ""]
    if a.get("positions"):
        lines += ['??? note "지금 보유 보기"', "",
                  "    | 방식·종목 | 넣은 돈 | 지금 |", "    |---|---:|---:|"]
        for p in a["positions"]:
            value = f"{p['market_value']:,.0f}원" if p["market_value"] is not None else "미평가"
            lines.append(f"    | {common._STRAT_LABEL.get(p['strategy'], p['strategy'])} {p['ticker']} | "
                         f"{p['cost']:,.0f}원 | {value} |")
        lines.append("")
    return lines


def _money_lines(data: dict) -> list[str]:
    money = data.get("money") or {}
    if not money:
        return []
    seed = int(data.get("seed_won", 1_000_000)) // 10000
    r_won = float(data.get("r_won", 10000))
    lines = ["## 추천대로 샀다면", "",
             f"시드 {seed}만 원, 추천마다 {r_won:,.0f}원 손실까지 걸었을 때입니다. 수수료는 뺐습니다.", "",
             "| 방식 | 끝남 | 진행 중 | 합계 |", "|---|---:|---:|---:|"]
    for key in ("base", "book", "rsi"):
        m = money.get(key)
        if not m:
            continue
        # 금액은 분석 코드가 시드 상한까지 반영해 넘긴다(2026-10-16). 옛 자료에는 없어 R × 1R 로 물러선다
        closed_won = m.get("closed_won", m["closed_r"] * r_won)
        open_won = m.get("open_won", m["open_r"] * r_won)
        lines.append(f"| {common._STRAT_LABEL[key]} | {m['closed']}건 {closed_won:+,.0f}원 | "
                     f"{m['open']}건 {open_won:+,.0f}원 | **{m['total_won']:+,.0f}원** |")
    lines.append("")
    for key, m in money.items():
        if m.get("unvalued"):
            lines += [f"**{common._STRAT_LABEL[key]} 일부 제외: 평가 못 한 보유 {m['unvalued']}건**", ""]
    return lines


RECENT_ROWS = 20


def _recent_lines(data: dict) -> list[str]:
    trades = [t for t in data.get("trades") or [] if t.get("pushed")][:RECENT_ROWS]
    if not trades:
        return []
    lines = ["## 최근 추천", "", "| 날짜 | 종목 | 방식 | 결과 |", "|---|---|---|---|"]
    for t in trades:
        res = t.get("result", "")
        if t.get("pct") is not None:
            res += f" {t['pct'] * 100:+.1f}%"
        name = t["ticker"]
        if t.get("entry") is not None and t.get("stop") is not None:
            tg = " / ".join(f"{v:,.2f}" for v in (t.get("targets") or [])) or "-"
            name += f"<br>{t['entry']:,.2f} · 목표 {tg} · 손절 {t['stop']:,.2f}"
        lines.append(f"| {common._md(t['ts'])} | {name} | {common._STRAT_LABEL.get(t['strategy'], '')} | {res} |")
    lines.append("")
    return lines


def _strategies_index(data: dict, names: dict) -> str:
    """추천 기록: 금액 → 계좌 → 최근 추천. 연구 비교는 research.md 로 옮겼다 (2026-11-05 사용자 승인)."""
    lines = ["# 추천 기록", ""]
    body = _money_lines(data) + _cash_account_lines(data.get("cash_account") or {}) + _recent_lines(data)
    if not body:
        lines += ['!!! info "아직 기록이 없습니다"', "    다음 스캔 때 채워집니다.", ""]
    lines += body
    lines += ["## 더 보기", "",
              "- [과거 비교 연구](research.md)",
              "- [매도 규칙](manual-exits-2026-10-18.md)",
              "- [가상 포지션](../positions/index.md)",
              "- [분석 스냅샷](../snapshots/index.md)", "",
              f"> 기준 시각: {str(data.get('generated', ''))[:16].replace('T', ' ')}", "", common.DISCLAIMER]
    return "\n".join(lines) + "\n"


def _research_index(data: dict) -> str:
    """과거 측정·연구 비교와 방식별 기간 성적. 메뉴에는 없고 추천 기록 맨 아래에서 들어온다."""
    lines = ["# 과거 비교 연구", ""]
    lines += strategy_comparison.lines()
    periods = data.get("periods") or []
    if periods:
        active = common._STRAT_LABEL.get(data.get("active"), "스윙")
        since = str(data.get("active_since") or "")[5:16].replace("T", " ")
        lines += ["## 방식별 기간 성적", "",
                  f"지금 켜진 방식: {active} ({since}부터). 텔레그램에 「둘다」·「단타」·「스윙」, "
                  "「RSI 켜」·「RSI 꺼」, 「권총 켜」·「권총 꺼」를 보내 바꿉니다.", "",
                  "| 기간 | 구분 | 끝남 | 거래당 |", "|---|---|---:|---:|"]
        for i, p in enumerate(periods):
            both = p["strategy"] == "both"
            on = common._STRAT_LABEL["base" if both else p["strategy"]]
            off = common._STRAT_LABEL["book" if p["strategy"] in ("base", "both") else "base"]
            end = "지금" if i == len(periods) - 1 else common._md(p["end"])
            done, r = _strat_cell(p["active"])
            lines.append(f"| {common._md(p['start'])}~{end} | {on}(알림) | {done} | {r} |")
            done, r = _strat_cell(p["other"])
            lines.append(f"| | {off}({'알림' if both else '기록만'}) | {done} | {r} |")
        counts = data.get('closed_counts')
        if counts is None:
            counts = {'base': 0, 'book': 0}
            for p in periods:
                counts['base' if p['strategy'] == 'both' else p['strategy']] += p['active'].get('closed', 0)
                if p['strategy'] == 'both':
                    counts['book'] += p['other'].get('closed', 0)
        lines += ['', '방식별 완결: ' + ' · '.join(f'{common._STRAT_LABEL[k]} {v}/200건' for k, v in counts.items()), '',
                  '200건은 방식별 점검 시점이며 우월성 보장이 아닙니다. 비용 차감 계좌 수익률로 비교합니다.', '',
                  'R 은 손절 폭 대비 몇 배를 벌었는지입니다 (−1R = 손절). 거래비용은 빼지 않았습니다.', '']
    lines += ["[매도·알림 규칙과 백테스트 비교 보기](manual-exits-2026-10-18.md)", "", common.DISCLAIMER]
    return "\n".join(lines) + "\n"
