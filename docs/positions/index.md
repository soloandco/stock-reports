# 오픈 포지션

현재 **매수후보/매수관찰** 판정인 종목의 진입가 대비 현재 수익률·R-배수. 진입가 = 비매수→매수로 전환된 **첫 스냅샷 가격**, 현재가 = **최신 스냅샷 가격**입니다.

!!! warning "가정된 진입 (실제 체결 아님)"
    진입가는 판정이 매수로 바뀐 시점의 분석용 스냅샷 가격이며, 실제 매매 체결가가 아닙니다. R-배수·수익률은 그 가정 진입가 기준의 참고 수치입니다.

??? info "📘 R이 뭔가요? (수익률 %와 뭐가 다른가요)"
    **R = 이 매매에서 각오한 손실폭(진입가→손절가)을 1로 봤을 때, 지금 얼마나 벌었나**를 나타내는 숫자입니다.

    - **1R** = 진입가 − 손절가 (각오한 최대 손실폭)
    - **R배수** = 지금 이익 ÷ 1R

    예시 — $100에 사서 손절을 $90에 뒀다면 1R = $10.
    현재가 $110이면 이익 $10 → **+1.0R** (각오한 손실만큼 벌었다는 뜻). 현재가가 $90까지 내려가 손절되면 **−1.0R**.

    **왜 수익률 %만으로는 부족한가?** 종목마다 손절폭이 다르기 때문입니다. +6% 올라도 손절이 −25% 멀리 있으면 +0.2R에 불과하고, +4%라도 손절이 −9%로 가까우면 +0.8R입니다. **R은 '감수한 위험 대비' 성과라, 종목이 달라도 같은 잣대로 비교**할 수 있습니다.

    | R 값 | 의미 |
    |------|------|
    | **+3R** | 목표 도달 (3:1 리워드) |
    | **+1.5R** | 손절선을 본전으로 올릴 때 |
    | **+1R** | 각오한 위험만큼 벌었다 |
    | **0R** | 본전 |
    | **−1R** | 손절 도달 (청산) |

<div class="seed-panel">
<label>시드 (원): <input type="number" id="seed-input" min="0" step="100000" placeholder="예: 10000000"></label>
&nbsp;&nbsp;<label>트레이드당 리스크: <input type="number" id="risk-input" min="0.1" step="0.1" value="1" style="width:4.5em"> %</label>
<p class="seed-hint">💡 시드를 입력하면 종목별 <b>주수·손익(원)</b>과 아래 <b>포트폴리오 요약</b>이 계산됩니다. 시드는 이 브라우저에만 저장되며 서버·공개 저장소에 올라가지 않습니다.</p>
<div id="seed-summary"></div>
</div>


| 종목 | 판정 | 진입일 | 진입가 | 현재가 | 수익률 | R | 손절까지 | 타겟까지 | 보유 | 주수 | 손익(원) |
|------|------|--------|--------|--------|--------|---|---------|---------|------|------|---------|
| [**KO**](../snapshots/KO-2026-08-07.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $86.86 | 🟢 +5.1% | +1.4R | -8.4% | +5.7% | 38일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**AVGO**](../snapshots/AVGO-2026-08-07.md) Broadcom | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $392.23 | $420.57 | 🟢 +7.2% | +0.8R | -14.8% | +17.3% | 3일 | <span class="js-shares" data-ticker="AVGO">—</span> | <span class="js-pnl" data-ticker="AVGO">—</span> |
| [**USD**](../snapshots/USD-2026-08-07.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $90.38 | 🟢 +16.5% | +0.8R | -31.7% | +38.3% | 7일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-08-07.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $206.64 | $218.99 | 🟢 +6.0% | +0.8R | -12.6% | +15.3% | 3일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**CAT**](../snapshots/CAT-2026-08-07.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $808.91 | $857.36 | 🟢 +6.0% | +0.6R | -15.1% | +22.7% | 7일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |
| [**PM**](../snapshots/PM-2026-08-07.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $188.05 | 🟢 +2.8% | +0.5R | -7.9% | +12.6% | 38일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**161890**](../snapshots/161890-2026-08-07.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | ₩95,100 | ₩102,300 | 🟢 +7.6% | +0.5R | -21.9% | +37.5% | 7일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**066570**](../snapshots/066570-2026-08-07.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-05 | ₩165,500 | ₩179,500 | 🟢 +8.5% | +0.4R | -27.2% | +50.3% | 2일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**278470**](../snapshots/278470-2026-08-07.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | ₩338,000 | ₩357,500 | 🟢 +5.8% | +0.4R | -19.8% | +37.7% | 3일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**BE**](../snapshots/BE-2026-08-07.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $207.21 | $228.74 | 🟢 +10.4% | +0.4R | -35.0% | +67.4% | 7일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**MS**](../snapshots/MS-2026-08-07.md) Morgan Stanley | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $211.72 | $213.76 | 🟢 +1.0% | +0.2R | -6.4% | +15.5% | 38일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**009150**](../snapshots/009150-2026-08-07.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,356,000 | 🟢 +5.2% | +0.2R | -33.2% | +80.0% | 25일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**GEV**](../snapshots/GEV-2026-08-07.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $982.55 | $999.74 | 🟢 +1.7% | +0.1R | -14.1% | +35.3% | 7일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-08-07.md) Alphabet | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 08-01 | $356.13 | $357.75 | 🟢 +0.5% | +0.1R | -7.1% | +19.5% | 6일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-08-07.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $532.52 | 🟢 +0.7% | +0.1R | -12.6% | +35.2% | 20일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**CDNS**](../snapshots/CDNS-2026-08-07.md) Cadence Design Systems | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-28 | $338.61 | $338.42 | 🔴 -0.1% | -0.0R | -8.8% | +26.5% | 10일 | <span class="js-shares" data-ticker="CDNS">—</span> | <span class="js-pnl" data-ticker="CDNS">—</span> |
| [**BA**](../snapshots/BA-2026-08-07.md) Boeing | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $233.49 | $232.17 | 🔴 -0.6% | -0.1R | -6.0% | +20.4% | 3일 | <span class="js-shares" data-ticker="BA">—</span> | <span class="js-pnl" data-ticker="BA">—</span> |
| [**CORZ**](../snapshots/CORZ-2026-08-07.md) Core Scientific | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $21.81 | $21.05 | 🔴 -3.5% | -0.2R | -15.0% | +59.4% | 7일 | <span class="js-shares" data-ticker="CORZ">—</span> | <span class="js-pnl" data-ticker="CORZ">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-08-07.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-30 | $133.87 | $132.06 | 🔴 -1.4% | -0.3R | -4.0% | +17.5% | 8일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**LLY**](../snapshots/LLY-2026-08-07.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,192.28 | 🔴 -1.9% | -0.3R | -4.4% | +21.1% | 29일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-08-07.md) Apple | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-13 | $318.73 | $312.41 | 🔴 -2.0% | -0.4R | -3.0% | +17.1% | 25일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**DLR**](../snapshots/DLR-2026-08-07.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $192.54 | 🔴 -3.3% | -0.6R | -2.5% | +21.2% | 13일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**GS**](../snapshots/GS-2026-08-07.md) Goldman Sachs | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-25 | $1,076.91 | $1,032.50 | 🔴 -4.1% | -0.7R | -1.7% | +22.4% | 43일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**AMD**](../snapshots/AMD-2026-08-07.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $489.28 | 🔴 -10.1% | -0.8R | -2.8% | +53.2% | 25일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |

**합계** 24포지션 · 평균 +0.2R · 양의 R 15/24

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 86.86499786376953, "r": 1.3732971403369043}, {"ticker": "AVGO", "entry": 392.2300109863281, "stop": 358.4747922503201, "current": 420.56500244140625, "r": 0.8394255026661126}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 90.375, "r": 0.8110888984301249}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 218.99000549316406, "r": 0.8067469141196716}, {"ticker": "CAT", "entry": 808.905029296875, "stop": 727.7539578057504, "current": 857.3599853515625, "r": 0.5970957026733398}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 188.0500030517578, "r": 0.5390317236863815}, {"ticker": "161890", "entry": 95100.0, "stop": 79921.43092159486, "current": 102300.0, "r": 0.47435301462267526}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 179500.0, "r": 0.40299909250329097}, {"ticker": "278470", "entry": 338000.0, "stop": 286622.8624105194, "current": 357500.0, "r": 0.3795462517941559}, {"ticker": "BE", "entry": 207.2100067138672, "stop": 148.66912487910352, "current": 228.7449951171875, "r": 0.36786238485618555}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 213.76499938964844, "r": 0.1747353607472783}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1356000.0, "r": 0.17456730405412246}, {"ticker": "GEV", "entry": 982.5499877929688, "stop": 859.1024131708681, "current": 999.739990234375, "r": 0.13924941412602485}, {"ticker": "GOOGL", "entry": 356.1300048828125, "stop": 332.3223349724717, "current": 357.75, "r": 0.06804509316906565}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 532.52001953125, "r": 0.054970486530886126}, {"ticker": "CDNS", "entry": 338.6099853515625, "stop": 308.74442908515095, "current": 338.4200134277344, "r": -0.006360903581822045}, {"ticker": "BA", "entry": 233.49000549316406, "stop": 218.1540878686476, "current": 232.1699981689453, "r": -0.08607292739422033}, {"ticker": "CORZ", "entry": 21.809999465942383, "stop": 17.894681127765164, "current": 21.049999237060547, "r": -0.19410943459469887}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 132.05999755859375, "r": -0.2555030136505058}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1192.2750244140625, "r": -0.30946704984138046}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 312.4100036621094, "r": -0.40239835155141507}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 192.5399932861328, "r": -0.5714746220794693}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1032.5, "r": -0.7145427696693568}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 489.2799987792969, "r": -0.7989012079680667}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

