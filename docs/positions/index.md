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
| [**PM**](../snapshots/PM-2026-07-21.md) Philip Morris | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $182.87 | $192.72 | 🟢 +5.4% | +1.0R | -10.1% | +9.8% | 21일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**KMI**](../snapshots/KMI-2026-07-21.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $32.58 | 🟢 +2.7% | +0.6R | -7.0% | +10.4% | 19일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-07-21.md) Apple | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-13 | $318.73 | $326.59 | 🟢 +2.5% | +0.5R | -7.2% | +12.0% | 8일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**009150**](../snapshots/009150-2026-07-21.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,310,000 | 🟢 +1.6% | +0.1R | -30.9% | +86.3% | 8일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**CIFR**](../snapshots/CIFR-2026-07-21.md) Cipher Mining | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-21 | $20.54 | $20.54 | ⚪ +0.0% | +0.0R | -23.2% | +69.7% | 0일 | <span class="js-shares" data-ticker="CIFR">—</span> | <span class="js-pnl" data-ticker="CIFR">—</span> |
| [**MS**](../snapshots/MS-2026-07-21.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $210.94 | 🔴 -0.4% | -0.1R | -5.2% | +17.0% | 21일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-07-21.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $524.14 | 🔴 -0.9% | -0.1R | -11.2% | +37.4% | 3일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-07-21.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $125.00 | $124.33 | 🔴 -0.5% | -0.1R | -4.6% | +15.9% | 8일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**278470**](../snapshots/278470-2026-07-21.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩375,000 | ₩368,000 | 🔴 -1.9% | -0.1R | -14.4% | +50.8% | 8일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-07-21.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $355.50 | $351.99 | 🔴 -1.0% | -0.2R | -4.9% | +18.7% | 8일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**KO**](../snapshots/KO-2026-07-21.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $82.12 | 🔴 -0.6% | -0.2R | -3.1% | +11.9% | 21일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**GEV**](../snapshots/GEV-2026-07-21.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $1,102.51 | $1,079.18 | 🔴 -2.1% | -0.2R | -7.1% | +29.8% | 21일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**066570**](../snapshots/066570-2026-07-21.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩185,600 | ₩173,200 | 🔴 -6.7% | -0.3R | -18.3% | +83.4% | 8일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**161890**](../snapshots/161890-2026-07-21.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-14 | ₩106,500 | ₩101,700 | 🔴 -4.5% | -0.3R | -9.8% | +48.2% | 7일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**GS**](../snapshots/GS-2026-07-21.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-25 | $1,076.91 | $1,055.03 | 🔴 -2.0% | -0.4R | -3.8% | +19.7% | 26일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**USD**](../snapshots/USD-2026-07-21.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $92.19 | $83.24 | 🔴 -9.7% | -0.6R | -8.2% | +67.5% | 8일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**AMD**](../snapshots/AMD-2026-07-21.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $503.57 | 🔴 -7.4% | -0.6R | -5.6% | +48.8% | 8일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**LLY**](../snapshots/LLY-2026-07-21.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,146.90 | 🔴 -5.7% | -0.9R | -0.6% | +25.9% | 12일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**BE**](../snapshots/BE-2026-07-21.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $275.01 | $197.06 | 🔴 -28.3% | -1.3R | +10.1% | +127.8% | 21일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**CAT**](../snapshots/CAT-2026-07-21.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $991.41 | $864.30 | 🔴 -12.8% | -1.6R | +5.6% | +42.1% | 19일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |

**합계** 20포지션 · 평균 -0.2R · 양의 R 4/20

<script type="application/json" id="pos-data">
[{"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 192.72000122070312, "r": 1.0249918215115306}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 32.58000183105469, "r": 0.607927322041272}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 326.5899963378906, "r": 0.500449601785548}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1310000.0, "r": 0.05471512515129212}, {"ticker": "CIFR", "entry": 20.540000915527344, "stop": 15.765568272066863, "current": 20.540000915527344, "r": 0.0}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 210.94000244140625, "r": -0.06664718343154709}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 524.1400146484375, "r": -0.07664464076608658}, {"ticker": "PCAR", "entry": 125.00499725341797, "stop": 118.63641278688668, "current": 124.33000183105469, "r": -0.10598829707144075}, {"ticker": "278470", "entry": 375000.0, "stop": 314981.3971592858, "current": 368000.0, "r": -0.11663050568800447}, {"ticker": "GOOGL", "entry": 355.5, "stop": 334.78411647226744, "current": 351.989990234375, "r": -0.169435677745828}, {"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 82.12000274658203, "r": -0.17268005702578984}, {"ticker": "GEV", "entry": 1102.510009765625, "stop": 1002.9343461066205, "current": 1079.1800537109375, "r": -0.23429375409016223}, {"ticker": "066570", "entry": 185600.0, "stop": 141564.11742172934, "current": 173200.0, "r": -0.28158854266086025}, {"ticker": "161890", "entry": 106500.0, "stop": 91763.98947207628, "current": 101700.0, "r": -0.3257326663077726}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1055.030029296875, "r": -0.35204204586031934}, {"ticker": "USD", "entry": 92.19000244140625, "stop": 76.43252202238607, "current": 83.23999786376953, "r": -0.5679844962290767}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 503.57000732421875, "r": -0.5902126440227841}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1146.9000244140625, "r": -0.9056083420680324}, {"ticker": "BE", "entry": 275.010009765625, "stop": 217.05686725842352, "current": 197.05999755859375, "r": -1.3450523791241327}, {"ticker": "CAT", "entry": 991.4099731445312, "stop": 912.5806793261623, "current": 864.2999877929688, "r": -1.6124714455065072}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

