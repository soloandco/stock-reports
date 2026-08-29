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
| [**KO**](../snapshots/KO-2026-08-29.md) Coca-Cola | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $82.65 | $89.66 | 🟢 +8.5% | +2.3R | -11.2% | +2.5% | 60일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**066570**](../snapshots/066570-2026-08-29.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-05 | ₩165,500 | ₩198,300 | 🟢 +19.8% | +0.9R | -34.1% | +36.0% | 24일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**PM**](../snapshots/PM-2026-08-29.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $191.89 | 🟢 +4.9% | +0.9R | -9.7% | +10.3% | 60일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-08-29.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $206.64 | $217.55 | 🟢 +5.3% | +0.7R | -12.1% | +16.1% | 25일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**USD**](../snapshots/USD-2026-08-29.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $82.82 | 🟢 +6.8% | +0.3R | -25.5% | +50.9% | 29일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**MS**](../snapshots/MS-2026-08-29.md) Morgan Stanley | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $211.72 | $214.77 | 🟢 +1.4% | +0.3R | -6.9% | +14.9% | 60일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**009150**](../snapshots/009150-2026-08-29.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,385,000 | 🟢 +7.4% | +0.3R | -34.6% | +76.2% | 47일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-08-29.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $319.70 | 🟢 +0.3% | +0.1R | -5.2% | +14.4% | 47일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-08-29.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-29 | $346.59 | $346.59 | ⚪ +0.0% | +0.0R | -5.3% | +15.9% | 0일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-08-29.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $508.62 | 🔴 -3.9% | -0.3R | -8.5% | +41.6% | 42일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**LLY**](../snapshots/LLY-2026-08-29.md) Eli Lilly | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-09 | $1,215.83 | $1,174.61 | 🔴 -3.4% | -0.5R | -3.0% | +22.9% | 51일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**GS**](../snapshots/GS-2026-08-29.md) Goldman Sachs | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-25 | $1,076.91 | $1,033.99 | 🔴 -4.0% | -0.7R | -1.9% | +22.2% | 65일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**AMD**](../snapshots/AMD-2026-08-29.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $465.58 | 🔴 -14.4% | -1.1R | +2.1% | +61.0% | 47일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**DLR**](../snapshots/DLR-2026-08-29.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $185.47 | 🔴 -6.8% | -1.2R | +1.2% | +25.8% | 35일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-08-29.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-30 | $133.87 | $125.34 | 🔴 -6.4% | -1.2R | +1.2% | +23.8% | 30일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-08-29.md) Skyward Specialty Insurance | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-08 | $63.67 | $58.29 | 🔴 -8.4% | -1.2R | +1.8% | +31.4% | 21일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |

**합계** 16포지션 · 평균 -0.0R · 양의 R 8/16

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 89.66000366210938, "r": 2.283944069156318}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 198300.0, "r": 0.9441693024362817}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 191.88999938964844, "r": 0.9386218152668638}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 217.5500030517578, "r": 0.7126807641767511}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 82.81999969482422, "r": 0.3332894182513663}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 214.77000427246094, "r": 0.2606082448494618}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1385000.0, "r": 0.25012628640590684}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 319.70001220703125, "r": 0.06176051263707171}, {"ticker": "GOOGL", "entry": 346.5899963378906, "stop": 328.2404029184531, "current": 346.5899963378906, "r": 0.0}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 508.6199951171875, "r": -0.32039979065227736}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1174.6099853515625, "r": -0.5415521013885548}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1033.989990234375, "r": -0.6905693193328208}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 465.5799865722656, "r": -1.1450116737122324}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 185.47000122070312, "r": -1.1892599072123868}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 125.33999633789062, "r": -1.204112339377281}, {"ticker": "SKWD", "entry": 63.66999816894531, "stop": 59.36272420763139, "current": 58.290000915527344, "r": -1.2490492366491617}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

