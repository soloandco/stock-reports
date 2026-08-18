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
| [**066570**](../snapshots/066570-2026-08-18.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-05 | ₩165,500 | ₩215,000 | 🟢 +29.9% | +1.4R | -39.2% | +25.5% | 13일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**KO**](../snapshots/KO-2026-08-18.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $86.99 | 🟢 +5.2% | +1.4R | -8.5% | +5.6% | 49일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-08-18.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $206.64 | $225.01 | 🟢 +8.9% | +1.2R | -15.0% | +12.2% | 14일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**USD**](../snapshots/USD-2026-08-18.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $95.50 | 🟢 +23.1% | +1.1R | -35.4% | +30.9% | 18일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**278470**](../snapshots/278470-2026-08-18.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | ₩338,000 | ₩390,500 | 🟢 +15.5% | +1.0R | -26.6% | +26.0% | 14일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**CAT**](../snapshots/CAT-2026-08-18.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $808.91 | $881.68 | 🟢 +9.0% | +0.9R | -17.5% | +19.4% | 18일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |
| [**GEV**](../snapshots/GEV-2026-08-18.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $982.55 | $1,079.37 | 🟢 +9.9% | +0.8R | -20.4% | +25.3% | 18일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**009150**](../snapshots/009150-2026-08-18.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,558,000 | 🟢 +20.9% | +0.7R | -41.9% | +56.6% | 36일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**KMI**](../snapshots/KMI-2026-08-18.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-11 | $31.39 | $32.34 | 🟢 +3.0% | +0.7R | -7.2% | +9.9% | 7일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**MS**](../snapshots/MS-2026-08-18.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $218.25 | 🟢 +3.1% | +0.6R | -8.4% | +13.1% | 49일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-08-18.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $559.12 | 🟢 +5.7% | +0.5R | -16.8% | +28.8% | 31일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**BE**](../snapshots/BE-2026-08-18.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $207.21 | $232.18 | 🟢 +12.1% | +0.4R | -36.0% | +64.9% | 18일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**PM**](../snapshots/PM-2026-08-18.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $184.51 | 🟢 +0.9% | +0.2R | -6.1% | +14.7% | 49일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**AVGO**](../snapshots/AVGO-2026-08-18.md) Broadcom | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $392.23 | $392.43 | 🟢 +0.1% | +0.0R | -8.7% | +25.8% | 14일 | <span class="js-shares" data-ticker="AVGO">—</span> | <span class="js-pnl" data-ticker="AVGO">—</span> |
| [**RDW**](../snapshots/RDW-2026-08-18.md) RedWire | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-08 | $13.59 | $13.40 | 🔴 -1.4% | -0.1R | -15.8% | +53.0% | 10일 | <span class="js-shares" data-ticker="RDW">—</span> | <span class="js-pnl" data-ticker="RDW">—</span> |
| [**DLR**](../snapshots/DLR-2026-08-18.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $197.96 | 🔴 -0.6% | -0.1R | -5.2% | +17.9% | 24일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**BA**](../snapshots/BA-2026-08-18.md) Boeing | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $233.49 | $231.67 | 🔴 -0.8% | -0.1R | -5.8% | +20.6% | 14일 | <span class="js-shares" data-ticker="BA">—</span> | <span class="js-pnl" data-ticker="BA">—</span> |
| [**LLY**](../snapshots/LLY-2026-08-18.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,184.91 | 🔴 -2.5% | -0.4R | -3.8% | +21.9% | 40일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**GS**](../snapshots/GS-2026-08-18.md) Goldman Sachs | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-25 | $1,076.91 | $1,051.06 | 🔴 -2.4% | -0.4R | -3.5% | +20.2% | 54일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-08-18.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-30 | $133.87 | $130.84 | 🔴 -2.3% | -0.4R | -3.1% | +18.6% | 19일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-08-18.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-01 | $356.13 | $344.00 | 🔴 -3.4% | -0.5R | -3.4% | +24.3% | 17일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**AMD**](../snapshots/AMD-2026-08-18.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $506.00 | 🔴 -7.0% | -0.6R | -6.0% | +48.1% | 36일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-08-18.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $305.59 | 🔴 -4.1% | -0.8R | -0.8% | +19.7% | 36일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-08-18.md) Skyward Specialty Insurance | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-08 | $63.67 | $59.80 | 🔴 -6.1% | -0.9R | -0.7% | +28.1% | 10일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |

**합계** 24포지션 · 평균 +0.3R · 양의 R 14/24

<script type="application/json" id="pos-data">
[{"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 215000.0, "r": 1.4248896484937787}, {"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 86.98500061035156, "r": 1.4123954966586445}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 225.00999450683594, "r": 1.199994295465629}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 95.5, "r": 1.135208320932142}, {"ticker": "278470", "entry": 338000.0, "stop": 286622.8624105194, "current": 390500.0, "r": 1.0218552932919582}, {"ticker": "CAT", "entry": 808.905029296875, "stop": 727.7539578057504, "current": 881.6849975585938, "r": 0.8968454380750669}, {"ticker": "GEV", "entry": 982.5499877929688, "stop": 859.1024131708681, "current": 1079.3699951171875, "r": 0.7843006038847294}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1558000.0, "r": 0.7008746983665515}, {"ticker": "KMI", "entry": 31.389999389648438, "stop": 30.00431157917487, "current": 32.34000015258789, "r": 0.6855806594811462}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 218.25, "r": 0.557957317374126}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 559.1199951171875, "r": 0.4727458007219367}, {"ticker": "BE", "entry": 207.2100067138672, "stop": 148.66912487910352, "current": 232.17999267578125, "r": 0.4265392863809918}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 184.50999450683594, "r": 0.17065836751853175}, {"ticker": "AVGO", "entry": 392.2300109863281, "stop": 358.4747922503201, "current": 392.42999267578125, "r": 0.005924467295476198}, {"ticker": "RDW", "entry": 13.59000015258789, "stop": 11.286366858996743, "current": 13.399999618530273, "r": -0.08247863693679484}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 197.9550018310547, "r": -0.09830399233019396}, {"ticker": "BA", "entry": 233.49000549316406, "stop": 218.1540878686476, "current": 231.6699981689453, "r": -0.11867612807917215}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1184.9100341796875, "r": -0.40622902880682366}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1051.06005859375, "r": -0.4159175621510637}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 130.83999633789062, "r": -0.4277209191758181}, {"ticker": "GOOGL", "entry": 356.1300048828125, "stop": 332.3223349724717, "current": 344.0, "r": -0.5094998766571385}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 506.0, "r": -0.5547254936608935}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 305.5899963378906, "r": -0.836631978831815}, {"ticker": "SKWD", "entry": 63.66999816894531, "stop": 59.36272420763139, "current": 59.79999923706055, "r": -0.898479866069218}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

