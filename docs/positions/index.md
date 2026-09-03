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
| [**KO**](../snapshots/KO-2026-09-03.md) Coca-Cola | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $82.65 | $88.24 | 🟢 +6.8% | +1.8R | -9.8% | +11.1% | 65일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-09-03.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $206.64 | $224.41 | 🟢 +8.6% | +1.2R | -14.7% | +26.2% | 30일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**066570**](../snapshots/066570-2026-09-03.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-05 | ₩165,500 | ₩199,450 | 🟢 +20.5% | +1.0R | -34.4% | +70.1% | 29일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**PM**](../snapshots/PM-2026-09-03.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $187.94 | 🟢 +2.8% | +0.5R | -7.8% | +22.9% | 65일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**USD**](../snapshots/USD-2026-09-03.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $84.17 | 🟢 +8.5% | +0.4R | -26.7% | +86.1% | 34일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-09-03.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $324.96 | 🟢 +2.0% | +0.4R | -6.8% | +22.2% | 52일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**009150**](../snapshots/009150-2026-09-03.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,340,000 | 🟢 +4.0% | +0.1R | -32.4% | +139.4% | 52일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**MS**](../snapshots/MS-2026-09-03.md) Morgan Stanley | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $211.72 | $211.82 | 🟢 +0.0% | +0.0R | -5.6% | +27.6% | 65일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**BE**](../snapshots/BE-2026-09-03.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 09-03 | $217.28 | $217.28 | ⚪ +0.0% | +0.0R | -19.1% | +95.5% | 0일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**KMI**](../snapshots/KMI-2026-09-03.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 09-01 | $32.25 | $31.97 | 🔴 -0.9% | -0.2R | -4.0% | +25.4% | 2일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**278470**](../snapshots/278470-2026-09-03.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 09-02 | ₩432,500 | ₩419,000 | 🔴 -3.1% | -0.3R | -9.4% | +66.5% | 1일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-09-03.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $501.44 | 🔴 -5.2% | -0.4R | -7.2% | +69.0% | 47일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**LLY**](../snapshots/LLY-2026-09-03.md) Eli Lilly | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-09 | $1,215.83 | $1,160.08 | 🔴 -4.6% | -0.7R | -1.8% | +37.6% | 56일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**GS**](../snapshots/GS-2026-09-03.md) Goldman Sachs | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-25 | $1,076.91 | $1,004.42 | 🔴 -6.7% | -1.2R | +1.0% | +38.2% | 70일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**AMD**](../snapshots/AMD-2026-09-03.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $457.06 | 🔴 -16.0% | -1.3R | +4.0% | +93.9% | 52일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-09-03.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-30 | $133.87 | $122.13 | 🔴 -8.8% | -1.7R | +3.8% | +38.6% | 35일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-09-03.md) Skyward Specialty Insurance | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-08 | $63.67 | $56.32 | 🔴 -11.5% | -1.7R | +5.4% | +51.3% | 26일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |

**합계** 17포지션 · 평균 -0.1R · 양의 R 8/17

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 88.23999786376953, "r": 1.8212888861395176}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 224.41000366210938, "r": 1.1608007308288133}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 199450.0, "r": 0.9772727993204806}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 187.94000244140625, "r": 0.52758505809179}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 84.16999816894531, "r": 0.41866712084858254}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 324.9599914550781, "r": 0.3966662920176928}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1340000.0, "r": 0.132879589653138}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 211.82000732421875, "r": 0.008545045584928197}, {"ticker": "BE", "entry": 217.27999877929688, "stop": 175.7639100375121, "current": 217.27999877929688, "r": 0.0}, {"ticker": "KMI", "entry": 32.25, "stop": 30.68182502661655, "current": 31.969999313354492, "r": -0.17855194184191472}, {"ticker": "278470", "entry": 432500.0, "stop": 379472.18390413764, "current": 419000.0, "r": -0.25458336763473416}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 501.44000244140625, "r": -0.43316770227396145}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1160.0799560546875, "r": -0.7324490808074016}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1004.4199829101562, "r": -1.166340962450685}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 457.05999755859375, "r": -1.2694359710458132}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 122.12999725341797, "r": -1.6572424753843937}, {"ticker": "SKWD", "entry": 63.66999816894531, "stop": 59.36272420763139, "current": 56.31999969482422, "r": -1.7064153662236503}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

