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
| [**PM**](../snapshots/PM-2026-07-23.md) Philip Morris | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $182.87 | $194.39 | 🟢 +6.3% | +1.2R | -10.9% | +8.9% | 23일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-07-23.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $125.00 | $131.11 | 🟢 +4.9% | +1.0R | -9.5% | +9.9% | 10일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**CIFR**](../snapshots/CIFR-2026-07-23.md) Cipher Mining | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-21 | $20.54 | $24.46 | 🟢 +19.1% | +0.8R | -35.5% | +42.5% | 2일 | <span class="js-shares" data-ticker="CIFR">—</span> | <span class="js-pnl" data-ticker="CIFR">—</span> |
| [**MS**](../snapshots/MS-2026-07-23.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $218.54 | 🟢 +3.2% | +0.6R | -8.5% | +12.9% | 23일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**KMI**](../snapshots/KMI-2026-07-23.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $32.47 | 🟢 +2.4% | +0.5R | -6.7% | +10.7% | 21일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-07-23.md) Apple | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-13 | $318.73 | $325.89 | 🟢 +2.2% | +0.5R | -7.0% | +12.3% | 10일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-07-23.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $555.52 | 🟢 +5.0% | +0.4R | -16.2% | +29.6% | 5일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**GS**](../snapshots/GS-2026-07-23.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-25 | $1,076.91 | $1,098.20 | 🟢 +2.0% | +0.3R | -7.6% | +15.0% | 28일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-07-23.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-22 | $207.29 | $212.06 | 🟢 +2.3% | +0.3R | -9.1% | +18.2% | 1일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**AMD**](../snapshots/AMD-2026-07-23.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $552.33 | 🟢 +1.5% | +0.1R | -13.9% | +35.7% | 10일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**009150**](../snapshots/009150-2026-07-23.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,310,000 | 🟢 +1.6% | +0.1R | -30.9% | +86.3% | 10일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**USD**](../snapshots/USD-2026-07-23.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $92.19 | $92.49 | 🟢 +0.3% | +0.0R | -17.4% | +50.8% | 10일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**CDNS**](../snapshots/CDNS-2026-07-23.md) Cadence Design Systems | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-23 | $337.01 | $337.01 | ⚪ +0.0% | +0.0R | -9.1% | +27.3% | 0일 | <span class="js-shares" data-ticker="CDNS">—</span> | <span class="js-pnl" data-ticker="CDNS">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-07-23.md) Skyward Specialty Insurance | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-23 | $57.93 | $57.93 | ⚪ +0.0% | +0.0R | -7.4% | +22.1% | 0일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |
| [**CORZ**](../snapshots/CORZ-2026-07-23.md) Core Scientific | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-22 | $24.01 | $23.62 | 🔴 -1.6% | -0.1R | -13.6% | +47.4% | 1일 | <span class="js-shares" data-ticker="CORZ">—</span> | <span class="js-pnl" data-ticker="CORZ">—</span> |
| [**KO**](../snapshots/KO-2026-07-23.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $82.21 | 🔴 -0.5% | -0.1R | -3.2% | +11.7% | 23일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**278470**](../snapshots/278470-2026-07-23.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩375,000 | ₩365,000 | 🔴 -2.7% | -0.2R | -13.7% | +52.1% | 10일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**066570**](../snapshots/066570-2026-07-23.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩185,600 | ₩173,200 | 🔴 -6.7% | -0.3R | -18.3% | +83.4% | 10일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**161890**](../snapshots/161890-2026-07-23.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-14 | ₩106,500 | ₩101,700 | 🔴 -4.5% | -0.3R | -9.8% | +48.2% | 9일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-07-23.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $355.50 | $342.09 | 🔴 -3.8% | -0.6R | -2.1% | +22.1% | 10일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**LLY**](../snapshots/LLY-2026-07-23.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,163.08 | 🔴 -4.3% | -0.7R | -2.0% | +24.2% | 14일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**BE**](../snapshots/BE-2026-07-23.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $275.01 | $218.22 | 🔴 -20.7% | -1.0R | -0.5% | +105.7% | 23일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**GEV**](../snapshots/GEV-2026-07-23.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $1,102.51 | $987.08 | 🔴 -10.5% | -1.2R | +1.6% | +42.0% | 23일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**CAT**](../snapshots/CAT-2026-07-23.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $991.41 | $889.38 | 🔴 -10.3% | -1.3R | +2.6% | +38.1% | 21일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |

**합계** 24포지션 · 평균 +0.0R · 양의 R 12/24

<script type="application/json" id="pos-data">
[{"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 194.38999938964844, "r": 1.1987718625713255}, {"ticker": "PCAR", "entry": 125.00499725341797, "stop": 118.63641278688668, "current": 131.11000061035156, "r": 0.9586122927342978}, {"ticker": "CIFR", "entry": 20.540000915527344, "stop": 15.765568272066863, "current": 24.459999084472656, "r": 0.8210395792921106}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 218.5399932861328, "r": 0.5827358635049714}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 32.474998474121094, "r": 0.5337014816836316}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 325.8900146484375, "r": 0.4558813816075862}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 555.52001953125, "r": 0.4162051123052807}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1098.199951171875, "r": 0.3425477267609571}, {"ticker": "NVDA", "entry": 207.2899932861328, "stop": 192.84901769421657, "current": 212.05999755859375, "r": 0.3303103894955052}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 552.3300170898438, "r": 0.1218692545959734}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1310000.0, "r": 0.05471512515129212}, {"ticker": "USD", "entry": 92.19000244140625, "stop": 76.43252202238607, "current": 92.48999786376953, "r": 0.019038286222534}, {"ticker": "CDNS", "entry": 337.010009765625, "stop": 306.30955949252694, "current": 337.010009765625, "r": 0.0}, {"ticker": "SKWD", "entry": 57.93000030517578, "stop": 53.66446092219317, "current": 57.93000030517578, "r": 0.0}, {"ticker": "CORZ", "entry": 24.010000228881836, "stop": 20.41172026954609, "current": 23.6200008392334, "r": -0.10838494893555552}, {"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 82.20500183105469, "r": -0.14498632012067778}, {"ticker": "278470", "entry": 375000.0, "stop": 314981.3971592858, "current": 365000.0, "r": -0.16661500812572066}, {"ticker": "066570", "entry": 185600.0, "stop": 141564.11742172934, "current": 173200.0, "r": -0.28158854266086025}, {"ticker": "161890", "entry": 106500.0, "stop": 91763.98947207628, "current": 101700.0, "r": -0.3257326663077726}, {"ticker": "GOOGL", "entry": 355.5, "stop": 334.78411647226744, "current": 342.0899963378906, "r": -0.6473295548392745}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1163.0799560546875, "r": -0.6930347804948956}, {"ticker": "BE", "entry": 275.010009765625, "stop": 217.05686725842352, "current": 218.22000122070312, "r": -0.9799297516586772}, {"ticker": "GEV", "entry": 1102.510009765625, "stop": 1002.9343461066205, "current": 987.0789794921875, "r": -1.1592293340743327}, {"ticker": "CAT", "entry": 991.4099731445312, "stop": 912.5806793261623, "current": 889.3800048828125, "r": -1.2943153911388152}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

