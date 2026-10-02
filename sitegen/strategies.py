"""「방식별 기록」 페이지.

2026-10-02 gen.py 에서 나눴다. 다른 sitegen 모듈은 함수를 이름째 가져오지 않고
「모듈.이름」으로 부른다(테스트가 한 곳만 바꿔 끼워도 모든 호출에 먹게).
"""
from __future__ import annotations

import json

from sitegen import common, config as cfg


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


def _strategies_index(data: dict, names: dict) -> str:
    """스윙·단타 두 방식의 켜져 있던 기간별 성적과 최근 거래. 모바일 4열 이하."""
    lines = [
        "# 방식별 기록",
        "",
        "스윙(일봉)과 단타(1시간봉) 두 방식을 섞지 않고 따로 기록합니다. **켜진 방식만 알림이 나가고**, "
        "꺼진 방식은 같은 기간에 무엇을 했을지 기록만 합니다. 「둘 다」가 켜진 기간에는 두 방식 모두 알림이 "
        "나갑니다. 텔레그램에 「둘다」·「단타」·「스윙」을 보내 바꿉니다.",
        "",
    ]
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
    total = sum(p["active"].get("closed", 0)
                + (p["other"].get("closed", 0) if p["strategy"] == "both" else 0)
                for p in periods)
    min_n = data.get("min_n", 100)
    lines += ["", f'!!! warning "표본 부족: 알림 나간 끝난 거래 {total}건"',
              f"    {min_n}건이 쌓이기 전에는 두 방식의 우열을 가릴 수 없습니다. 숫자는 기록으로만 읽으세요.",
              ""] if total < min_n else [""]
    money = data.get("money") or {}
    if money:
        seed = int(data.get("seed_won", 1_000_000)) // 10000
        r_won = float(data.get("r_won", 10000))
        lines += ["## 추천대로 했다면", "",
                  f"사지 않았어도 **알림이 나간 추천을 그대로 따랐을 때**의 결과입니다. "
                  f"시드 {seed}만 원에서 추천마다 {r_won:,.0f}원(시드 1%)을 손절 위험으로 건 경우로 환산합니다. "
                  "진행 중인 추천은 지금 가격으로 평가합니다.", "",
                  "| 방식 | 끝난 추천 | 진행 중 | 합계 |", "|---|---:|---:|---:|"]
        for key in ("base", "book"):
            m = money.get(key)
            if not m:
                continue
            won = lambda r: f"{r * r_won:+,.0f}원"  # noqa: E731
            lines.append(f"| {common._STRAT_LABEL[key]} | {m['closed']}건 {won(m['closed_r'])} | "
                         f"{m['open']}건 {won(m['open_r'])} | **{m['total_won']:+,.0f}원** |")
        lines.append("")
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
