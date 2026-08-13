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
| [**KO**](../snapshots/KO-2026-08-14.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $87.44 | 🟢 +5.8% | +1.6R | -9.0% | +5.1% | 45일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-08-14.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $206.64 | $225.30 | 🟢 +9.0% | +1.2R | -15.1% | +12.1% | 10일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**278470**](../snapshots/278470-2026-08-14.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | ₩338,000 | ₩397,000 | 🟢 +17.5% | +1.1R | -27.8% | +24.0% | 10일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**066570**](../snapshots/066570-2026-08-14.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-05 | ₩165,500 | ₩205,000 | 🟢 +23.9% | +1.1R | -36.2% | +31.6% | 9일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**USD**](../snapshots/USD-2026-08-14.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $95.36 | 🟢 +23.0% | +1.1R | -35.3% | +31.1% | 14일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**AVGO**](../snapshots/AVGO-2026-08-14.md) Broadcom | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $392.23 | $417.82 | 🟢 +6.5% | +0.8R | -14.2% | +18.1% | 10일 | <span class="js-shares" data-ticker="AVGO">—</span> | <span class="js-pnl" data-ticker="AVGO">—</span> |
| [**PM**](../snapshots/PM-2026-08-14.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $188.92 | 🟢 +3.3% | +0.6R | -8.3% | +12.1% | 45일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**MS**](../snapshots/MS-2026-08-14.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $218.33 | 🟢 +3.1% | +0.6R | -8.4% | +13.1% | 45일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**CAT**](../snapshots/CAT-2026-08-14.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $808.91 | $854.60 | 🟢 +5.6% | +0.6R | -14.8% | +23.1% | 14일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |
| [**GEV**](../snapshots/GEV-2026-08-14.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $982.55 | $1,048.79 | 🟢 +6.7% | +0.5R | -18.1% | +29.0% | 14일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**KMI**](../snapshots/KMI-2026-08-14.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-11 | $31.39 | $32.10 | 🟢 +2.3% | +0.5R | -6.5% | +10.7% | 3일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**BE**](../snapshots/BE-2026-08-14.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $207.21 | $236.20 | 🟢 +14.0% | +0.5R | -37.1% | +62.1% | 14일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-08-14.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $550.74 | 🟢 +4.1% | +0.3R | -15.5% | +30.7% | 27일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**009150**](../snapshots/009150-2026-08-14.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,335,000 | 🟢 +3.6% | +0.1R | -32.2% | +82.8% | 32일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**LLY**](../snapshots/LLY-2026-08-14.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,209.28 | 🔴 -0.5% | -0.1R | -5.8% | +19.4% | 36일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**DLR**](../snapshots/DLR-2026-08-14.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $197.60 | 🔴 -0.7% | -0.1R | -5.0% | +18.1% | 20일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**RDW**](../snapshots/RDW-2026-08-14.md) RedWire | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-08 | $13.59 | $13.19 | 🔴 -3.0% | -0.2R | -14.4% | +55.5% | 6일 | <span class="js-shares" data-ticker="RDW">—</span> | <span class="js-pnl" data-ticker="RDW">—</span> |
| [**BA**](../snapshots/BA-2026-08-14.md) Boeing | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $233.49 | $230.32 | 🔴 -1.4% | -0.2R | -5.3% | +21.4% | 10일 | <span class="js-shares" data-ticker="BA">—</span> | <span class="js-pnl" data-ticker="BA">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-08-14.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-01 | $356.13 | $346.36 | 🔴 -2.7% | -0.4R | -4.1% | +23.4% | 13일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-08-14.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-30 | $133.87 | $130.72 | 🔴 -2.4% | -0.4R | -3.0% | +18.7% | 15일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**GS**](../snapshots/GS-2026-08-14.md) Goldman Sachs | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-25 | $1,076.91 | $1,042.48 | 🔴 -3.2% | -0.6R | -2.7% | +21.2% | 50일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-08-14.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $305.26 | 🔴 -4.2% | -0.9R | -0.7% | +19.8% | 32일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**AMD**](../snapshots/AMD-2026-08-14.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $483.01 | 🔴 -11.2% | -0.9R | -1.6% | +55.2% | 32일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-08-14.md) Skyward Specialty Insurance | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 08-08 | $63.67 | $58.98 | 🔴 -7.4% | -1.1R | +0.6% | +29.9% | 6일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |

**합계** 24포지션 · 평균 +0.2R · 양의 R 14/24

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 87.44000244140625, "r": 1.5606406345768808}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 225.3000030517578, "r": 1.218938698951993}, {"ticker": "278470", "entry": 338000.0, "stop": 286622.8624105194, "current": 397000.0, "r": 1.1483707105566767}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 205000.0, "r": 1.137033153848571}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 95.36000061035156, "r": 1.1263543655519495}, {"ticker": "AVGO", "entry": 392.2300109863281, "stop": 358.4747922503201, "current": 417.82000732421875, "r": 0.7581048885514333}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 188.9199981689453, "r": 0.6295634320427731}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 218.3300018310547, "r": 0.5647930930838878}, {"ticker": "CAT", "entry": 808.905029296875, "stop": 727.7539578057504, "current": 854.5999755859375, "r": 0.5630849408323596}, {"ticker": "GEV", "entry": 982.5499877929688, "stop": 859.1024131708681, "current": 1048.7900390625, "r": 0.5365844689319021}, {"ticker": "KMI", "entry": 31.389999389648438, "stop": 30.00431157917487, "current": 32.099998474121094, "r": 0.5123802627880591}, {"ticker": "BE", "entry": 207.2100067138672, "stop": 148.66912487910352, "current": 236.1999969482422, "r": 0.49520931912507865}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 550.739990234375, "r": 0.341130673424964}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1335000.0, "r": 0.11985217890283036}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1209.280029296875, "r": -0.08605359341911335}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 197.60000610351562, "r": -0.12932398990997318}, {"ticker": "RDW", "entry": 13.59000015258789, "stop": 11.286366858996743, "current": 13.1850004196167, "r": -0.17580911601595883}, {"ticker": "BA", "entry": 233.49000549316406, "stop": 218.1540878686476, "current": 230.32000732421875, "r": -0.20670417294610766}, {"ticker": "GOOGL", "entry": 356.1300048828125, "stop": 332.3223349724717, "current": 346.3599853515625, "r": -0.4103727734819786}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 130.72000122070312, "r": -0.4446596790758988}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1042.4849853515625, "r": -0.5538876560221637}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 305.260009765625, "r": -0.8576424058616925}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 483.010009765625, "r": -0.890466933705919}, {"ticker": "SKWD", "entry": 63.66999816894531, "stop": 59.36272420763139, "current": 58.97999954223633, "r": -1.088855426618443}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

