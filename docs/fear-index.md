# 시장 현황

## 최근 분석

| 종목 | 기업명 | 분석일 | 판정 | Stage | TT |
|------|--------|--------|------|-------|----|
| [**AAPL**](snapshots/AAPL-2026-10-20.md) | [Apple](snapshots/AAPL-2026-10-20.md) | 2026-10-20 | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 2 | 7/7 |
| [**ADI**](snapshots/ADI-2026-10-20.md) | [ADI ANALOG DEVICES INC](snapshots/ADI-2026-10-20.md) | 2026-10-20 | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 2 | 6/7 |
| [**ADP**](snapshots/ADP-2026-10-20.md) | [ADP AUTOMATIC DATA PROCESSING INC](snapshots/ADP-2026-10-20.md) | 2026-10-20 | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 2 | 7/7 |
| [**AEE**](snapshots/AEE-2026-10-20.md) | [AEE AMEREN CORP](snapshots/AEE-2026-10-20.md) | 2026-10-20 | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | 4 | 3/7 |
| [**AEP**](snapshots/AEP-2026-10-20.md) | [AEP AMERICAN ELECTRIC POWER CO INC](snapshots/AEP-2026-10-20.md) | 2026-10-20 | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | 4 | 3/7 |

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

> **RS**: 상대강도 순위 · **신호**: 최근 20일 매집/분산(가격방향×거래량) · **거래대금 비중**: 섹터 쏠림 게이지. 수집: 2026-10-19 23:34 UTC · `--scan` 시 갱신

### 미국 (S&P 500 섹터 ETF)

| 순위 | 섹터 | RS | 신호 | 매집일 | 분산일 | 거래대금 비중 |
|---|---|---|---|---|---|---|
| 1 | Energy | +1.61 | 🟢 매집 | 6 | 2 | 13.8% |
| 2 | Technology | +0.90 | 🟢 매집 | 5 | 4 | 14.5% |
| 3 | Health Care | +0.82 | 🔴 분산 | 4 | 6 | 11.1% |
| 4 | Consumer Staples | +0.36 | 🟢 매집 | 5 | 3 | 10.1% |
| 5 | Materials | +0.26 | 🟢 매집 | 6 | 3 | 3.6% |
| 6 | Financials | +0.15 | 🔴 분산 | 4 | 7 | 15.4% |
| 7 | Industrials | -0.02 | 🔴 분산 | 3 | 7 | 9.3% |
| 8 | Consumer Discretionary | -0.07 | 🟢 매집 | 4 | 3 | 6.5% |
| 9 | Communication | -0.08 | 🔴 분산 | 3 | 4 | 4.7% |
| 10 | Real Estate | -0.11 | 🔴 분산 | 4 | 6 | 2.2% |
| 11 | Utilities | -0.34 | 🟢 매집 | 5 | 2 | 8.7% |

## 테마별 자금 흐름 (로테이션)

> GPU→전력→반도체→피지컬AI→기판 로테이션 추적. RS+신호로 현재 자금이 어느 테마에 집중되는지 판독. 수집: 2026-10-19 23:34 UTC
>
> **US**: SMH(GPU/반도체)·IRBO(AI인프라)·BOTZ(피지컬AI) ETF + 전력/DataCenter 바스켓

### 미국 테마

| 순위 | 테마 | ETF/바스켓 | RS | 신호 | 매집일 | 분산일 |
|---|---|---|---|---|---|---|
| 1 | GPU/반도체 | SOXX | +1.24 | 🔴 분산 | 1 | 6 |
| 2 | AI인프라 | ARTY | +1.12 | 🔴 분산 | 4 | 5 |
| 3 | 전력/DataCenter | VST·CEG·GEV·VRT·ETN | -0.27 | 🔴 분산 | 2 | 6 |
| 4 | 피지컬AI(로보틱스) | BOTZ | -0.35 | 🔴 분산 | 2 | 5 |

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.


## CNN Fear & Greed Index

> 수집: 2026-10-19 23:33 UTC · 출처: [CNN Markets](https://edition.cnn.com/markets/fear-and-greed)

| 점수 | 전일比 | 등급 |
|------|--------|------|
| **23.1** / 100 | +5.2 | 🔴 **극공포** |

### 구성 지표 (7개)

| 지표 | 점수 | 등급 |
|------|------|------|
| S&P500 모멘텀 | 29.4 | 🟠 공포 |
| 신고가/신저가 | 12.4 | 🔴 극공포 |
| 시장 폭 | 13.4 | 🔴 극공포 |
| 풋/콜 비율 | 15.4 | 🔴 극공포 |
| VIX | 18.8 | 🔴 극공포 |
| 정크본드 수요 | 52.4 | ⚪ 중립 |
| 안전자산 수요 | 20.0 | 🔴 극공포 |

## VIX

> 수집: 2026-10-19 23:33 UTC · `python monitor.py --scan` 실행 시 갱신

| 지수 | 현재값 | 전일比 | 등급 | 시장 국면 | 신규 진입 |
|------|--------|--------|------|---------|---------|
| VIX (미국 S&P500) | 18.44 | -1.55 | ⚪ 중립 | 횡보 | ⚠️ 신규 진입 자제 |

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
