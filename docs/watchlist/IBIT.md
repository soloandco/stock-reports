---
type: watchlist
ticker: IBIT
market: NASDAQ
title: IBIT 비트코인 현물 ETF 관찰 종목
created: 2026-08-23
updated: 2026-08-23
tags:
  - stock-agent
  - watchlist
  - IBIT
  - crypto
  - signal-source
status: watching
comments: true
lines:
  - kind: ma
    period: 150
    direction: above
    note: SMA150 탈환 (BITX 실행 트리거)
related:
  - "[[BITX-2x-bitcoin-strategy]]"
---

# IBIT — iShares 비트코인 현물 ETF 관찰 종목

> **역할: BITX의 기초자산 신호원(signal source).** IBIT 자체 매매보다, **국면
> 판정을 정직하게 받기 위해** 등록됐다 (GDX→GDXU 선례, 2026-08-10). 실행은 필요 시
> BITX(2x)로 하되 **판정·Stage·매물대·주봉 저항은 이 종목에서 읽는다.**
> 판정의 SSOT는 스냅샷(`snapshots/IBIT-YYYY-MM-DD.md`)이다.

## 왜 2배 ETF가 아니라 기초자산을 보는가

BITX는 **일일 리밸런싱 2배 선물 ETF**라 가격 경로가 복리 누적과 롤 비용의 산물이다.
장기 이평·매물대·주봉 저항이 구조적으로 왜곡된다. 등록일 기준 BITX는 52주 고점 대비
-72.7%인데 IBIT는 그보다 훨씬 얕다. 같은 날짜의 Stage·TT 점수가 두 종목에서 다르게
나오면 **IBIT 쪽이 정본**이다.

---
