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
| [**KO**](../snapshots/KO-2026-08-11.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $86.88 | 🟢 +5.1% | +1.4R | -8.4% | +5.7% | 42일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**278470**](../snapshots/278470-2026-08-11.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | ₩338,000 | ₩384,500 | 🟢 +13.8% | +0.9R | -25.5% | +28.0% | 7일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**AVGO**](../snapshots/AVGO-2026-08-11.md) Broadcom | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $392.23 | $422.40 | 🟢 +7.7% | +0.9R | -15.1% | +16.8% | 7일 | <span class="js-shares" data-ticker="AVGO">—</span> | <span class="js-pnl" data-ticker="AVGO">—</span> |
| [**161890**](../snapshots/161890-2026-08-11.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | ₩95,100 | ₩106,700 | 🟢 +12.2% | +0.8R | -25.1% | +31.8% | 11일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**USD**](../snapshots/USD-2026-08-11.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $89.01 | 🟢 +14.8% | +0.7R | -30.6% | +40.4% | 11일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-08-11.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $206.64 | $217.55 | 🟢 +5.3% | +0.7R | -12.1% | +16.1% | 7일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**066570**](../snapshots/066570-2026-08-11.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-05 | ₩165,500 | ₩185,000 | 🟢 +11.8% | +0.6R | -29.3% | +45.8% | 6일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**CAT**](../snapshots/CAT-2026-08-11.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $808.91 | $837.59 | 🟢 +3.5% | +0.4R | -13.1% | +25.6% | 11일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |
| [**PM**](../snapshots/PM-2026-08-11.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $185.98 | 🟢 +1.7% | +0.3R | -6.8% | +13.8% | 42일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**MS**](../snapshots/MS-2026-08-11.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $215.22 | 🟢 +1.7% | +0.3R | -7.1% | +14.7% | 42일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**LLY**](../snapshots/LLY-2026-08-11.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,231.41 | 🟢 +1.3% | +0.2R | -7.4% | +17.3% | 33일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**GEV**](../snapshots/GEV-2026-08-11.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $982.55 | $990.49 | 🟢 +0.8% | +0.1R | -13.3% | +36.6% | 11일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-08-11.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-01 | $356.13 | $357.52 | 🟢 +0.4% | +0.1R | -7.0% | +19.6% | 10일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**BE**](../snapshots/BE-2026-08-11.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $207.21 | $210.62 | 🟢 +1.6% | +0.1R | -29.4% | +81.8% | 11일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-08-11.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $529.39 | 🟢 +0.1% | +0.0R | -12.1% | +36.0% | 24일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**KMI**](../snapshots/KMI-2026-08-11.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-11 | $31.39 | $31.39 | ⚪ +0.0% | +0.0R | -4.4% | +13.2% | 0일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**009150**](../snapshots/009150-2026-08-11.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,278,000 | 🔴 -0.9% | -0.0R | -29.2% | +91.0% | 29일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**BA**](../snapshots/BA-2026-08-11.md) Boeing | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $233.49 | $232.75 | 🔴 -0.3% | -0.0R | -6.3% | +20.1% | 7일 | <span class="js-shares" data-ticker="BA">—</span> | <span class="js-pnl" data-ticker="BA">—</span> |
| [**RDW**](../snapshots/RDW-2026-08-11.md) RedWire | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-08 | $13.59 | $13.12 | 🔴 -3.4% | -0.2R | -14.0% | +56.2% | 3일 | <span class="js-shares" data-ticker="RDW">—</span> | <span class="js-pnl" data-ticker="RDW">—</span> |
| [**CDNS**](../snapshots/CDNS-2026-08-11.md) Cadence Design Systems | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-28 | $338.61 | $331.91 | 🔴 -2.0% | -0.2R | -7.0% | +29.0% | 14일 | <span class="js-shares" data-ticker="CDNS">—</span> | <span class="js-pnl" data-ticker="CDNS">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-08-11.md) Paccar | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-30 | $133.87 | $131.24 | 🔴 -2.0% | -0.4R | -3.4% | +18.2% | 12일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-08-11.md) Skyward Specialty Insurance | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 08-08 | $63.67 | $62.00 | 🔴 -2.6% | -0.4R | -4.3% | +23.5% | 3일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-08-11.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $308.26 | 🔴 -3.3% | -0.7R | -1.7% | +18.7% | 29일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**DLR**](../snapshots/DLR-2026-08-11.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $191.26 | 🔴 -3.9% | -0.7R | -1.9% | +22.0% | 17일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**GS**](../snapshots/GS-2026-08-11.md) Goldman Sachs | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-25 | $1,076.91 | $1,033.97 | 🔴 -4.0% | -0.7R | -1.9% | +22.2% | 47일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**AMD**](../snapshots/AMD-2026-08-11.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $469.56 | 🔴 -13.7% | -1.1R | +1.3% | +59.6% | 29일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |

**합계** 26포지션 · 평균 +0.1R · 양의 R 15/26

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 86.875, "r": 1.3765559581344629}, {"ticker": "278470", "entry": 338000.0, "stop": 286622.8624105194, "current": 384500.0, "r": 0.9050718312014486}, {"ticker": "AVGO", "entry": 392.2300109863281, "stop": 358.4747922503201, "current": 422.3999938964844, "r": 0.8937872139448686}, {"ticker": "161890", "entry": 95100.0, "stop": 79921.43092159486, "current": 106700.0, "r": 0.7642354124476435}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 89.01000213623047, "r": 0.724762592221058}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 217.5500030517578, "r": 0.7126807641767511}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 185000.0, "r": 0.5613201645581553}, {"ticker": "CAT", "entry": 808.905029296875, "stop": 727.7539578057504, "current": 837.5850219726562, "r": 0.353414836659525}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 185.97999572753906, "r": 0.3236267223599455}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 215.22000122070312, "r": 0.2990583423998307}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1231.41064453125, "r": 0.20470064489694487}, {"ticker": "GEV", "entry": 982.5499877929688, "stop": 859.1024131708681, "current": 990.4949951171875, "r": 0.06435936346696249}, {"ticker": "GOOGL", "entry": 356.1300048828125, "stop": 332.3223349724717, "current": 357.5199890136719, "r": 0.05838387948480584}, {"ticker": "BE", "entry": 207.2100067138672, "stop": 148.66912487910352, "current": 210.6179962158203, "r": 0.05821554775297797}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 529.3900146484375, "r": 0.0058110890302426}, {"ticker": "KMI", "entry": 31.389999389648438, "stop": 30.00431157917487, "current": 31.389999389648438, "r": 0.0}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1278000.0, "r": -0.028660303650676823}, {"ticker": "BA", "entry": 233.49000549316406, "stop": 218.1540878686476, "current": 232.75, "r": -0.04825309520318934}, {"ticker": "RDW", "entry": 13.59000015258789, "stop": 11.286366858996743, "current": 13.125, "r": -0.20185511030837688}, {"ticker": "CDNS", "entry": 338.6099853515625, "stop": 308.74442908515095, "current": 331.9100036621094, "r": -0.22433808463793103}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 131.24000549316406, "r": -0.37125479623830326}, {"ticker": "SKWD", "entry": 63.66999816894531, "stop": 59.36272420763139, "current": 62.0, "r": -0.38771579981782334}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 308.260009765625, "r": -0.6666307514877835}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 191.25999450683594, "r": -0.6833226133529428}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1033.969970703125, "r": -0.6908914269729316}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 469.55999755859375, "r": -1.0868883510695444}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

