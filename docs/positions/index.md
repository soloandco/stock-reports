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
| [**KO**](../snapshots/KO-2026-08-13.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $86.74 | 🟢 +4.9% | +1.3R | -8.2% | +5.9% | 44일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-08-13.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $206.64 | $224.09 | 🟢 +8.4% | +1.1R | -14.6% | +12.7% | 9일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**USD**](../snapshots/USD-2026-08-13.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $93.77 | 🟢 +20.9% | +1.0R | -34.2% | +33.3% | 13일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**278470**](../snapshots/278470-2026-08-13.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | ₩338,000 | ₩385,500 | 🟢 +14.1% | +0.9R | -25.6% | +27.7% | 9일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**AVGO**](../snapshots/AVGO-2026-08-13.md) Broadcom | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $392.23 | $416.05 | 🟢 +6.1% | +0.7R | -13.8% | +18.6% | 9일 | <span class="js-shares" data-ticker="AVGO">—</span> | <span class="js-pnl" data-ticker="AVGO">—</span> |
| [**CAT**](../snapshots/CAT-2026-08-13.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $808.91 | $855.65 | 🟢 +5.8% | +0.6R | -14.9% | +23.0% | 13일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |
| [**BE**](../snapshots/BE-2026-08-13.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $207.21 | $237.19 | 🟢 +14.5% | +0.5R | -37.3% | +61.4% | 13일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**MS**](../snapshots/MS-2026-08-13.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $217.65 | 🟢 +2.8% | +0.5R | -8.1% | +13.4% | 44일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**GEV**](../snapshots/GEV-2026-08-13.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $982.55 | $1,039.92 | 🟢 +5.8% | +0.5R | -17.4% | +30.1% | 13일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**066570**](../snapshots/066570-2026-08-13.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-05 | ₩165,500 | ₩181,200 | 🟢 +9.5% | +0.5R | -27.8% | +48.9% | 8일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**PM**](../snapshots/PM-2026-08-13.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $186.18 | 🟢 +1.8% | +0.3R | -6.9% | +13.7% | 44일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-08-13.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $546.61 | 🟢 +3.3% | +0.3R | -14.9% | +31.7% | 26일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**KMI**](../snapshots/KMI-2026-08-13.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-11 | $31.39 | $31.73 | 🟢 +1.1% | +0.2R | -5.4% | +12.0% | 2일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**LLY**](../snapshots/LLY-2026-08-13.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,220.42 | 🟢 +0.4% | +0.1R | -6.6% | +18.3% | 35일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**RDW**](../snapshots/RDW-2026-08-13.md) RedWire | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-08 | $13.59 | $13.49 | 🔴 -0.7% | -0.0R | -16.3% | +52.0% | 5일 | <span class="js-shares" data-ticker="RDW">—</span> | <span class="js-pnl" data-ticker="RDW">—</span> |
| [**009150**](../snapshots/009150-2026-08-13.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,262,000 | 🔴 -2.1% | -0.1R | -28.3% | +93.4% | 31일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**BA**](../snapshots/BA-2026-08-13.md) Boeing | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $233.49 | $231.25 | 🔴 -1.0% | -0.1R | -5.7% | +20.9% | 9일 | <span class="js-shares" data-ticker="BA">—</span> | <span class="js-pnl" data-ticker="BA">—</span> |
| [**DLR**](../snapshots/DLR-2026-08-13.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $197.12 | 🔴 -1.0% | -0.2R | -4.8% | +18.4% | 19일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-08-13.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-30 | $133.87 | $131.06 | 🔴 -2.1% | -0.4R | -3.3% | +18.4% | 14일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-08-13.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-01 | $356.13 | $343.54 | 🔴 -3.5% | -0.5R | -3.3% | +24.5% | 12일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**GS**](../snapshots/GS-2026-08-13.md) Goldman Sachs | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-25 | $1,076.91 | $1,035.66 | 🔴 -3.8% | -0.7R | -2.0% | +22.0% | 49일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-08-13.md) Skyward Specialty Insurance | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 08-08 | $63.67 | $60.13 | 🔴 -5.6% | -0.8R | -1.3% | +27.4% | 5일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |
| [**AMD**](../snapshots/AMD-2026-08-13.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $482.93 | 🔴 -11.2% | -0.9R | -1.5% | +55.2% | 31일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-08-13.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $302.25 | 🔴 -5.2% | -1.0R | +0.3% | +21.0% | 31일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |

**합계** 24포지션 · 평균 +0.2R · 양의 R 14/24

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 86.73500061035156, "r": 1.3309424519672601}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 224.08999633789062, "r": 1.1398966989485635}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 93.7699966430664, "r": 1.025798040156363}, {"ticker": "278470", "entry": 338000.0, "stop": 286622.8624105194, "current": 385500.0, "r": 0.924535741549867}, {"ticker": "AVGO", "entry": 392.2300109863281, "stop": 358.4747922503201, "current": 416.04998779296875, "r": 0.7056679736822712}, {"ticker": "CAT", "entry": 808.905029296875, "stop": 727.7539578057504, "current": 855.6500244140625, "r": 0.5760243735327626}, {"ticker": "BE", "entry": 207.2100067138672, "stop": 148.66912487910352, "current": 237.19000244140625, "r": 0.5121206717069963}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 217.64999389648438, "r": 0.5066896514463649}, {"ticker": "GEV", "entry": 982.5499877929688, "stop": 859.1024131708681, "current": 1039.9200439453125, "r": 0.4647321450256574}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 181200.0, "r": 0.4519346965929763}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 186.17999267578125, "r": 0.34443840857832675}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 546.6099853515625, "r": 0.2762654226297816}, {"ticker": "KMI", "entry": 31.389999389648438, "stop": 30.00431157917487, "current": 31.729999542236328, "r": 0.2453656227745077}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1220.4200439453125, "r": 0.06030503419396352}, {"ticker": "RDW", "entry": 13.59000015258789, "stop": 11.286366858996743, "current": 13.489999771118164, "r": -0.04340985249168516}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1262000.0, "r": -0.0703480180516613}, {"ticker": "BA", "entry": 233.49000549316406, "stop": 218.1540878686476, "current": 231.25, "r": -0.1460626972580448}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 197.1199951171875, "r": -0.1712679866374477}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 131.05999755859375, "r": -0.3966650900507718}, {"ticker": "GOOGL", "entry": 356.1300048828125, "stop": 332.3223349724717, "current": 343.5400085449219, "r": -0.5288210221875681}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1035.6600341796875, "r": -0.6636988643062642}, {"ticker": "SKWD", "entry": 63.66999816894531, "stop": 59.36272420763139, "current": 60.130001068115234, "r": -0.8218648575931793}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 482.92999267578125, "r": -0.8916354880505913}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 302.25, "r": -1.0492913875329102}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

