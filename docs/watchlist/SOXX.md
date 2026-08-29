---
type: watchlist
ticker: SOXX
market: NASDAQ
title: SOXX 반도체 ETF 관찰 종목
created: 2026-07-18
updated: 2026-07-18
tags:
  - stock-agent
  - watchlist
  - SOXX
  - semiconductor
  - signal-source
status: watching
comments: true
related:
  - "[[SOXS-semiconductor-bear-3x]]"
---

# SOXX — iShares 반도체 ETF 관찰 종목

> **역할: 인버스 페어 신호원(signal source).** SOXX 자체 매매보다, SOXX가 Stage 4로
> 전환하는 순간 **인버스 체크 알림(🔄)** 을 발생시켜 SOXS 매수 검토를 트리거하는
> 용도로 등록됐다 (`core/inverse.py`, 2026-07-18).
> 판정·Stage·손절가의 SSOT는 스냅샷(`snapshots/SOXX-YYYY-MM-DD.md`)이다.


## 차트

<div class="stock-chart" data-src="../charts/SOXX.json"></div>

<p class="stock-chart-note">추세선·매물벽(저항)·지지대·주봉 저항을 함께 표시합니다. 손가락으로 확대·이동할 수 있습니다.</p>

## 인버스 페어 백테스트 근거 (2026-07-18)

`data/inverse_pairs_backtest.json` — 기초 Stage 4 확정 전환 → SOXS 종가 매수,
2N ATR 손절, 3R/60일 청산, 비겹침:

| 기초 | 기대값 | n |
|------|--------|---|
| ^SOX | +0.566R | 14 |
| SOXX | +0.166R | 15 |

- **저표본 + 기초 정의 민감** — 검증된 엣지가 아니라 참고 신호. 판정·원장 미반영.
- Stage 3(천장권) 포함 시 두 기초 모두 음수(-0.14~-0.21R) — **Stage 4 전환만** 유효.
- 양자(QTUM) 페어는 합성 -2x조차 음수 + 바스켓 인버스 상품 부재로 기각.
- 인버스 진입 시 손절·타겟은 **SOXS 스냅샷**의 2N ATR 기준을 쓴다.
