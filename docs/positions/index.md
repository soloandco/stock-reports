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
| [**PCAR**](../snapshots/PCAR-2026-07-25.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $125.00 | $132.24 | 🟢 +5.8% | +1.1R | -10.3% | +9.0% | 12일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**PM**](../snapshots/PM-2026-07-25.md) Philip Morris | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $182.87 | $193.00 | 🟢 +5.5% | +1.1R | -10.2% | +9.7% | 25일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-07-25.md) Apple | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-13 | $318.73 | $333.02 | 🟢 +4.5% | +0.9R | -9.0% | +9.9% | 12일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**KMI**](../snapshots/KMI-2026-07-25.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $32.86 | 🟢 +3.6% | +0.8R | -7.8% | +9.4% | 23일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**CIFR**](../snapshots/CIFR-2026-07-25.md) Cipher Mining | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-21 | $20.54 | $23.15 | 🟢 +12.7% | +0.5R | -31.9% | +50.6% | 4일 | <span class="js-shares" data-ticker="CIFR">—</span> | <span class="js-pnl" data-ticker="CIFR">—</span> |
| [**MS**](../snapshots/MS-2026-07-25.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $214.48 | 🟢 +1.3% | +0.2R | -6.7% | +15.1% | 25일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**009150**](../snapshots/009150-2026-07-25.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,326,000 | 🟢 +2.9% | +0.1R | -31.7% | +84.0% | 12일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**DLR**](../snapshots/DLR-2026-07-25.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $199.08 | ⚪ +0.0% | +0.0R | -5.7% | +17.2% | 0일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-07-25.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-22 | $207.29 | $206.84 | 🔴 -0.2% | -0.0R | -6.8% | +21.2% | 3일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-07-25.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $527.01 | 🔴 -0.4% | -0.0R | -11.7% | +36.6% | 7일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**KO**](../snapshots/KO-2026-07-25.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $82.25 | 🔴 -0.5% | -0.1R | -3.2% | +11.7% | 25일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**GS**](../snapshots/GS-2026-07-25.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-25 | $1,076.91 | $1,061.23 | 🔴 -1.5% | -0.3R | -4.4% | +19.0% | 30일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**LLY**](../snapshots/LLY-2026-07-25.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,196.03 | 🔴 -1.6% | -0.3R | -4.7% | +20.7% | 16일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**AMD**](../snapshots/AMD-2026-07-25.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $521.95 | 🔴 -4.1% | -0.3R | -8.9% | +43.6% | 12일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**278470**](../snapshots/278470-2026-07-25.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩375,000 | ₩354,000 | 🔴 -5.6% | -0.3R | -11.0% | +56.8% | 12일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**066570**](../snapshots/066570-2026-07-25.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩185,600 | ₩169,200 | 🔴 -8.8% | -0.4R | -16.3% | +87.8% | 12일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**USD**](../snapshots/USD-2026-07-25.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $92.19 | $85.74 | 🔴 -7.0% | -0.4R | -10.9% | +62.7% | 12일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**161890**](../snapshots/161890-2026-07-25.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-14 | ₩106,500 | ₩100,200 | 🔴 -5.9% | -0.4R | -8.4% | +50.4% | 11일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**GEV**](../snapshots/GEV-2026-07-25.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $1,102.51 | $1,014.75 | 🔴 -8.0% | -0.9R | -1.2% | +38.1% | 25일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**CAT**](../snapshots/CAT-2026-07-25.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $991.41 | $888.73 | 🔴 -10.4% | -1.3R | +2.7% | +38.2% | 23일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |

**합계** 20포지션 · 평균 +0.0R · 양의 R 7/20

<script type="application/json" id="pos-data">
[{"ticker": "PCAR", "entry": 125.00499725341797, "stop": 118.63641278688668, "current": 132.24000549316406, "r": 1.1360465230174943}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 193.0, "r": 1.05412849978324}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 333.0199890136719, "r": 0.909850781323246}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 32.86000061035156, "r": 0.8058557054696962}, {"ticker": "CIFR", "entry": 20.540000915527344, "stop": 15.765568272066863, "current": 23.149999618530273, "r": 0.546661540314708}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 214.47999572753906, "r": 0.23582839492771246}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1326000.0, "r": 0.09640283955227659}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 199.0800018310547, "r": 0.0}, {"ticker": "NVDA", "entry": 207.2899932861328, "stop": 192.84901769421657, "current": 206.83999633789062, "r": -0.031161118262265218}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 527.010009765625, "r": -0.03156891849949675}, {"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 82.25, "r": -0.13032536865614577}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1061.22998046875, "r": -0.2522868809747986}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1196.030029296875, "r": -0.2601334197993478}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 521.9500122070312, "r": -0.32179455230201437}, {"ticker": "278470", "entry": 375000.0, "stop": 314981.3971592858, "current": 354000.0, "r": -0.3498915170640134}, {"ticker": "066570", "entry": 185600.0, "stop": 141564.11742172934, "current": 169200.0, "r": -0.3724235564224281}, {"ticker": "USD", "entry": 92.19000244140625, "stop": 76.43252202238607, "current": 85.73999786376953, "r": -0.4093296901610738}, {"ticker": "161890", "entry": 106500.0, "stop": 91763.98947207628, "current": 100200.0, "r": -0.4275241245289515}, {"ticker": "GEV", "entry": 1102.510009765625, "stop": 1002.9343461066205, "current": 1014.75, "r": -0.8813399433234809}, {"ticker": "CAT", "entry": 991.4099731445312, "stop": 912.5806793261623, "current": 888.72998046875, "r": -1.3025613664936146}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

