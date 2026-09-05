# 오픈 포지션

현재 **매수** 판정인 종목의 진입가 대비 현재 수익률·R-배수. 진입가 = 비매수→매수로 전환된 **첫 스냅샷 가격**, 현재가 = **최신 스냅샷 가격**입니다.

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
| [**KO**](../snapshots/KO-2026-09-06.md) Coca-Cola | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 06-30 | $82.65 | $88.07 | 🟢 +6.6% | +1.8R | -9.6% | +11.3% | 68일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-09-06.md) NVIDIA | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 08-04 | $206.64 | $230.36 | 🟢 +11.5% | +1.5R | -16.9% | +22.9% | 33일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**066570**](../snapshots/066570-2026-09-05.md)  | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 08-05 | ₩165,500 | ₩201,500 | 🟢 +21.8% | +1.0R | -35.1% | +68.3% | 31일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**BE**](../snapshots/BE-2026-09-06.md) Bloom Energy | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-03 | $217.28 | $252.87 | 🟢 +16.4% | +0.9R | -30.5% | +68.0% | 3일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**USD**](../snapshots/USD-2026-09-06.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-31 | $77.55 | $88.80 | 🟢 +14.5% | +0.7R | -30.5% | +76.4% | 37일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**MS**](../snapshots/MS-2026-09-06.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 06-30 | $211.72 | $217.72 | 🟢 +2.8% | +0.5R | -8.1% | +24.1% | 68일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**009150**](../snapshots/009150-2026-09-05.md)  | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-13 | ₩1,289,000 | ₩1,401,000 | 🟢 +8.7% | +0.3R | -35.4% | +129.0% | 54일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-09-06.md) Apple | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-13 | $318.73 | $319.97 | 🟢 +0.4% | +0.1R | -5.3% | +24.2% | 55일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**DLR**](../snapshots/DLR-2026-09-06.md) Digital Realty | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-04 | $187.79 | $188.39 | 🟢 +0.3% | +0.1R | -6.0% | +28.3% | 2일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**PM**](../snapshots/PM-2026-09-06.md) Philip Morris | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 06-30 | $182.87 | $182.53 | 🔴 -0.2% | -0.0R | -5.1% | +26.5% | 68일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-09-06.md) SOXX 반도체 ETF | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-18 | $529.02 | $519.86 | 🔴 -1.7% | -0.1R | -10.5% | +63.0% | 50일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**278470**](../snapshots/278470-2026-09-04.md)  | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-02 | ₩432,500 | ₩406,000 | 🔴 -6.1% | -0.5R | -6.5% | +71.8% | 2일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**GS**](../snapshots/GS-2026-09-06.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 06-25 | $1,076.91 | $1,038.61 | 🔴 -3.6% | -0.6R | -2.3% | +33.6% | 73일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**LLY**](../snapshots/LLY-2026-09-06.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-09 | $1,215.83 | $1,149.36 | 🔴 -5.5% | -0.9R | -0.8% | +38.9% | 59일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**AMD**](../snapshots/AMD-2026-09-06.md) Advanced Micro Devices | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-13 | $543.98 | $477.57 | 🔴 -12.2% | -1.0R | -0.4% | +85.6% | 55일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-09-06.md) Paccar | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-30 | $133.87 | $124.70 | 🔴 -6.8% | -1.3R | +1.7% | +35.8% | 38일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-09-06.md) Skyward Specialty Insurance | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 08-08 | $63.67 | $57.34 | 🔴 -9.9% | -1.5R | +3.5% | +48.6% | 29일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |

**합계** 17포지션 · 평균 +0.1R · 양의 R 9/17

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 88.06999969482422, "r": 1.7659014123292935}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 230.36000061035156, "r": 1.5494759781754046}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 201500.0, "r": 1.0362833807227483}, {"ticker": "BE", "entry": 217.27999877929688, "stop": 175.7639100375121, "current": 252.8699951171875, "r": 0.8572579309974903}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 88.80000305175781, "r": 0.7114816591507693}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 217.72000122070312, "r": 0.5126714441139955}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1401000.0, "r": 0.2918140008068913}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 319.9700012207031, "r": 0.0789508620251533}, {"ticker": "DLR", "entry": 187.7899932861328, "stop": 177.01335135985073, "current": 188.38999938964844, "r": 0.05567653705300625}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 182.52999877929688, "r": -0.035380025354235935}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 519.8599853515625, "r": -0.14386615299913377}, {"ticker": "278470", "entry": 432500.0, "stop": 379472.18390413764, "current": 406000.0, "r": -0.499737721653367}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1038.6099853515625, "r": -0.6162351250933583}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1149.3599853515625, "r": -0.8732891290188128}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 477.57000732421875, "r": -0.9699116935734232}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 124.69999694824219, "r": -1.2944559821149573}, {"ticker": "SKWD", "entry": 63.66999816894531, "stop": 59.36272420763139, "current": 57.34000015258789, "r": -1.4696065477168927}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

