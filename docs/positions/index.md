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
| [**KO**](../snapshots/KO-2026-07-30.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $89.13 | 🟢 +7.8% | +2.1R | -10.7% | +3.1% | 30일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**PM**](../snapshots/PM-2026-07-30.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $198.43 | 🟢 +8.5% | +1.6R | -12.7% | +6.7% | 30일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-07-30.md) Apple | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-13 | $318.73 | $338.19 | 🟢 +6.1% | +1.2R | -10.4% | +8.2% | 17일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**KMI**](../snapshots/KMI-2026-07-30.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $31.86 | 🟢 +0.4% | +0.1R | -4.9% | +12.9% | 28일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-07-30.md) Paccar | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-30 | $133.87 | $133.87 | ⚪ +0.0% | +0.0R | -5.3% | +15.9% | 0일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**LLY**](../snapshots/LLY-2026-07-30.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,210.67 | 🔴 -0.4% | -0.1R | -5.9% | +19.3% | 21일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**CDNS**](../snapshots/CDNS-2026-07-30.md) Cadence Design Systems | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-28 | $338.61 | $332.76 | 🔴 -1.7% | -0.2R | -7.2% | +28.7% | 2일 | <span class="js-shares" data-ticker="CDNS">—</span> | <span class="js-pnl" data-ticker="CDNS">—</span> |
| [**009150**](../snapshots/009150-2026-07-30.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,114,000 | 🔴 -13.6% | -0.5R | -18.7% | +119.1% | 17일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**MS**](../snapshots/MS-2026-07-30.md) Morgan Stanley | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $211.72 | $203.19 | 🔴 -4.0% | -0.7R | -1.6% | +21.5% | 30일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**DLR**](../snapshots/DLR-2026-07-30.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $188.23 | 🔴 -5.5% | -0.9R | -0.3% | +24.0% | 5일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-07-30.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $465.00 | 🔴 -12.1% | -1.0R | +0.1% | +54.8% | 12일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**GS**](../snapshots/GS-2026-07-30.md) Goldman Sachs | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-25 | $1,076.91 | $980.76 | 🔴 -8.9% | -1.5R | +3.5% | +28.8% | 35일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**AMD**](../snapshots/AMD-2026-07-30.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $429.56 | 🔴 -21.0% | -1.7R | +10.7% | +74.5% | 17일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |

**합계** 13포지션 · 평균 -0.1R · 양의 R 4/13

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 89.12999725341797, "r": 2.1112615263808734}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 198.4250030517578, "r": 1.6186544199998976}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 338.19000244140625, "r": 1.2390283873122017}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 31.860000610351562, "r": 0.09896554000020273}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 133.8699951171875, "r": 0.0}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1210.6700439453125, "r": -0.0677914418216807}, {"ticker": "CDNS", "entry": 338.6099853515625, "stop": 308.74442908515095, "current": 332.760009765625, "r": -0.19587700070789257}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1114000.0, "r": -0.45595937626076766}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 203.19000244140625, "r": -0.7288477987454579}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 188.22999572753906, "r": -0.9480879260289401}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 465.0, "r": -1.005489034671327}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 980.760009765625, "r": -1.5470221092517056}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 429.55999755859375, "r": -1.6710407349936047}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

