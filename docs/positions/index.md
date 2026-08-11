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
| [**KO**](../snapshots/KO-2026-08-12.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $86.50 | 🟢 +4.7% | +1.3R | -8.0% | +6.2% | 43일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**278470**](../snapshots/278470-2026-08-12.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | ₩338,000 | ₩387,000 | 🟢 +14.5% | +1.0R | -25.9% | +27.2% | 8일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**USD**](../snapshots/USD-2026-08-12.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $89.21 | 🟢 +15.0% | +0.7R | -30.8% | +40.1% | 12일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**161890**](../snapshots/161890-2026-08-12.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | ₩95,100 | ₩105,900 | 🟢 +11.4% | +0.7R | -24.5% | +32.8% | 12일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-08-12.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $206.64 | $217.50 | 🟢 +5.3% | +0.7R | -12.0% | +16.1% | 8일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**AVGO**](../snapshots/AVGO-2026-08-12.md) Broadcom | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $392.23 | $416.08 | 🟢 +6.1% | +0.7R | -13.8% | +18.6% | 8일 | <span class="js-shares" data-ticker="AVGO">—</span> | <span class="js-pnl" data-ticker="AVGO">—</span> |
| [**066570**](../snapshots/066570-2026-08-12.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-05 | ₩165,500 | ₩190,000 | 🟢 +14.8% | +0.7R | -31.2% | +42.0% | 7일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**CAT**](../snapshots/CAT-2026-08-12.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $808.91 | $843.22 | 🟢 +4.2% | +0.4R | -13.7% | +24.8% | 12일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |
| [**PM**](../snapshots/PM-2026-08-12.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $186.30 | 🟢 +1.9% | +0.4R | -7.0% | +13.6% | 43일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**MS**](../snapshots/MS-2026-08-12.md) Morgan Stanley | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $211.72 | $215.10 | 🟢 +1.6% | +0.3R | -7.0% | +14.8% | 43일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**GEV**](../snapshots/GEV-2026-08-12.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $982.55 | $1,011.69 | 🟢 +3.0% | +0.2R | -15.1% | +33.7% | 12일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-08-12.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $534.20 | 🟢 +1.0% | +0.1R | -12.9% | +34.8% | 25일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**BE**](../snapshots/BE-2026-08-12.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $207.21 | $211.49 | 🟢 +2.1% | +0.1R | -29.7% | +81.0% | 12일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**KMI**](../snapshots/KMI-2026-08-12.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-11 | $31.39 | $31.49 | 🟢 +0.3% | +0.1R | -4.7% | +12.9% | 1일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**LLY**](../snapshots/LLY-2026-08-12.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,214.65 | 🔴 -0.1% | -0.0R | -6.2% | +18.9% | 34일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**BA**](../snapshots/BA-2026-08-12.md) Boeing | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $233.49 | $233.22 | 🔴 -0.1% | -0.0R | -6.5% | +19.8% | 8일 | <span class="js-shares" data-ticker="BA">—</span> | <span class="js-pnl" data-ticker="BA">—</span> |
| [**RDW**](../snapshots/RDW-2026-08-12.md) RedWire | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-08 | $13.59 | $13.52 | 🔴 -0.5% | -0.0R | -16.5% | +51.6% | 4일 | <span class="js-shares" data-ticker="RDW">—</span> | <span class="js-pnl" data-ticker="RDW">—</span> |
| [**009150**](../snapshots/009150-2026-08-12.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,274,000 | 🔴 -1.2% | -0.0R | -28.9% | +91.6% | 30일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-08-12.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-30 | $133.87 | $132.53 | 🔴 -1.0% | -0.2R | -4.3% | +17.0% | 13일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-08-12.md) Skyward Specialty Insurance | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 08-08 | $63.67 | $61.66 | 🔴 -3.2% | -0.5R | -3.7% | +24.2% | 4일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-08-12.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-01 | $356.13 | $343.80 | 🔴 -3.5% | -0.5R | -3.3% | +24.4% | 11일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**GS**](../snapshots/GS-2026-08-12.md) Goldman Sachs | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-25 | $1,076.91 | $1,034.13 | 🔴 -4.0% | -0.7R | -1.9% | +22.2% | 48일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**DLR**](../snapshots/DLR-2026-08-12.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $190.83 | 🔴 -4.1% | -0.7R | -1.7% | +22.3% | 18일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-08-12.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $304.91 | 🔴 -4.3% | -0.9R | -0.6% | +20.0% | 30일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**AMD**](../snapshots/AMD-2026-08-12.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $474.32 | 🔴 -12.8% | -1.0R | +0.3% | +58.0% | 30일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |

**합계** 25포지션 · 평균 +0.1R · 양의 R 14/25

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 86.50499725341797, "r": 1.2560045571213385}, {"ticker": "278470", "entry": 338000.0, "stop": 286622.8624105194, "current": 387000.0, "r": 0.9537316070724943}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 89.21499633789062, "r": 0.7377270024178096}, {"ticker": "161890", "entry": 95100.0, "stop": 79921.43092159486, "current": 105900.0, "r": 0.7115295219340129}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 217.5, "r": 0.7094143846005743}, {"ticker": "AVGO", "entry": 392.2300109863281, "stop": 358.4747922503201, "current": 416.0799865722656, "r": 0.7065566889808296}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 190000.0, "r": 0.7052484118807593}, {"ticker": "CAT", "entry": 808.905029296875, "stop": 727.7539578057504, "current": 843.219970703125, "r": 0.4228525979475572}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 186.3000030517578, "r": 0.3569266905732583}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 215.10000610351562, "r": 0.2888053307306401}, {"ticker": "GEV", "entry": 982.5499877929688, "stop": 859.1024131708681, "current": 1011.6900024414062, "r": 0.23605173886681285}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 534.2000122070312, "r": 0.08135620503260628}, {"ticker": "BE", "entry": 207.2100067138672, "stop": 148.66912487910352, "current": 211.48500061035156, "r": 0.07302578578421295}, {"ticker": "KMI", "entry": 31.389999389648438, "stop": 30.00431157917487, "current": 31.489999771118164, "r": 0.07216660254487689}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1214.6500244140625, "r": -0.015502060010607185}, {"ticker": "BA", "entry": 233.49000549316406, "stop": 218.1540878686476, "current": 233.22000122070312, "r": -0.01760600696167671}, {"ticker": "RDW", "entry": 13.59000015258789, "stop": 11.286366858996743, "current": 13.520000457763672, "r": -0.030386648351958753}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1274000.0, "r": -0.039082232250922944}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 132.52999877929688, "r": -0.18915666542539303}, {"ticker": "SKWD", "entry": 63.66999816894531, "stop": 59.36272420763139, "current": 61.65999984741211, "r": -0.4666520726534092}, {"ticker": "GOOGL", "entry": 356.1300048828125, "stop": 332.3223349724717, "current": 343.79998779296875, "r": -0.5179010434989374}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1034.1300048828125, "r": -0.6883165299230218}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 190.8300018310547, "r": -0.7208959437547557}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 304.9100036621094, "r": -0.8799274874861875}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 474.32000732421875, "r": -1.017374074767253}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

