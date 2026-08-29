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
    note: SMA150 재탈환 (BITX 실행 트리거. 2026-08-23 등록 시점엔 이미 위 — 이탈 후 재돌파에 발화)
  - kind: ma
    period: 150
    direction: below
    note: SMA150 이탈 (BITX 논거 무효 — 검토 철회)
related:
  - "[[BITX-2x-bitcoin-strategy]]"
---

# IBIT — iShares 비트코인 현물 ETF 관찰 종목

> **역할: BITX의 기초자산 신호원(signal source).** IBIT 자체 매매보다, **국면
> 판정을 정직하게 받기 위해** 등록됐다 (GDX→GDXU 선례, 2026-08-10). 실행은 필요 시
> BITX(2x)로 하되 **판정·Stage·매물대·주봉 저항은 이 종목에서 읽는다.**
> 판정의 SSOT는 스냅샷(`snapshots/IBIT-YYYY-MM-DD.md`)이다.


## 차트

<div class="stock-chart" data-src="../charts/IBIT.json"></div>

<p class="stock-chart-note">추세선·매물벽(저항)·지지대·주봉 저항을 함께 표시합니다. 손가락으로 확대·이동할 수 있습니다.</p>

## 왜 2배 ETF가 아니라 기초자산을 보는가

BITX는 **일일 리밸런싱 2배 선물 ETF**라 가격 경로가 복리 누적과 롤 비용의 산물이다.
장기 이평·매물대·주봉 저항이 구조적으로 왜곡된다. 등록일 기준 BITX는 52주 고점 대비
-72.7%인데 IBIT는 그보다 훨씬 얕다. 같은 날짜의 Stage·TT 점수가 두 종목에서 다르게
나오면 **IBIT 쪽이 정본**이다.

---

## 분석 메모 (2026-08-23)

**약세 논거**
- Stage 1, TT 3/8. 현재가 $43.68이 SMA150($39.95)·SMA200($43.00)을 막 넘겼지만 이평 배열은 아직 역배열(SMA50 < SMA150 < SMA200).
- **3거래일 +19.3% (08-19~21)** 뒤라 SMA50 이격 +20.4%, RSI 79.5. 추격 자리가 아니다.
- 주봉 머리 위 저항 $46.56 (+6.6%), 과거 -27% 거부 이력. 52주 고점 대비 -25% 밖.
- 시장 국면 RANGING. 08-19 급등은 미 재무부 국채 바이백 확대·SEC 규제안 같은 **외부 촉매**가 쏟아낸 숏 청산(1시간 $10억)이 밀어 올린 것이라, 차트 구조가 만든 상승이 아니다.

**강세 논거**
- 수급 2/2 (거래량 1.86배, OBV 상승). SMA200을 종가로 되찾았다.
- 매물벽 $50.71~52.33까지 **에어포켓 +16.1%**. 주봉 저항 $46.56만 넘기면 위가 가볍다.
- 2배 ETF(BITX)보다 왜곡이 없어 이 종목의 Stage 전환이 BITX 실행의 정직한 트리거다.

**판정: 매수불가 (기준미달)** — Stage 1 + TT 3/8. 보는 자리는 **SMA150 탈환 유지 + 이평 정배열 전환**(lines에 SMA150 등록됨)이며, 그때 BITX 실행을 검토한다.
