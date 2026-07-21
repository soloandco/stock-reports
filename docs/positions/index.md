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
| [**AAPL**](../snapshots/AAPL-2026-07-22.md) Apple | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-13 | $318.73 | $327.74 | 🟢 +2.8% | +0.6R | -7.5% | +11.6% | 9일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**PM**](../snapshots/PM-2026-07-22.md) Philip Morris | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $182.87 | $188.15 | 🟢 +2.9% | +0.5R | -7.9% | +12.5% | 22일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**CIFR**](../snapshots/CIFR-2026-07-22.md) Cipher Mining | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-21 | $20.54 | $22.89 | 🟢 +11.4% | +0.5R | -31.1% | +52.3% | 1일 | <span class="js-shares" data-ticker="CIFR">—</span> | <span class="js-pnl" data-ticker="CIFR">—</span> |
| [**KMI**](../snapshots/KMI-2026-07-22.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $32.37 | 🟢 +2.0% | +0.5R | -6.4% | +11.1% | 20일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**MS**](../snapshots/MS-2026-07-22.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $216.40 | 🟢 +2.2% | +0.4R | -7.6% | +14.1% | 22일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-07-22.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $552.69 | 🟢 +4.5% | +0.4R | -15.8% | +30.3% | 4일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-07-22.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $125.00 | $126.25 | 🟢 +1.0% | +0.2R | -6.0% | +14.1% | 9일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**GS**](../snapshots/GS-2026-07-22.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-25 | $1,076.91 | $1,085.80 | 🟢 +0.8% | +0.1R | -6.5% | +16.4% | 27일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**AMD**](../snapshots/AMD-2026-07-22.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $544.43 | 🟢 +0.1% | +0.0R | -12.7% | +37.7% | 9일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**CORZ**](../snapshots/CORZ-2026-07-22.md) Core Scientific | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-22 | $24.01 | $24.01 | ⚪ +0.0% | +0.0R | -15.0% | +45.0% | 0일 | <span class="js-shares" data-ticker="CORZ">—</span> | <span class="js-pnl" data-ticker="CORZ">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-07-22.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-22 | $207.29 | $207.29 | ⚪ +0.0% | +0.0R | -7.0% | +20.9% | 0일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**009150**](../snapshots/009150-2026-07-22.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,275,000 | 🔴 -1.1% | -0.0R | -29.0% | +91.4% | 9일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**278470**](../snapshots/278470-2026-07-22.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩375,000 | ₩368,000 | 🔴 -1.9% | -0.1R | -14.4% | +50.8% | 9일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**USD**](../snapshots/USD-2026-07-22.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $92.19 | $90.10 | 🔴 -2.3% | -0.1R | -15.2% | +54.8% | 9일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**KO**](../snapshots/KO-2026-07-22.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $81.96 | 🔴 -0.8% | -0.2R | -2.9% | +12.1% | 22일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**GEV**](../snapshots/GEV-2026-07-22.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $1,102.51 | $1,079.03 | 🔴 -2.1% | -0.2R | -7.1% | +29.9% | 22일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-07-22.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $355.50 | $347.15 | 🔴 -2.3% | -0.4R | -3.6% | +20.3% | 9일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**066570**](../snapshots/066570-2026-07-22.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩185,600 | ₩167,200 | 🔴 -9.9% | -0.4R | -15.3% | +90.0% | 9일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**161890**](../snapshots/161890-2026-07-22.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-14 | ₩106,500 | ₩99,500 | 🔴 -6.6% | -0.5R | -7.8% | +51.5% | 8일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**LLY**](../snapshots/LLY-2026-07-22.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,175.15 | 🔴 -3.3% | -0.5R | -3.0% | +22.9% | 13일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**BE**](../snapshots/BE-2026-07-22.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $275.01 | $226.55 | 🔴 -17.6% | -0.8R | -4.2% | +98.1% | 22일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**CAT**](../snapshots/CAT-2026-07-22.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $991.41 | $889.76 | 🔴 -10.3% | -1.3R | +2.6% | +38.0% | 20일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |

**합계** 22포지션 · 평균 -0.1R · 양의 R 9/22

<script type="application/json" id="pos-data">
[{"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 327.739990234375, "r": 0.5736703473480074}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 188.14999389648438, "r": 0.5494367728806329}, {"ticker": "CIFR", "entry": 20.540000915527344, "stop": 15.765568272066863, "current": 22.889999389648438, "r": 0.4922047601488056}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 32.3650016784668, "r": 0.4559458286024517}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 216.39500427246094, "r": 0.39945676096366894}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 552.6900024414062, "r": 0.37175727907115685}, {"ticker": "PCAR", "entry": 125.00499725341797, "stop": 118.63641278688668, "current": 126.25, "r": 0.1954912827371408}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1085.7950439453125, "r": 0.142956870079888}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 544.4299926757812, "r": 0.0064988022326512495}, {"ticker": "CORZ", "entry": 24.010000228881836, "stop": 20.41172026954609, "current": 24.010000228881836, "r": 0.0}, {"ticker": "NVDA", "entry": 207.2899932861328, "stop": 192.84901769421657, "current": 207.2899932861328, "r": 0.0}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1275000.0, "r": -0.03647675010086141}, {"ticker": "278470", "entry": 375000.0, "stop": 314981.3971592858, "current": 368000.0, "r": -0.11663050568800447}, {"ticker": "USD", "entry": 92.19000244140625, "stop": 76.43252202238607, "current": 90.0999984741211, "r": -0.13263566964439324}, {"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 81.95999908447266, "r": -0.22481119878811012}, {"ticker": "GEV", "entry": 1102.510009765625, "stop": 1002.9343461066205, "current": 1079.030029296875, "r": -0.23580039144059214}, {"ticker": "GOOGL", "entry": 355.5, "stop": 334.78411647226744, "current": 347.1499938964844, "r": -0.40307265158820715}, {"ticker": "066570", "entry": 185600.0, "stop": 141564.11742172934, "current": 167200.0, "r": -0.417841063303212}, {"ticker": "161890", "entry": 106500.0, "stop": 91763.98947207628, "current": 99500.0, "r": -0.4750268050321683}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1175.14501953125, "r": -0.5345227687766686}, {"ticker": "BE", "entry": 275.010009765625, "stop": 217.05686725842352, "current": 226.55279541015625, "r": -0.8361447241527459}, {"ticker": "CAT", "entry": 991.4099731445312, "stop": 912.5806793261623, "current": 889.760009765625, "r": -1.2894947862036998}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

