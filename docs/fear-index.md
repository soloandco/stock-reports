# 시장 현황

## 최근 분석

| 종목 | 기업명 | 분석일 | 판정 | Stage | TT |
|------|--------|--------|------|-------|----|
| [**AAPL**](snapshots/AAPL-2026-10-17.md) | [Apple](snapshots/AAPL-2026-10-17.md) | 2026-10-17 | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 2 | 7/7 |
| [**ADI**](snapshots/ADI-2026-10-17.md) | [ADI ANALOG DEVICES INC](snapshots/ADI-2026-10-17.md) | 2026-10-17 | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 2 | 6/7 |
| [**ADP**](snapshots/ADP-2026-10-17.md) | [ADP AUTOMATIC DATA PROCESSING INC](snapshots/ADP-2026-10-17.md) | 2026-10-17 | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 2 | 7/7 |
| [**AEE**](snapshots/AEE-2026-10-17.md) | [AEE AMEREN CORP](snapshots/AEE-2026-10-17.md) | 2026-10-17 | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | 1 | 4/7 |
| [**AEP**](snapshots/AEP-2026-10-17.md) | [AEP AMERICAN ELECTRIC POWER CO INC](snapshots/AEP-2026-10-17.md) | 2026-10-17 | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | 1 | 4/7 |

[→ 전체 스냅샷](snapshots/index.md)

## 섹터 히트맵 (S&P 500)

<div class="tradingview-widget-container" style="height:520px;margin-bottom:1rem;">
<div class="tradingview-widget-container__widget" style="height:100%;width:100%"></div>
<script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>
{
  "exchanges": [],
  "dataSource": "SPX500",
  "grouping": "sector",
  "blockSize": "market_cap_basic",
  "blockColor": "change",
  "locale": "ko",
  "colorTheme": "dark",
  "hasTopBar": true,
  "isDataSetEnabled": true,
  "isZoomEnabled": true,
  "hasSymbolTooltip": true,
  "isMonoSize": false,
  "width": "100%",
  "height": 500
}
</script>
</div>

> 출처: TradingView · 실시간 데이터 (페이지 로드 시점 기준)


## 섹터 자금 흐름

> **RS**: 상대강도 순위 · **신호**: 최근 20일 매집/분산(가격방향×거래량) · **거래대금 비중**: 섹터 쏠림 게이지. 수집: 2026-10-16 20:16 UTC · `--scan` 시 갱신

### 미국 (S&P 500 섹터 ETF)

| 순위 | 섹터 | RS | 신호 | 매집일 | 분산일 | 거래대금 비중 |
|---|---|---|---|---|---|---|
| 1 | Energy | +1.71 | 🟢 매집 | 6 | 3 | 13.5% |
| 2 | Health Care | +0.83 | 🔴 분산 | 4 | 5 | 11.5% |
| 3 | Technology | +0.78 | 🟢 매집 | 5 | 4 | 14.2% |
| 4 | Consumer Staples | +0.41 | 🟢 매집 | 6 | 2 | 9.7% |
| 5 | Materials | +0.26 | 🟢 매집 | 6 | 3 | 3.6% |
| 6 | Financials | +0.17 | 🔴 분산 | 4 | 7 | 15.3% |
| 7 | Industrials | -0.01 | 🔴 분산 | 4 | 7 | 9.3% |
| 8 | Real Estate | -0.09 | 🔴 분산 | 5 | 6 | 2.4% |
| 9 | Communication | -0.11 | 🟢 매집 | 4 | 3 | 5.4% |
| 10 | Consumer Discretionary | -0.19 | 🔴 분산 | 5 | 6 | 6.4% |
| 11 | Utilities | -0.23 | 🟢 매집 | 5 | 4 | 8.7% |

## 테마별 자금 흐름 (로테이션)

> GPU→전력→반도체→피지컬AI→기판 로테이션 추적. RS+신호로 현재 자금이 어느 테마에 집중되는지 판독. 수집: 2026-10-16 20:16 UTC
>
> **US**: SMH(GPU/반도체)·IRBO(AI인프라)·BOTZ(피지컬AI) ETF + 전력/DataCenter 바스켓

### 미국 테마

| 순위 | 테마 | ETF/바스켓 | RS | 신호 | 매집일 | 분산일 |
|---|---|---|---|---|---|---|
| 1 | GPU/반도체 | SOXX | +1.13 | 🔴 분산 | 1 | 8 |
| 2 | AI인프라 | ARTY | +0.99 | 🔴 분산 | 3 | 5 |
| 3 | 전력/DataCenter | VST·CEG·GEV·VRT·ETN | -0.30 | 🔴 분산 | 2 | 5 |
| 4 | 피지컬AI(로보틱스) | BOTZ | -0.46 | ⚪ 중립 | 5 | 5 |

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.


## CNN Fear & Greed Index

> 수집: 2026-10-16 20:16 UTC · 출처: [CNN Markets](https://edition.cnn.com/markets/fear-and-greed)

| 점수 | 전일比 | 등급 |
|------|--------|------|
| **18.2** / 100 | -13.4 | 🔴 **극공포** |

### 구성 지표 (7개)

| 지표 | 점수 | 등급 |
|------|------|------|
| S&P500 모멘텀 | 23.6 | 🔴 극공포 |
| 신고가/신저가 | 12.0 | 🔴 극공포 |
| 시장 폭 | 12.0 | 🔴 극공포 |
| 풋/콜 비율 | 16.4 | 🔴 극공포 |
| VIX | 4.0 | 🔴 극공포 |
| 정크본드 수요 | 44.2 | 🟠 공포 |
| 안전자산 수요 | 15.0 | 🔴 극공포 |

## VIX

> 수집: 2026-10-16 20:16 UTC · `python monitor.py --scan` 실행 시 갱신

| 지수 | 현재값 | 전일比 | 등급 | 시장 국면 | 신규 진입 |
|------|--------|--------|------|---------|---------|
| VIX (미국 S&P500) | 20.16 | +3.7 | 🟡 주의 | 횡보 | ⚠️ 신규 진입 자제 |

??? info "📘 VIX 등급 기준"
    | 등급 | VIX | 의미 |
    |------|-----|------|
    | 🔴 극공포 | > 40 | 패닉 매도 구간, 저점 매수 기회일 수 있음 |
    | 🟠 공포   | 30–40 | 시장 불안 고조, 변동성 확대 |
    | 🟡 주의   | 20–30 | 불확실성 존재, 선별적 접근 |
    | ⚪ 중립   | 15–20 | 안정적 흐름, 정상 변동성 |
    | 🟢 탐욕   | < 15  | 과열 주의, 변동성 낮음 |

??? info "📘 시장 국면 해석"
    S&P500 / KOSPI의 50·150·200일 MA 정렬 기반으로 판정합니다.

    | 국면 | 한국어 | 신규 진입 |
    |------|--------|---------|
    | STRONG_UPTREND | 강한 상승 | ✅ 허용 |
    | UPTREND | 상승 | ✅ 허용 |
    | RANGING | 횡보 | ⚠️ 자제 |
    | DOWNTREND | 하락 | 🚫 금지 |
    | STRONG_DOWNTREND | 강한 하락 | 🚫 금지 |
