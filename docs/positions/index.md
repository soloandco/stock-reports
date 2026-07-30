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
| [**KO**](../snapshots/KO-2026-07-31.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $88.51 | 🟢 +7.1% | +1.9R | -10.1% | +3.8% | 31일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**PM**](../snapshots/PM-2026-07-31.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $192.04 | 🟢 +5.0% | +1.0R | -9.8% | +10.2% | 31일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-07-31.md) Apple | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-13 | $318.73 | $333.43 | 🟢 +4.6% | +0.9R | -9.1% | +9.7% | 18일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**066570**](../snapshots/066570-2026-07-31.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | ₩150,500 | ₩150,500 | ⚪ +0.0% | +0.0R | -25.1% | +75.3% | 0일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**161890**](../snapshots/161890-2026-07-31.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | ₩97,400 | ₩97,400 | ⚪ +0.0% | +0.0R | -15.1% | +45.4% | 0일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**BE**](../snapshots/BE-2026-07-31.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $207.21 | $207.21 | ⚪ +0.0% | +0.0R | -28.3% | +84.8% | 0일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**CAT**](../snapshots/CAT-2026-07-31.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $808.91 | $808.91 | ⚪ +0.0% | +0.0R | -10.0% | +30.1% | 0일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |
| [**CIFR**](../snapshots/CIFR-2026-07-31.md) Cipher Mining | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $22.66 | $22.66 | ⚪ +0.0% | +0.0R | -24.0% | +72.0% | 0일 | <span class="js-shares" data-ticker="CIFR">—</span> | <span class="js-pnl" data-ticker="CIFR">—</span> |
| [**CORZ**](../snapshots/CORZ-2026-07-31.md) Core Scientific | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $21.81 | $21.81 | ⚪ +0.0% | +0.0R | -18.0% | +53.9% | 0일 | <span class="js-shares" data-ticker="CORZ">—</span> | <span class="js-pnl" data-ticker="CORZ">—</span> |
| [**GEV**](../snapshots/GEV-2026-07-31.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $982.55 | $982.55 | ⚪ +0.0% | +0.0R | -12.6% | +37.7% | 0일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-07-31.md) Skyward Specialty Insurance | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $59.87 | $59.87 | ⚪ +0.0% | +0.0R | -7.2% | +21.6% | 0일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |
| [**USD**](../snapshots/USD-2026-07-31.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $77.55 | ⚪ +0.0% | +0.0R | -20.4% | +61.2% | 0일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-07-31.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-30 | $133.87 | $133.76 | 🔴 -0.1% | -0.0R | -5.2% | +16.0% | 1일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**KMI**](../snapshots/KMI-2026-07-31.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $31.65 | 🔴 -0.2% | -0.0R | -4.2% | +13.6% | 29일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**MS**](../snapshots/MS-2026-07-31.md) Morgan Stanley | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $211.72 | $210.13 | 🔴 -0.8% | -0.1R | -4.8% | +17.5% | 31일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**CDNS**](../snapshots/CDNS-2026-07-31.md) Cadence Design Systems | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-28 | $338.61 | $332.82 | 🔴 -1.7% | -0.2R | -7.2% | +28.7% | 3일 | <span class="js-shares" data-ticker="CDNS">—</span> | <span class="js-pnl" data-ticker="CDNS">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-07-31.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $504.53 | 🔴 -4.6% | -0.4R | -7.8% | +42.7% | 13일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**DLR**](../snapshots/DLR-2026-07-31.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $193.23 | 🔴 -2.9% | -0.5R | -2.9% | +20.8% | 6일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**009150**](../snapshots/009150-2026-07-31.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,029,000 | 🔴 -20.2% | -0.7R | -12.0% | +137.2% | 18일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**LLY**](../snapshots/LLY-2026-07-31.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,155.27 | 🔴 -5.0% | -0.8R | -1.3% | +25.0% | 22일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**GS**](../snapshots/GS-2026-07-31.md) Goldman Sachs | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-25 | $1,076.91 | $1,025.11 | 🔴 -4.8% | -0.8R | -1.0% | +23.2% | 36일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**AMD**](../snapshots/AMD-2026-07-31.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $485.39 | 🔴 -10.8% | -0.9R | -2.0% | +54.4% | 18일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |

**합계** 22포지션 · 평균 -0.0R · 양의 R 3/22

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 88.51499938964844, "r": 1.9108877324499713}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 192.0449981689453, "r": 0.9547509911733502}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 333.42999267578125, "r": 0.935955940589537}, {"ticker": "066570", "entry": 150500.0, "stop": 112728.14763778396, "current": 150500.0, "r": 0.0}, {"ticker": "161890", "entry": 97400.0, "stop": 82652.00102095744, "current": 97400.0, "r": 0.0}, {"ticker": "BE", "entry": 207.2100067138672, "stop": 148.66912487910352, "current": 207.2100067138672, "r": 0.0}, {"ticker": "CAT", "entry": 808.905029296875, "stop": 727.7539578057504, "current": 808.905029296875, "r": 0.0}, {"ticker": "CIFR", "entry": 22.655000686645508, "stop": 17.219999176066082, "current": 22.655000686645508, "r": 0.0}, {"ticker": "CORZ", "entry": 21.809999465942383, "stop": 17.894681127765164, "current": 21.809999465942383, "r": 0.0}, {"ticker": "GEV", "entry": 982.5499877929688, "stop": 859.1024131708681, "current": 982.5499877929688, "r": 0.0}, {"ticker": "SKWD", "entry": 59.869998931884766, "stop": 55.5506716263135, "current": 59.869998931884766, "r": 0.0}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 77.55000305175781, "r": 0.0}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 133.75999450683594, "r": -0.015527914562523153}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 31.649999618530273, "r": -0.049482095857106036}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 210.1300048828125, "r": -0.13585761978039182}, {"ticker": "CDNS", "entry": 338.6099853515625, "stop": 308.74442908515095, "current": 332.82000732421875, "r": -0.19386807919112758}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 504.5299987792969, "r": -0.38463667311038885}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 193.22999572753906, "r": -0.5111812934503003}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1029000.0, "r": -0.6774253590159977}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1155.27001953125, "r": -0.7956425083470203}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1025.1099853515625, "r": -0.8334456625026812}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 485.3900146484375, "r": -0.8557097955547734}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

