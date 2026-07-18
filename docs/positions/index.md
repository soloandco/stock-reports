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
| [**PM**](../snapshots/PM-2026-07-19.md) Philip Morris | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $182.87 | $192.98 | 🟢 +5.5% | +1.1R | -10.2% | +9.7% | 19일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-07-19.md) Apple | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-13 | $318.73 | $333.74 | 🟢 +4.7% | +1.0R | -9.2% | +9.6% | 6일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**KMI**](../snapshots/KMI-2026-07-19.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $32.30 | 🟢 +1.8% | +0.4R | -6.2% | +11.3% | 17일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**MS**](../snapshots/MS-2026-07-19.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $215.50 | 🟢 +1.8% | +0.3R | -7.2% | +14.5% | 19일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**278470**](../snapshots/278470-2026-07-19.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩375,000 | ₩393,000 | 🟢 +4.8% | +0.3R | -19.9% | +41.2% | 6일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-07-19.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $125.00 | $126.20 | 🟢 +1.0% | +0.2R | -6.0% | +14.2% | 6일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**161890**](../snapshots/161890-2026-07-19.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-14 | ₩106,500 | ₩107,600 | 🟢 +1.0% | +0.1R | -14.7% | +40.1% | 5일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**009150**](../snapshots/009150-2026-07-19.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,277,000 | 🔴 -0.9% | -0.0R | -29.1% | +91.1% | 6일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-07-19.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $521.81 | 🔴 -1.4% | -0.1R | -10.8% | +38.0% | 1일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**066570**](../snapshots/066570-2026-07-19.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩185,600 | ₩179,000 | 🔴 -3.6% | -0.1R | -20.9% | +77.5% | 6일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**GS**](../snapshots/GS-2026-07-19.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-25 | $1,076.91 | $1,065.22 | 🔴 -1.1% | -0.2R | -4.7% | +18.6% | 24일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**KO**](../snapshots/KO-2026-07-19.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $81.56 | 🔴 -1.3% | -0.4R | -2.4% | +12.6% | 19일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-07-19.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $355.50 | $346.77 | 🔴 -2.5% | -0.4R | -3.5% | +20.4% | 6일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**GEV**](../snapshots/GEV-2026-07-19.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $1,102.51 | $1,057.84 | 🔴 -4.1% | -0.4R | -5.2% | +32.5% | 19일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**LLY**](../snapshots/LLY-2026-07-19.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,179.11 | 🔴 -3.0% | -0.5R | -3.3% | +22.5% | 10일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**AVGO**](../snapshots/AVGO-2026-07-19.md) Broadcom | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $391.85 | $370.83 | 🔴 -5.4% | -0.6R | -3.8% | +34.0% | 6일 | <span class="js-shares" data-ticker="AVGO">—</span> | <span class="js-pnl" data-ticker="AVGO">—</span> |
| [**USD**](../snapshots/USD-2026-07-19.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $92.19 | $82.26 | 🔴 -10.8% | -0.6R | -7.1% | +69.5% | 6일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**AMD**](../snapshots/AMD-2026-07-19.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $495.76 | 🔴 -8.9% | -0.7R | -4.1% | +51.2% | 6일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**BE**](../snapshots/BE-2026-07-19.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $275.01 | $214.96 | 🔴 -21.8% | -1.0R | +1.0% | +108.8% | 19일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**CAT**](../snapshots/CAT-2026-07-19.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $991.41 | $880.28 | 🔴 -11.2% | -1.4R | +3.7% | +39.5% | 17일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |

**합계** 20포지션 · 평균 -0.2R · 양의 R 7/20

<script type="application/json" id="pos-data">
[{"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 192.97999572753906, "r": 1.0520468548124382}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 333.739990234375, "r": 0.9556936560958254}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 32.29999923706055, "r": 0.40999624204086654}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 215.5, "r": 0.3229829054885448}, {"ticker": "278470", "entry": 375000.0, "stop": 314981.3971592858, "current": 393000.0, "r": 0.2999070146262972}, {"ticker": "PCAR", "entry": 125.00499725341797, "stop": 118.63641278688668, "current": 126.19999694824219, "r": 0.18763976533628154}, {"ticker": "161890", "entry": 106500.0, "stop": 91763.98947207628, "current": 107600.0, "r": 0.07464706936219788}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1277000.0, "r": -0.031265785800738355}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 521.8099975585938, "r": -0.11323954735294096}, {"ticker": "066570", "entry": 185600.0, "stop": 141564.11742172934, "current": 179000.0, "r": -0.14987777270658692}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1065.219970703125, "r": -0.18808925704394353}, {"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 81.55999755859375, "r": -0.3551365674442559}, {"ticker": "GOOGL", "entry": 355.5, "stop": 334.78411647226744, "current": 346.7699890136719, "r": -0.42141629994401025}, {"ticker": "GEV", "entry": 1102.510009765625, "stop": 1002.9343461066205, "current": 1057.8399658203125, "r": -0.4486040293769416}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1179.1099853515625, "r": -0.4824306509197959}, {"ticker": "AVGO", "entry": 391.8500061035156, "stop": 356.8287411224586, "current": 370.8299865722656, "r": -0.6002073181142862}, {"ticker": "USD", "entry": 92.19000244140625, "stop": 76.43252202238607, "current": 82.26000213623047, "r": -0.6301769090691492}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 495.760009765625, "r": -0.7042683613301248}, {"ticker": "BE", "entry": 275.010009765625, "stop": 217.05686725842352, "current": 214.9600067138672, "r": -1.0361819990054166}, {"ticker": "CAT", "entry": 991.4099731445312, "stop": 912.5806793261623, "current": 880.280029296875, "r": -1.4097544004860867}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

