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
| [**KO**](../snapshots/KO-2026-08-26.md) Coca-Cola | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $82.65 | $91.64 | 🟢 +10.9% | +2.9R | -13.2% | +0.2% | 57일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**PM**](../snapshots/PM-2026-08-26.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $193.94 | 🟢 +6.1% | +1.2R | -10.7% | +9.2% | 57일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**066570**](../snapshots/066570-2026-08-26.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-05 | ₩165,500 | ₩199,800 | 🟢 +20.7% | +1.0R | -34.6% | +35.0% | 21일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**MS**](../snapshots/MS-2026-08-26.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $216.76 | 🟢 +2.4% | +0.4R | -7.7% | +13.9% | 57일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-08-26.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $206.64 | $213.05 | 🟢 +3.1% | +0.4R | -10.2% | +18.5% | 22일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**USD**](../snapshots/USD-2026-08-26.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $81.99 | 🟢 +5.7% | +0.3R | -24.7% | +52.4% | 26일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**LLY**](../snapshots/LLY-2026-08-26.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,233.66 | 🟢 +1.5% | +0.2R | -7.6% | +17.1% | 48일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-08-26.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-23 | $344.82 | $346.96 | 🟢 +0.6% | +0.1R | -6.3% | +16.6% | 3일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**009150**](../snapshots/009150-2026-08-26.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,318,000 | 🟢 +2.2% | +0.1R | -31.3% | +85.2% | 44일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**BE**](../snapshots/BE-2026-08-26.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-26 | $217.62 | $217.62 | ⚪ +0.0% | +0.0R | -21.6% | +64.9% | 0일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-08-26.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $514.06 | 🔴 -2.8% | -0.2R | -9.5% | +40.1% | 39일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**GS**](../snapshots/GS-2026-08-26.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-25 | $1,076.91 | $1,059.11 | 🔴 -1.7% | -0.3R | -4.2% | +19.3% | 62일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-08-26.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $309.90 | 🔴 -2.8% | -0.6R | -2.2% | +18.1% | 44일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**DLR**](../snapshots/DLR-2026-08-26.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $192.24 | 🔴 -3.4% | -0.6R | -2.4% | +21.4% | 32일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-08-26.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-30 | $133.87 | $129.22 | 🔴 -3.5% | -0.7R | -1.9% | +20.0% | 27일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**AMD**](../snapshots/AMD-2026-08-26.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $479.18 | 🔴 -11.9% | -0.9R | -0.8% | +56.4% | 44일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-08-26.md) Skyward Specialty Insurance | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-08 | $63.67 | $57.40 | 🔴 -9.8% | -1.5R | +3.4% | +33.4% | 18일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |

**합계** 17포지션 · 평균 +0.1R · 양의 R 9/17

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 91.63999938964844, "r": 2.9290507910922745}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 193.94000244140625, "r": 1.1519451716224982}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 199800.0, "r": 0.987347776633063}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 216.7550048828125, "r": 0.43021709976214484}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 213.0500030517578, "r": 0.41872454398467496}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 81.98999786376953, "r": 0.28079776670852497}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1233.6600341796875, "r": 0.23425335127139746}, {"ticker": "GOOGL", "entry": 344.82000732421875, "stop": 324.9343848096383, "current": 346.9599914550781, "r": 0.10761464114539557}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1318000.0, "r": 0.07555898235178436}, {"ticker": "BE", "entry": 217.6199951171875, "stop": 170.5670352691636, "current": 217.6199951171875, "r": 0.0}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 514.0599975585938, "r": -0.2349599103856174}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1059.1065673828125, "r": -0.2864518956072781}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 309.8999938964844, "r": -0.562212057493648}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 192.24000549316406, "r": -0.5976879533676043}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 129.22000122070312, "r": -0.6564027936762978}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 479.17999267578125, "r": -0.946399774043472}, {"ticker": "SKWD", "entry": 63.66999816894531, "stop": 59.36272420763139, "current": 57.400001525878906, "r": -1.4556763046374133}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

