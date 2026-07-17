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
| [**PM**](../snapshots/PM-2026-07-18.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $191.75 | 🟢 +4.9% | +0.9R | -9.6% | +10.4% | 18일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-07-18.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $332.18 | 🟢 +4.2% | +0.9R | -8.8% | +10.1% | 5일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**MS**](../snapshots/MS-2026-07-18.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $217.28 | 🟢 +2.6% | +0.5R | -7.9% | +13.6% | 18일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**KMI**](../snapshots/KMI-2026-07-18.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $32.31 | 🟢 +1.9% | +0.4R | -6.2% | +11.3% | 16일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**278470**](../snapshots/278470-2026-07-18.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩375,000 | ₩393,000 | 🟢 +4.8% | +0.3R | -19.9% | +41.2% | 5일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-07-18.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $125.00 | $126.73 | 🟢 +1.4% | +0.3R | -6.4% | +13.7% | 5일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**161890**](../snapshots/161890-2026-07-18.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-14 | ₩106,500 | ₩107,600 | 🟢 +1.0% | +0.1R | -14.7% | +40.1% | 4일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**GS**](../snapshots/GS-2026-07-18.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-25 | $1,076.91 | $1,079.99 | 🟢 +0.3% | +0.0R | -6.0% | +17.0% | 23일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-07-18.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $529.02 | ⚪ +0.0% | +0.0R | -12.0% | +36.1% | 0일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**009150**](../snapshots/009150-2026-07-18.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,277,000 | 🔴 -0.9% | -0.0R | -29.1% | +91.1% | 5일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-07-18.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $207.37 | $205.41 | 🔴 -0.9% | -0.1R | -5.9% | +21.5% | 5일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**066570**](../snapshots/066570-2026-07-18.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩185,600 | ₩179,000 | 🔴 -3.6% | -0.1R | -20.9% | +77.5% | 5일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**KO**](../snapshots/KO-2026-07-18.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $82.11 | 🔴 -0.7% | -0.2R | -3.1% | +11.9% | 18일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-07-18.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $355.50 | $346.64 | 🔴 -2.5% | -0.4R | -3.4% | +20.5% | 5일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**GEV**](../snapshots/GEV-2026-07-18.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $1,102.51 | $1,055.09 | 🔴 -4.3% | -0.5R | -4.9% | +32.8% | 18일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**USD**](../snapshots/USD-2026-07-18.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $92.19 | $84.67 | 🔴 -8.2% | -0.5R | -9.7% | +64.7% | 5일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**LLY**](../snapshots/LLY-2026-07-18.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,178.57 | 🔴 -3.1% | -0.5R | -3.3% | +22.5% | 9일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**CORZ**](../snapshots/CORZ-2026-07-18.md) Core Scientific | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $22.63 | $20.87 | 🔴 -7.8% | -0.5R | -8.6% | +59.4% | 5일 | <span class="js-shares" data-ticker="CORZ">—</span> | <span class="js-pnl" data-ticker="CORZ">—</span> |
| [**AVGO**](../snapshots/AVGO-2026-07-18.md) Broadcom | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $391.85 | $374.06 | 🔴 -4.5% | -0.5R | -4.6% | +32.8% | 5일 | <span class="js-shares" data-ticker="AVGO">—</span> | <span class="js-pnl" data-ticker="AVGO">—</span> |
| [**AMD**](../snapshots/AMD-2026-07-18.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $500.92 | 🔴 -7.9% | -0.6R | -5.1% | +49.6% | 5일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**BE**](../snapshots/BE-2026-07-18.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $275.01 | $218.68 | 🔴 -20.5% | -1.0R | -0.7% | +105.3% | 18일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**CAT**](../snapshots/CAT-2026-07-18.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $991.41 | $885.76 | 🔴 -10.7% | -1.3R | +3.0% | +38.6% | 16일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |

**합계** 22포지션 · 평균 -0.1R · 양의 R 8/22

<script type="application/json" id="pos-data">
[{"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 191.75070190429688, "r": 0.9241265163054232}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 332.17999267578125, "r": 0.856367751267075}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 217.27999877929688, "r": 0.4750753296057578}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 32.310001373291016, "r": 0.41706665377587104}, {"ticker": "278470", "entry": 375000.0, "stop": 314981.3971592858, "current": 393000.0, "r": 0.2999070146262972}, {"ticker": "PCAR", "entry": 125.00499725341797, "stop": 118.63641278688668, "current": 126.7300033569336, "r": 0.27086177667596617}, {"ticker": "161890", "entry": 106500.0, "stop": 91763.98947207628, "current": 107600.0, "r": 0.07464706936219788}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1079.989990234375, "r": 0.0495554748026496}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 529.02001953125, "r": 0.0}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1277000.0, "r": -0.031265785800738355}, {"ticker": "NVDA", "entry": 207.3699951171875, "stop": 193.26880716964297, "current": 205.41000366210938, "r": -0.1389947756436664}, {"ticker": "066570", "entry": 185600.0, "stop": 141564.11742172934, "current": 179000.0, "r": -0.14987777270658692}, {"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 82.1050033569336, "r": -0.17756704084730052}, {"ticker": "GOOGL", "entry": 355.5, "stop": 334.78411647226744, "current": 346.6400146484375, "r": -0.42769044051157895}, {"ticker": "GEV", "entry": 1102.510009765625, "stop": 1002.9343461066205, "current": 1055.0899658203125, "r": -0.4762212191495083}, {"ticker": "USD", "entry": 92.19000244140625, "stop": 76.43252202238607, "current": 84.66609954833984, "r": -0.47748134174957463}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1178.570068359375, "r": -0.48952413441109693}, {"ticker": "CORZ", "entry": 22.6299991607666, "stop": 19.081676322606583, "current": 20.8700008392334, "r": -0.49600850931755963}, {"ticker": "AVGO", "entry": 391.8500061035156, "stop": 356.8287411224586, "current": 374.05999755859375, "r": -0.5079773261915148}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 500.9200134277344, "r": -0.628912650323173}, {"ticker": "BE", "entry": 275.010009765625, "stop": 217.05686725842352, "current": 218.6750030517578, "r": -0.9720785496121592}, {"ticker": "CAT", "entry": 991.4099731445312, "stop": 912.5806793261623, "current": 885.760009765625, "r": -1.3402373440301902}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

