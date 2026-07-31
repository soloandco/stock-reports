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
| [**KO**](../snapshots/KO-2026-08-01.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $87.59 | 🟢 +6.0% | +1.6R | -9.1% | +4.9% | 32일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**PM**](../snapshots/PM-2026-08-01.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $190.82 | 🟢 +4.3% | +0.8R | -9.2% | +10.9% | 32일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**KMI**](../snapshots/KMI-2026-08-01.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $32.18 | 🟢 +1.5% | +0.3R | -5.8% | +11.8% | 30일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**CAT**](../snapshots/CAT-2026-08-01.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $808.91 | $814.81 | 🟢 +0.7% | +0.1R | -10.7% | +29.2% | 1일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |
| [**USD**](../snapshots/USD-2026-08-01.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $78.69 | 🟢 +1.5% | +0.1R | -21.5% | +58.8% | 1일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**GEV**](../snapshots/GEV-2026-08-01.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $982.55 | $990.29 | 🟢 +0.8% | +0.1R | -13.2% | +36.6% | 1일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**CDNS**](../snapshots/CDNS-2026-08-01.md) Cadence Design Systems | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-28 | $338.61 | $340.02 | 🟢 +0.4% | +0.0R | -9.2% | +25.9% | 4일 | <span class="js-shares" data-ticker="CDNS">—</span> | <span class="js-pnl" data-ticker="CDNS">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-08-01.md) Skyward Specialty Insurance | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $59.87 | $59.95 | 🟢 +0.1% | +0.0R | -7.3% | +21.5% | 1일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |
| [**161890**](../snapshots/161890-2026-08-01.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | ₩95,100 | ₩95,200 | 🟢 +0.1% | +0.0R | -16.0% | +47.7% | 1일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**066570**](../snapshots/066570-2026-08-01.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-01 | ₩162,100 | ₩162,100 | ⚪ +0.0% | +0.0R | -22.5% | +67.5% | 0일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-08-01.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-01 | $356.13 | $356.13 | ⚪ +0.0% | +0.0R | -6.7% | +20.1% | 0일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**BE**](../snapshots/BE-2026-08-01.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $207.21 | $205.81 | 🔴 -0.7% | -0.0R | -27.8% | +86.0% | 1일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**CIFR**](../snapshots/CIFR-2026-08-01.md) Cipher Mining | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $22.66 | $22.32 | 🔴 -1.5% | -0.1R | -22.8% | +74.6% | 1일 | <span class="js-shares" data-ticker="CIFR">—</span> | <span class="js-pnl" data-ticker="CIFR">—</span> |
| [**MS**](../snapshots/MS-2026-08-01.md) Morgan Stanley | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $211.72 | $210.42 | 🔴 -0.6% | -0.1R | -4.9% | +17.3% | 32일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-08-01.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-30 | $133.87 | $132.68 | 🔴 -0.9% | -0.2R | -4.4% | +16.9% | 2일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**CORZ**](../snapshots/CORZ-2026-08-01.md) Core Scientific | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $21.81 | $20.72 | 🔴 -5.0% | -0.3R | -13.6% | +61.9% | 1일 | <span class="js-shares" data-ticker="CORZ">—</span> | <span class="js-pnl" data-ticker="CORZ">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-08-01.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $504.89 | 🔴 -4.6% | -0.4R | -7.8% | +42.6% | 14일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**009150**](../snapshots/009150-2026-08-01.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,142,000 | 🔴 -11.4% | -0.4R | -20.7% | +113.7% | 19일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-08-01.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $308.91 | 🔴 -3.1% | -0.6R | -1.9% | +18.4% | 19일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**LLY**](../snapshots/LLY-2026-08-01.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,148.84 | 🔴 -5.5% | -0.9R | -0.8% | +25.7% | 23일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**DLR**](../snapshots/DLR-2026-08-01.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $188.52 | 🔴 -5.3% | -0.9R | -0.5% | +23.8% | 7일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**GS**](../snapshots/GS-2026-08-01.md) Goldman Sachs | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-25 | $1,076.91 | $1,018.38 | 🔴 -5.4% | -0.9R | -0.4% | +24.1% | 37일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**AMD**](../snapshots/AMD-2026-08-01.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $476.15 | 🔴 -12.5% | -1.0R | -0.1% | +57.4% | 19일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |

**합계** 23포지션 · 평균 -0.1R · 양의 R 9/23

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 87.58999633789062, "r": 1.6095104727919876}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 190.82000732421875, "r": 0.8272784206920911}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 32.18000030517578, "r": 0.3251701772246821}, {"ticker": "CAT", "entry": 808.905029296875, "stop": 727.7539578057504, "current": 814.8099975585938, "r": 0.07276512993872875}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 78.69000244140625, "r": 0.07209676952692752}, {"ticker": "GEV", "entry": 982.5499877929688, "stop": 859.1024131708681, "current": 990.2899780273438, "r": 0.06269860107068738}, {"ticker": "CDNS", "entry": 338.6099853515625, "stop": 308.74442908515095, "current": 340.0199890136719, "r": 0.047211699307778944}, {"ticker": "SKWD", "entry": 59.869998931884766, "stop": 55.5506716263135, "current": 59.95000076293945, "r": 0.01852182652412044}, {"ticker": "161890", "entry": 95100.0, "stop": 79921.43092159486, "current": 95200.0, "r": 0.006588236314203823}, {"ticker": "066570", "entry": 162100.0, "stop": 125601.90324299496, "current": 162100.0, "r": 0.0}, {"ticker": "GOOGL", "entry": 356.1300048828125, "stop": 332.3223349724717, "current": 356.1300048828125, "r": 0.0}, {"ticker": "BE", "entry": 207.2100067138672, "stop": 148.66912487910352, "current": 205.80999755859375, "r": -0.02391506775085957}, {"ticker": "CIFR", "entry": 22.655000686645508, "stop": 17.219999176066082, "current": 22.31999969482422, "r": -0.061637699855132996}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 210.4199981689453, "r": -0.11107907364954649}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 132.67999267578125, "r": -0.16798321555029208}, {"ticker": "CORZ", "entry": 21.809999465942383, "stop": 17.894681127765164, "current": 20.719999313354492, "r": -0.27839374948381373}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 504.8900146484375, "r": -0.3789823166859603}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1142000.0, "r": -0.38300587605904485}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 308.9100036621094, "r": -0.6252452816543089}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1148.8399658203125, "r": -0.8801211976764982}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 188.52000427246094, "r": -0.9227465946727706}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1018.3800048828125, "r": -0.9417288235672318}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 476.1499938964844, "r": -0.9906492992988035}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

