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
| [**MS**](../snapshots/MS-2026-07-16.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $228.55 | 🟢 +7.9% | +1.4R | -12.5% | +8.0% | 16일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**GS**](../snapshots/GS-2026-07-16.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-25 | $1,076.91 | $1,152.07 | 🟢 +7.0% | +1.2R | -11.9% | +9.7% | 21일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-07-16.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $355.50 | $370.92 | 🟢 +4.3% | +0.7R | -9.7% | +12.6% | 3일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-07-16.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $327.50 | 🟢 +2.8% | +0.6R | -7.5% | +11.7% | 3일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-07-16.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $207.37 | $212.50 | 🟢 +2.5% | +0.4R | -9.0% | +17.5% | 3일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**KMI**](../snapshots/KMI-2026-07-16.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $32.20 | 🟢 +1.5% | +0.3R | -5.9% | +11.7% | 14일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**009150**](../snapshots/009150-2026-07-16.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,413,000 | 🟢 +9.6% | +0.3R | -35.9% | +72.7% | 3일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**066570**](../snapshots/066570-2026-07-16.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩185,600 | ₩194,000 | 🟢 +4.5% | +0.2R | -27.0% | +63.8% | 3일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**278470**](../snapshots/278470-2026-07-16.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩375,000 | ₩385,500 | 🟢 +2.8% | +0.2R | -18.3% | +44.0% | 3일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**AVGO**](../snapshots/AVGO-2026-07-16.md) Broadcom | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $391.85 | $394.28 | 🟢 +0.6% | +0.1R | -9.5% | +26.0% | 3일 | <span class="js-shares" data-ticker="AVGO">—</span> | <span class="js-pnl" data-ticker="AVGO">—</span> |
| [**161890**](../snapshots/161890-2026-07-16.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-14 | ₩106,500 | ₩107,200 | 🟢 +0.7% | +0.0R | -14.4% | +40.6% | 2일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**CORZ**](../snapshots/CORZ-2026-07-16.md) Core Scientific | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $22.63 | $22.72 | 🟢 +0.4% | +0.0R | -16.0% | +46.5% | 3일 | <span class="js-shares" data-ticker="CORZ">—</span> | <span class="js-pnl" data-ticker="CORZ">—</span> |
| [**USD**](../snapshots/USD-2026-07-16.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $92.19 | $92.30 | 🟢 +0.1% | +0.0R | -17.2% | +51.1% | 3일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-07-16.md) Skyward Specialty Insurance | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-16 | $56.87 | $56.87 | ⚪ +0.0% | +0.0R | -7.2% | +21.6% | 0일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |
| [**KO**](../snapshots/KO-2026-07-16.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $82.45 | 🔴 -0.2% | -0.1R | -3.5% | +11.4% | 16일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**PM**](../snapshots/PM-2026-07-16.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $180.88 | 🔴 -1.1% | -0.2R | -4.2% | +17.0% | 16일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**AMD**](../snapshots/AMD-2026-07-16.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $529.14 | 🔴 -2.7% | -0.2R | -10.1% | +41.6% | 3일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-07-16.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $125.00 | $123.15 | 🔴 -1.5% | -0.3R | -3.7% | +17.0% | 3일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**CIFR**](../snapshots/CIFR-2026-07-16.md) Cipher Mining | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $21.28 | $19.87 | 🔴 -6.6% | -0.3R | -16.3% | +77.2% | 3일 | <span class="js-shares" data-ticker="CIFR">—</span> | <span class="js-pnl" data-ticker="CIFR">—</span> |
| [**GEV**](../snapshots/GEV-2026-07-16.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $1,102.51 | $1,055.28 | 🔴 -4.3% | -0.5R | -5.0% | +32.8% | 16일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**BE**](../snapshots/BE-2026-07-16.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $275.01 | $239.38 | 🔴 -13.0% | -0.6R | -9.3% | +87.5% | 16일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**LLY**](../snapshots/LLY-2026-07-16.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,156.63 | 🔴 -4.9% | -0.8R | -1.5% | +24.9% | 7일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**CAT**](../snapshots/CAT-2026-07-16.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $991.41 | $914.30 | 🔴 -7.8% | -1.0R | -0.2% | +34.3% | 14일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |

**합계** 23포지션 · 평균 +0.1R · 양의 R 13/23

<script type="application/json" id="pos-data">
[{"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 228.5500030517578, "r": 1.4380435571946657}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1152.0699462890625, "r": 1.2092981408085048}, {"ticker": "GOOGL", "entry": 355.5, "stop": 334.78411647226744, "current": 370.9200134277344, "r": 0.7443570247482542}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 327.5, "r": 0.5583900367808238}, {"ticker": "NVDA", "entry": 207.3699951171875, "stop": 193.26880716964297, "current": 212.5, "r": 0.3637994828446917}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 32.20000076293945, "r": 0.33930830412270974}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1413000.0, "r": 0.32307978660762965}, {"ticker": "066570", "entry": 185600.0, "stop": 141564.11742172934, "current": 194000.0, "r": 0.19075352889929245}, {"ticker": "278470", "entry": 375000.0, "stop": 314981.3971592858, "current": 385500.0, "r": 0.1749457585320067}, {"ticker": "AVGO", "entry": 391.8500061035156, "stop": 356.8287411224586, "current": 394.2799987792969, "r": 0.0693862051269602}, {"ticker": "161890", "entry": 106500.0, "stop": 91763.98947207628, "current": 107200.0, "r": 0.047502680503216835}, {"ticker": "CORZ", "entry": 22.6299991607666, "stop": 19.081676322606583, "current": 22.719999313354492, "r": 0.025364138691100657}, {"ticker": "USD", "entry": 92.19000244140625, "stop": 76.43252202238607, "current": 92.30000305175781, "r": 0.00698085020107564}, {"ticker": "SKWD", "entry": 56.869998931884766, "stop": 52.767579521513646, "current": 56.869998931884766, "r": 0.0}, {"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 82.44999694824219, "r": -0.06516392720290033}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 180.8800048828125, "r": -0.20707842144322924}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 529.1400146484375, "r": -0.21679312563783254}, {"ticker": "PCAR", "entry": 125.00499725341797, "stop": 118.63641278688668, "current": 123.1500015258789, "r": -0.2912728467821365}, {"ticker": "CIFR", "entry": 21.280000686645508, "stop": 16.63556842661093, "current": 19.8700008392334, "r": -0.30358928034007154}, {"ticker": "GEV", "entry": 1102.510009765625, "stop": 1002.9343461066205, "current": 1055.280029296875, "r": -0.4743124849309409}, {"ticker": "BE", "entry": 275.010009765625, "stop": 217.05686725842352, "current": 239.3800048828125, "r": -0.6148071241932218}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1156.6300048828125, "r": -0.7777748846579893}, {"ticker": "CAT", "entry": 991.4099731445312, "stop": 912.5806793261623, "current": 914.2999877929688, "r": -0.9781894726753753}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

