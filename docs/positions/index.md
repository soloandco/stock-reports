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
| [**MS**](../snapshots/MS-2026-07-13.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $219.33 | 🟢 +3.6% | +0.7R | -8.8% | +12.5% | 13일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**KMI**](../snapshots/KMI-2026-07-13.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $32.32 | 🟢 +1.9% | +0.4R | -6.2% | +11.3% | 11일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**KO**](../snapshots/KO-2026-07-13.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $83.86 | 🟢 +1.5% | +0.4R | -5.1% | +9.5% | 13일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**009150**](../snapshots/009150-2026-07-13.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,289,000 | ⚪ +0.0% | +0.0R | -29.8% | +89.3% | 0일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**066570**](../snapshots/066570-2026-07-13.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩185,600 | ₩185,600 | ⚪ +0.0% | +0.0R | -23.7% | +71.2% | 0일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**161890**](../snapshots/161890-2026-07-14.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-14 | ₩106,500 | ₩106,500 | ⚪ +0.0% | +0.0R | -13.8% | +41.5% | 0일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**278470**](../snapshots/278470-2026-07-13.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩375,000 | ₩375,000 | ⚪ +0.0% | +0.0R | -16.0% | +48.0% | 0일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-07-13.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $318.73 | ⚪ +0.0% | +0.0R | -4.9% | +14.8% | 0일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**AMD**](../snapshots/AMD-2026-07-13.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $543.98 | ⚪ +0.0% | +0.0R | -12.6% | +37.8% | 0일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**AVGO**](../snapshots/AVGO-2026-07-13.md) Broadcom | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $391.85 | $391.85 | ⚪ +0.0% | +0.0R | -8.9% | +26.8% | 0일 | <span class="js-shares" data-ticker="AVGO">—</span> | <span class="js-pnl" data-ticker="AVGO">—</span> |
| [**CDNS**](../snapshots/CDNS-2026-07-13.md) Cadence Design Systems | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $387.14 | $387.14 | ⚪ +0.0% | +0.0R | -7.2% | +21.6% | 0일 | <span class="js-shares" data-ticker="CDNS">—</span> | <span class="js-pnl" data-ticker="CDNS">—</span> |
| [**CIFR**](../snapshots/CIFR-2026-07-13.md) Cipher Mining | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $21.28 | $21.28 | ⚪ +0.0% | +0.0R | -21.8% | +65.5% | 0일 | <span class="js-shares" data-ticker="CIFR">—</span> | <span class="js-pnl" data-ticker="CIFR">—</span> |
| [**CORZ**](../snapshots/CORZ-2026-07-13.md) Core Scientific | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $22.63 | $22.63 | ⚪ +0.0% | +0.0R | -15.7% | +47.0% | 0일 | <span class="js-shares" data-ticker="CORZ">—</span> | <span class="js-pnl" data-ticker="CORZ">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-07-13.md) Alphabet | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $355.50 | $355.50 | ⚪ +0.0% | +0.0R | -5.8% | +17.5% | 0일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-07-13.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $207.37 | $207.37 | ⚪ +0.0% | +0.0R | -6.8% | +20.4% | 0일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-07-13.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $125.00 | $125.00 | ⚪ +0.0% | +0.0R | -5.1% | +15.3% | 0일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**USD**](../snapshots/USD-2026-07-13.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $92.19 | $92.19 | ⚪ +0.0% | +0.0R | -17.1% | +51.3% | 0일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**PM**](../snapshots/PM-2026-07-13.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $181.01 | 🔴 -1.0% | -0.2R | -4.3% | +17.0% | 13일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**LLY**](../snapshots/LLY-2026-07-13.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,189.26 | 🔴 -2.2% | -0.3R | -4.2% | +21.4% | 4일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**GEV**](../snapshots/GEV-2026-07-13.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $1,102.51 | $1,061.48 | 🔴 -3.7% | -0.4R | -5.5% | +32.0% | 13일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**GS**](../snapshots/GS-2026-07-13.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-25 | $1,076.91 | $1,046.17 | 🔴 -2.9% | -0.5R | -3.0% | +20.8% | 18일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**BE**](../snapshots/BE-2026-07-13.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $275.01 | $238.76 | 🔴 -13.2% | -0.6R | -9.1% | +88.0% | 13일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**CAT**](../snapshots/CAT-2026-07-13.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $991.41 | $936.38 | 🔴 -5.6% | -0.7R | -2.5% | +31.1% | 11일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |

**합계** 23포지션 · 평균 -0.1R · 양의 R 3/23

<script type="application/json" id="pos-data">
[{"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 219.3300018310547, "r": 0.6502383337695538}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 32.31999969482422, "r": 0.42413436893889417}, {"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 83.86000061035156, "r": 0.3942324380163412}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1289000.0, "r": 0.0}, {"ticker": "066570", "entry": 185600.0, "stop": 141564.11742172934, "current": 185600.0, "r": 0.0}, {"ticker": "161890", "entry": 106500.0, "stop": 91763.98947207628, "current": 106500.0, "r": 0.0}, {"ticker": "278470", "entry": 375000.0, "stop": 314981.3971592858, "current": 375000.0, "r": 0.0}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 318.7300109863281, "r": 0.0}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 543.9849853515625, "r": 0.0}, {"ticker": "AVGO", "entry": 391.8500061035156, "stop": 356.8287411224586, "current": 391.8500061035156, "r": 0.0}, {"ticker": "CDNS", "entry": 387.135009765625, "stop": 359.20759760859266, "current": 387.135009765625, "r": 0.0}, {"ticker": "CIFR", "entry": 21.280000686645508, "stop": 16.63556842661093, "current": 21.280000686645508, "r": 0.0}, {"ticker": "CORZ", "entry": 22.6299991607666, "stop": 19.081676322606583, "current": 22.6299991607666, "r": 0.0}, {"ticker": "GOOGL", "entry": 355.5, "stop": 334.78411647226744, "current": 355.5, "r": 0.0}, {"ticker": "NVDA", "entry": 207.3699951171875, "stop": 193.26880716964297, "current": 207.3699951171875, "r": 0.0}, {"ticker": "PCAR", "entry": 125.00499725341797, "stop": 118.63641278688668, "current": 125.00499725341797, "r": 0.0}, {"ticker": "USD", "entry": 92.19000244140625, "stop": 76.43252202238607, "current": 92.19000244140625, "r": 0.0}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 181.00999450683594, "r": -0.19355169870771466}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1189.260009765625, "r": -0.34907861410808716}, {"ticker": "GEV", "entry": 1102.510009765625, "stop": 1002.9343461066205, "current": 1061.47998046875, "r": -0.41204876562391574}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1046.169921875, "r": -0.49459824546104514}, {"ticker": "BE", "entry": 275.010009765625, "stop": 217.05686725842352, "current": 238.75999450683594, "r": -0.6255056014310958}, {"ticker": "CAT", "entry": 991.4099731445312, "stop": 912.5806793261623, "current": 936.3800048828125, "r": -0.698090336677551}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

