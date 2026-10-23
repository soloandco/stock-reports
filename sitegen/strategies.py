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
    lines = ["## 현금 제약 모의계좌", "",
             "**실제 체결 계좌 수익률이 아닙니다.** 알림이 나간 미국 추천을 한 계좌에서 따라간 모의 결과입니다.",
             f"{a['start']}부터 기준자금 {a['seed']:,.0f}원으로 시작하며, 이전 보유분은 제외합니다.", ""]
    if a["complete"]:
        lines += [f"**계좌 수익률 {a['return_pct']:+.2%} · 순자산 {a['equity']:,.0f}원**", ""]
    else:
        lines += [f"**수익률 산출 보류: 미평가 {a['unvalued']}건 · 기록 오류 {a['invalid']}건**", "",
                  "미평가 자산을 0원이나 원금으로 간주하지 않습니다.", ""]
    lines += ["| 현금 | 보유 평가금액 | 납부 비용 | 미청산 매도비용 |", "|---:|---:|---:|---:|",
              f"| {a['cash']:,.0f}원 | {a['market_value']:,.0f}원{' (부분)' if a['unvalued'] else ''} | "
              f"{a['fees_paid']:,.0f}원 | {a['exit_cost_reserve']:,.0f}원 |", "",
              f"진입 {a['taken']}건 · 완료 {a['closed']}건 · 보유 {a['open']}건 · "
              f"잔액 부족으로 축소 {a['reduced']}건 · 자금 부족 제외 {a['skipped_cash']}건", "",
              f"스윙·단타·RSI가 현금을 공유합니다. 초기자금의 {a['risk_pct']:.1%}를 손절 위험으로 배정하고, "
              "부족하면 남은 현금만큼 줄입니다. 차입은 없으며 매도대금은 원장에 기록된 시각 이후 재사용합니다.", "",
              f"편도 {a['side_cost']:.2%} 비용을 가정합니다. 순자산은 현금과 보유 평가금액의 합에서 미청산 매도비용을 뺀 값입니다.",
              "이전 기록은 환율 고정 환산·소수점 배분·알림가/규칙 청산가 기준입니다. "
              "새 체결 모형의 기록은 지연 후 모의 체결가를 사용합니다. 실제 체결가·환율 변동·세금·배당·입출금은 미반영입니다.", "",
              "**실체결 계좌 수익률: 산출 보류.** 확인된 체결 수량·가격, 시작 잔고, 입출금 자료가 필요합니다.", ""]
    if a.get("positions"):
        lines += ["### 모의계좌 보유", "", "| 방식·종목 | 투입 원금·비용 | 평가금액 | 가격 기준봉 |", "|---|---:|---:|---|"]
        for p in a["positions"]:
            value = f"{p['market_value']:,.0f}원" if p["market_value"] is not None else "미평가"
            day = (p.get("quote") or {}).get("bar_date") or "미상"
            lines.append(f"| {common._STRAT_LABEL.get(p['strategy'], p['strategy'])} {p['ticker']} | "
                         f"{p['cost']:,.0f}원 | {value} | {day} |")
        lines.append("")
    return lines


def _strategies_index(data: dict, names: dict) -> str:
    """스윙·단타 두 방식의 켜져 있던 기간별 성적과 최근 거래. 모바일 4열 이하."""
    lines = [
        "# 방식별 기록",
        "",
        "## 매도 처리 업데이트 · 2026-10-18",
        "",
        "**기존 손절·익절·보유기간 조건을 유지합니다.** 비교한 대안은 적용하지 않았습니다.",
        "",
        "미국 종목은 매도 알림과 모의 체결을 분리합니다. 알림 발송 후 30분이 지난 첫 확인 가능한 "
        "정규장 시간봉 시가에 비용을 반영합니다. 알림만으로 잔고나 확정 손익을 바꾸지 않습니다.",
        "",
        "단타 진입 손익비는 **비용 차감 후 1차 목표 이익 / 하드스톱 손실 ≥ 2**로 통일합니다.",
        "",
        "[매도·알림 규칙과 백테스트 비교 보기](manual-exits-2026-10-18.md)",
        "",
        "비교 결과는 가격 오류 후보를 사후 제외한 조건부 모의 결과입니다. 실제 계좌 실적이 아닙니다. "
        "아래 누적 기록에는 이전 처리 방식의 거래가 포함되며 소급 재계산하지 않았습니다.",
        "",
        "스윙(일봉)과 단타(1시간봉) 두 방식을 섞지 않고 따로 기록합니다. **켜진 방식만 알림이 나가고**, "
        "꺼진 방식은 같은 기간에 무엇을 했을지 기록만 합니다. 「둘 다」가 켜진 기간에는 두 방식 모두 알림이 "
        "나갑니다. 텔레그램에 「둘다」·「단타」·「스윙」을 보내 바꿉니다.",
        "",
    ]
    # RSI 반등 방식 (2026-10-10): 스윙·단타 전환과 무관하게 따로 켜고 끈다. 기록이 있거나 켜져 있을 때만 적는다
    if data.get("rsi_on") or (data.get("money") or {}).get("rsi"):
        lines += ["**RSI 방식**(일봉 RSI 가 30 아래에서 꺾여 올라오면 알림)은 위 두 방식과 따로 돕니다. "
                  f"지금 {'켜져' if data.get('rsi_on') else '꺼져'} 있습니다. "
                  "텔레그램에 「RSI 켜」·「RSI 꺼」를 보내 바꿉니다. 기간별 성적 표에는 넣지 않고 "
                  "아래 「추천대로 했다면」과 「최근 추천」에 함께 적습니다.", ""]
    lines[2:2] = strategy_comparison.lines()
    lines += _cash_account_lines(data.get("cash_account") or {})
    periods = data.get("periods") or []
    if not periods:
        lines += ['!!! info "아직 기록이 없습니다"',
                  "    다음 스캔 때 채워집니다.", "", common.DISCLAIMER]
        return "\n".join(lines) + "\n"
    active = common._STRAT_LABEL.get(data.get("active"), "스윙")
    since = str(data.get("active_since") or "")[5:16].replace("T", " ")
    lines += [f"**지금 켜진 방식: {active}** ({since}부터)", "", "## 기간별 성적", "",
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
    lines += ['', '방식별 완결: ' + ' · '.join(f'{common._STRAT_LABEL[k]} {v}/200건' for k,v in counts.items()), '',
              '200건은 방식별 점검 시점이며 우월성 보장이 아닙니다. 비용 차감 계좌 수익률로 비교합니다.', '']
    if any(v < 200 for v in counts.values()):
        lines += ['**표본 부족: 서로 다른 방식의 거래 수를 합치지 않습니다.**', '']
    money = data.get("money") or {}
    if money:
        seed = int(data.get("seed_won", 1_000_000)) // 10000
        r_won = float(data.get("r_won", 10000))
        lines += ["## 추천대로 했다면", "",
                  "이 표는 추천별 독립 손익의 합입니다. 동시 보유 자금 제약과 거래비용이 없어 계좌 수익률로 읽으면 안 됩니다.", "",
                  f"사지 않았어도 **알림이 나간 추천을 그대로 따랐을 때**의 결과입니다. "
                  f"시드 {seed}만 원에서 추천마다 {r_won:,.0f}원(시드 1%)을 손절 위험으로 건 경우로 환산합니다. "
                  "손절폭이 좁아 시드보다 많이 사야 하는 추천은 알림의 권장 주수처럼 시드만큼만 산 것으로 셉니다. "
                  "진행 중인 추천은 지금 가격으로 평가합니다.", "",
                  "| 방식 | 끝난 추천 | 진행 중 | 합계 |", "|---|---:|---:|---:|"]
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
                lines += [f"**{common._STRAT_LABEL[key]} 부분 집계: 미평가 {m['unvalued']}건. "
                          "해당 보유분의 손익은 합계에서 빠져 있습니다.**", ""]
    trades = data.get("trades") or []
    if trades:
        lines += ["## 최근 추천", "", "| 추천 | 종목 · 추천가 | 방식 | 결과 |", "|---|---|---|---|"]
        for t in trades:
            how = common._STRAT_LABEL.get(t["strategy"], "") + ("" if t.get("pushed") else " · 기록만")
            res = t.get("result", "")
            if t.get("r") is not None:
                res += f" {t['r']:+.2f}R"
                if t.get("pct") is not None:
                    res += f" ({t['pct'] * 100:+.1f}%)"
            name = t["ticker"]
            if t.get("entry") is not None and t.get("stop") is not None:
                tg = " / ".join(f"{v:,.2f}" for v in (t.get("targets") or [])) or "-"
                name += f"<br>{t['entry']:,.2f} · 목표 {tg} · 손절 {t['stop']:,.2f}"
            lines.append(f"| {common._md(t['ts'])} | {name} | {how} | {res} |")
        lines.append("")
    lines += ["R 은 손절 폭 대비 몇 배를 벌었는지입니다 (−1R = 손절). 거래비용은 빼지 않았습니다. "
              "진행 중 추천의 R 은 지금 가격 기준이라 확정 값이 아닙니다. "
              "알림 기록은 2026-09-04 부터라 그 전에 연 거래는 없습니다.", "",
              f"> 기준 시각: {str(data.get('generated', ''))[:16].replace('T', ' ')}", "", common.DISCLAIMER]
    return "\n".join(lines) + "\n"
