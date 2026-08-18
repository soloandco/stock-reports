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
| [**KO**](../snapshots/KO-2026-08-19.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $88.83 | 🟢 +7.5% | +2.0R | -10.4% | +3.4% | 50일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**066570**](../snapshots/066570-2026-08-19.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-05 | ₩165,500 | ₩215,000 | 🟢 +29.9% | +1.4R | -39.2% | +25.5% | 14일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**KMI**](../snapshots/KMI-2026-08-19.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-11 | $31.39 | $32.87 | 🟢 +4.7% | +1.1R | -8.7% | +8.1% | 8일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**278470**](../snapshots/278470-2026-08-19.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | ₩338,000 | ₩390,500 | 🟢 +15.5% | +1.0R | -26.6% | +26.0% | 15일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-08-19.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $206.64 | $219.74 | 🟢 +6.3% | +0.9R | -12.9% | +14.9% | 15일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**009150**](../snapshots/009150-2026-08-19.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,558,000 | 🟢 +20.9% | +0.7R | -41.9% | +56.6% | 37일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**USD**](../snapshots/USD-2026-08-19.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $88.29 | 🟢 +13.8% | +0.7R | -30.1% | +41.6% | 19일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**MS**](../snapshots/MS-2026-08-19.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $217.62 | 🟢 +2.8% | +0.5R | -8.1% | +13.4% | 50일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**PM**](../snapshots/PM-2026-08-19.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $187.64 | 🟢 +2.6% | +0.5R | -7.7% | +12.8% | 50일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**CAT**](../snapshots/CAT-2026-08-19.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $808.91 | $841.23 | 🟢 +4.0% | +0.4R | -13.5% | +25.1% | 19일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |
| [**GEV**](../snapshots/GEV-2026-08-19.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $982.55 | $1,004.40 | 🟢 +2.2% | +0.2R | -14.5% | +34.7% | 19일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**LLY**](../snapshots/LLY-2026-08-19.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,226.45 | 🟢 +0.9% | +0.1R | -7.1% | +17.8% | 41일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-08-19.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $531.39 | 🟢 +0.4% | +0.0R | -12.4% | +35.5% | 32일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**RDW**](../snapshots/RDW-2026-08-19.md) RedWire | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-08 | $13.59 | $12.94 | 🔴 -4.8% | -0.3R | -12.8% | +58.4% | 11일 | <span class="js-shares" data-ticker="RDW">—</span> | <span class="js-pnl" data-ticker="RDW">—</span> |
| [**DLR**](../snapshots/DLR-2026-08-19.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $195.26 | 🔴 -1.9% | -0.3R | -3.9% | +19.5% | 25일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**AVGO**](../snapshots/AVGO-2026-08-19.md) Broadcom | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $392.23 | $379.83 | 🔴 -3.2% | -0.4R | -5.6% | +29.9% | 15일 | <span class="js-shares" data-ticker="AVGO">—</span> | <span class="js-pnl" data-ticker="AVGO">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-08-19.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-01 | $356.13 | $344.20 | 🔴 -3.3% | -0.5R | -3.5% | +24.2% | 18일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-08-19.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $310.03 | 🔴 -2.7% | -0.6R | -2.3% | +18.0% | 37일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**GS**](../snapshots/GS-2026-08-19.md) Goldman Sachs | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-25 | $1,076.91 | $1,039.92 | 🔴 -3.4% | -0.6R | -2.4% | +21.5% | 55일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-08-19.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-30 | $133.87 | $128.02 | 🔴 -4.4% | -0.8R | -1.0% | +21.2% | 20일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**AMD**](../snapshots/AMD-2026-08-19.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $484.39 | 🔴 -11.0% | -0.9R | -1.8% | +54.7% | 37일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-08-19.md) Skyward Specialty Insurance | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-08 | $63.67 | $58.44 | 🔴 -8.2% | -1.2R | +1.6% | +31.1% | 11일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |

**합계** 22포지션 · 평균 +0.2R · 양의 R 13/22

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 88.83499908447266, "r": 2.015147530224957}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 215000.0, "r": 1.4248896484937787}, {"ticker": "KMI", "entry": 31.389999389648438, "stop": 30.00431157917487, "current": 32.869998931884766, "r": 1.068061312981118}, {"ticker": "278470", "entry": 338000.0, "stop": 286622.8624105194, "current": 390500.0, "r": 1.0218552932919582}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 219.74000549316406, "r": 0.8557396174850176}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1558000.0, "r": 0.7008746983665515}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 88.29000091552734, "r": 0.6792276888347079}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 217.6199951171875, "r": 0.5041263985290673}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 187.63999938964844, "r": 0.49636673484927896}, {"ticker": "CAT", "entry": 808.905029296875, "stop": 727.7539578057504, "current": 841.22998046875, "r": 0.39833055285548913}, {"ticker": "GEV", "entry": 982.5499877929688, "stop": 859.1024131708681, "current": 1004.4000244140625, "r": 0.176998508783841}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1226.449951171875, "r": 0.1395265589553915}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 531.3900146484375, "r": 0.03722279561932039}, {"ticker": "RDW", "entry": 13.59000015258789, "stop": 11.286366858996743, "current": 12.9399995803833, "r": -0.282163213221884}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 195.25999450683594, "r": -0.3337973072900309}, {"ticker": "AVGO", "entry": 392.2300109863281, "stop": 358.4747922503201, "current": 379.8299865722656, "r": -0.367351327539611}, {"ticker": "GOOGL", "entry": 356.1300048828125, "stop": 332.3223349724717, "current": 344.20001220703125, "r": -0.5010987098153394}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 310.0299987792969, "r": -0.5539345749127474}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1039.9200439453125, "r": -0.5951567153758665}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 128.02000427246094, "r": -0.8257968545641474}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 484.3900146484375, "r": -0.8703136051528749}, {"ticker": "SKWD", "entry": 63.66999816894531, "stop": 59.36272420763139, "current": 58.439998626708984, "r": -1.2142249574115616}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

