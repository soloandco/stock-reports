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
| [**PM**](../snapshots/PM-2026-07-28.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $195.65 | 🟢 +7.0% | +1.3R | -11.4% | +8.2% | 28일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-07-28.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $125.00 | $133.44 | 🟢 +6.7% | +1.3R | -11.1% | +8.0% | 15일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-07-28.md) Apple | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-13 | $318.73 | $336.91 | 🟢 +5.7% | +1.2R | -10.1% | +8.6% | 15일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**KO**](../snapshots/KO-2026-07-28.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $84.10 | 🟢 +1.8% | +0.5R | -5.4% | +9.2% | 28일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**MS**](../snapshots/MS-2026-07-28.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $214.52 | 🟢 +1.3% | +0.2R | -6.8% | +15.1% | 28일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**CIFR**](../snapshots/CIFR-2026-07-28.md) Cipher Mining | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-21 | $20.54 | $21.65 | 🟢 +5.4% | +0.2R | -27.2% | +61.0% | 7일 | <span class="js-shares" data-ticker="CIFR">—</span> | <span class="js-pnl" data-ticker="CIFR">—</span> |
| [**009150**](../snapshots/009150-2026-07-28.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,326,000 | 🟢 +2.9% | +0.1R | -31.7% | +84.0% | 15일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**KMI**](../snapshots/KMI-2026-07-28.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $31.76 | 🟢 +0.1% | +0.0R | -4.6% | +13.2% | 26일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**CDNS**](../snapshots/CDNS-2026-07-28.md) Cadence Design Systems | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-28 | $338.61 | $338.61 | ⚪ +0.0% | +0.0R | -8.8% | +26.5% | 0일 | <span class="js-shares" data-ticker="CDNS">—</span> | <span class="js-pnl" data-ticker="CDNS">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-07-28.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $516.23 | 🔴 -2.4% | -0.2R | -9.9% | +39.5% | 10일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**LLY**](../snapshots/LLY-2026-07-28.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,197.99 | 🔴 -1.5% | -0.2R | -4.9% | +20.5% | 19일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**DLR**](../snapshots/DLR-2026-07-28.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $195.77 | 🔴 -1.7% | -0.3R | -4.2% | +19.2% | 3일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**278470**](../snapshots/278470-2026-07-28.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩375,000 | ₩354,000 | 🔴 -5.6% | -0.3R | -11.0% | +56.8% | 15일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**161890**](../snapshots/161890-2026-07-28.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-14 | ₩106,500 | ₩100,200 | 🔴 -5.9% | -0.4R | -8.4% | +50.4% | 14일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**GS**](../snapshots/GS-2026-07-28.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-25 | $1,076.91 | $1,046.08 | 🔴 -2.9% | -0.5R | -3.0% | +20.8% | 33일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**CORZ**](../snapshots/CORZ-2026-07-28.md) Core Scientific | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-26 | $22.75 | $20.74 | 🔴 -8.8% | -0.6R | -7.0% | +59.8% | 2일 | <span class="js-shares" data-ticker="CORZ">—</span> | <span class="js-pnl" data-ticker="CORZ">—</span> |
| [**AMD**](../snapshots/AMD-2026-07-28.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $494.95 | 🔴 -9.0% | -0.7R | -3.9% | +51.4% | 15일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**USD**](../snapshots/USD-2026-07-28.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $92.19 | $80.15 | 🔴 -13.1% | -0.8R | -4.6% | +74.0% | 15일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**GEV**](../snapshots/GEV-2026-07-28.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $1,102.51 | $996.73 | 🔴 -9.6% | -1.1R | +0.6% | +40.6% | 28일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**CAT**](../snapshots/CAT-2026-07-28.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $991.41 | $873.12 | 🔴 -11.9% | -1.5R | +4.5% | +40.6% | 26일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |

**합계** 20포지션 · 평균 -0.1R · 양의 R 8/20

<script type="application/json" id="pos-data">
[{"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 195.64999389648438, "r": 1.329886914794018}, {"ticker": "PCAR", "entry": 125.00499725341797, "stop": 118.63641278688668, "current": 133.44000244140625, "r": 1.3244709609045178}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 336.9100036621094, "r": 1.1575301591688416}, {"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 84.0999984741211, "r": 0.4724266649101667}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 214.52000427246094, "r": 0.23924693467804534}, {"ticker": "CIFR", "entry": 20.540000915527344, "stop": 15.765568272066863, "current": 21.649999618530273, "r": 0.2324880851598755}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1326000.0, "r": 0.09640283955227659}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 31.760000228881836, "r": 0.02827625379605525}, {"ticker": "CDNS", "entry": 338.6099853515625, "stop": 308.74442908515095, "current": 338.6099853515625, "r": 0.0}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 516.22998046875, "r": -0.20087847714704676}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1197.989990234375, "r": -0.2343832568022126}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 195.77000427246094, "r": -0.28923197743374285}, {"ticker": "278470", "entry": 375000.0, "stop": 314981.3971592858, "current": 354000.0, "r": -0.3498915170640134}, {"ticker": "161890", "entry": 106500.0, "stop": 91763.98947207628, "current": 100200.0, "r": -0.4275241245289515}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1046.0799560546875, "r": -0.49604576577056725}, {"ticker": "CORZ", "entry": 22.75, "stop": 19.2853467003893, "current": 20.739999771118164, "r": -0.5801446941625261}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 494.95001220703125, "r": -0.716097411450755}, {"ticker": "USD", "entry": 92.19000244140625, "stop": 76.43252202238607, "current": 80.1500015258789, "r": -0.7640816041246271}, {"ticker": "GEV", "entry": 1102.510009765625, "stop": 1002.9343461066205, "current": 996.72998046875, "r": -1.0623080520870771}, {"ticker": "CAT", "entry": 991.4099731445312, "stop": 912.5806793261623, "current": 873.1199951171875, "r": -1.5005840125866972}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

