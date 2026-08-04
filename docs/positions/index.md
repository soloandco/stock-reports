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
| [**KO**](../snapshots/KO-2026-08-05.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $86.46 | 🟢 +4.6% | +1.2R | -8.0% | +6.2% | 36일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**GOOGL**](../snapshots/GOOGL-2026-08-05.md) Alphabet | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 08-01 | $356.13 | $379.76 | 🟢 +6.6% | +1.0R | -12.5% | +12.6% | 4일 | <span class="js-shares" data-ticker="GOOGL">—</span> | <span class="js-pnl" data-ticker="GOOGL">—</span> |
| [**CAT**](../snapshots/CAT-2026-08-05.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $808.91 | $883.92 | 🟢 +9.3% | +0.9R | -17.7% | +19.1% | 5일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |
| [**AVGO**](../snapshots/AVGO-2026-08-05.md) Broadcom | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $392.23 | $420.89 | 🟢 +7.3% | +0.8R | -14.8% | +17.3% | 1일 | <span class="js-shares" data-ticker="AVGO">—</span> | <span class="js-pnl" data-ticker="AVGO">—</span> |
| [**USD**](../snapshots/USD-2026-08-05.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $90.08 | 🟢 +16.2% | +0.8R | -31.5% | +38.8% | 5일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**MS**](../snapshots/MS-2026-08-05.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $218.06 | 🟢 +3.0% | +0.5R | -8.3% | +13.2% | 36일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**BE**](../snapshots/BE-2026-08-05.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $207.21 | $229.63 | 🟢 +10.8% | +0.4R | -35.3% | +66.7% | 5일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-08-05.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $206.64 | $212.36 | 🟢 +2.8% | +0.4R | -9.9% | +18.9% | 1일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-08-05.md) Skyward Specialty Insurance | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $59.87 | $61.35 | 🟢 +2.5% | +0.3R | -9.4% | +18.7% | 5일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |
| [**PM**](../snapshots/PM-2026-08-05.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $185.85 | 🟢 +1.6% | +0.3R | -6.8% | +13.9% | 36일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**CORZ**](../snapshots/CORZ-2026-08-05.md) Core Scientific | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $21.81 | $23.01 | 🟢 +5.5% | +0.3R | -22.2% | +45.8% | 5일 | <span class="js-shares" data-ticker="CORZ">—</span> | <span class="js-pnl" data-ticker="CORZ">—</span> |
| [**GEV**](../snapshots/GEV-2026-08-05.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $982.55 | $1,015.41 | 🟢 +3.3% | +0.3R | -15.4% | +33.2% | 5일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**BA**](../snapshots/BA-2026-08-05.md) Boeing | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $233.49 | $236.79 | 🟢 +1.4% | +0.2R | -7.9% | +18.0% | 1일 | <span class="js-shares" data-ticker="BA">—</span> | <span class="js-pnl" data-ticker="BA">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-08-05.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $542.48 | 🟢 +2.5% | +0.2R | -14.2% | +32.7% | 18일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-08-05.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-30 | $133.87 | $134.70 | 🟢 +0.6% | +0.1R | -5.9% | +15.2% | 6일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**CDNS**](../snapshots/CDNS-2026-08-05.md) Cadence Design Systems | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-28 | $338.61 | $341.97 | 🟢 +1.0% | +0.1R | -9.7% | +25.2% | 8일 | <span class="js-shares" data-ticker="CDNS">—</span> | <span class="js-pnl" data-ticker="CDNS">—</span> |
| [**161890**](../snapshots/161890-2026-08-05.md) 한국콜마 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | ₩95,100 | ₩96,800 | 🟢 +1.8% | +0.1R | -17.4% | +45.3% | 5일 | <span class="js-shares" data-ticker="161890">—</span> | <span class="js-pnl" data-ticker="161890">—</span> |
| [**066570**](../snapshots/066570-2026-08-05.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-05 | ₩165,500 | ₩165,500 | ⚪ +0.0% | +0.0R | -21.0% | +63.0% | 0일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**278470**](../snapshots/278470-2026-08-05.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | ₩338,000 | ₩338,000 | ⚪ +0.0% | +0.0R | -15.2% | +45.6% | 1일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**KMI**](../snapshots/KMI-2026-08-05.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $31.49 | 🔴 -0.7% | -0.2R | -3.8% | +14.2% | 34일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**CIFR**](../snapshots/CIFR-2026-08-05.md) Cipher Mining | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $22.66 | $21.57 | 🔴 -4.8% | -0.2R | -20.2% | +80.6% | 5일 | <span class="js-shares" data-ticker="CIFR">—</span> | <span class="js-pnl" data-ticker="CIFR">—</span> |
| [**AMD**](../snapshots/AMD-2026-08-05.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $526.41 | 🔴 -3.2% | -0.3R | -9.7% | +42.4% | 23일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**009150**](../snapshots/009150-2026-08-05.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,181,000 | 🔴 -8.4% | -0.3R | -23.4% | +106.6% | 23일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**GS**](../snapshots/GS-2026-08-05.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-25 | $1,076.91 | $1,056.61 | 🔴 -1.9% | -0.3R | -4.0% | +19.6% | 41일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**DLR**](../snapshots/DLR-2026-08-05.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $193.75 | 🔴 -2.7% | -0.5R | -3.2% | +20.5% | 11일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-08-05.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $308.70 | 🔴 -3.1% | -0.6R | -1.8% | +18.5% | 23일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**LLY**](../snapshots/LLY-2026-08-05.md) Eli Lilly | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-09 | $1,215.83 | $1,113.70 | 🔴 -8.4% | -1.3R | +2.3% | +29.7% | 27일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |

**합계** 27포지션 · 평균 +0.2R · 양의 R 17/27

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 86.46499633789062, "r": 1.2429717716807585}, {"ticker": "GOOGL", "entry": 356.1300048828125, "stop": 332.3223349724717, "current": 379.760009765625, "r": 0.9925374877845091}, {"ticker": "CAT", "entry": 808.905029296875, "stop": 727.7539578057504, "current": 883.9199829101562, "r": 0.9243864835658456}, {"ticker": "AVGO", "entry": 392.2300109863281, "stop": 358.4747922503201, "current": 420.8900146484375, "r": 0.8490540051377777}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 90.08000183105469, "r": 0.7924323840578893}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 218.05999755859375, "r": 0.5417225130373049}, {"ticker": "BE", "entry": 207.2100067138672, "stop": 148.66912487910352, "current": 229.6300048828125, "r": 0.3829801920686394}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 212.360107421875, "r": 0.3736580747208121}, {"ticker": "SKWD", "entry": 59.869998931884766, "stop": 55.5506716263135, "current": 61.345001220703125, "r": 0.34148889039175956}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 185.84500122070312, "r": 0.3095791914242609}, {"ticker": "CORZ", "entry": 21.809999465942383, "stop": 17.894681127765164, "current": 23.010000228881836, "r": 0.3064886834969631}, {"ticker": "GEV", "entry": 982.5499877929688, "stop": 859.1024131708681, "current": 1015.4099731445312, "r": 0.26618575093236074}, {"ticker": "BA", "entry": 233.49000549316406, "stop": 218.1540878686476, "current": 236.7949981689453, "r": 0.21550667894158398}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 542.47998046875, "r": 0.21140017183459917}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 134.6999969482422, "r": 0.11716478188770245}, {"ticker": "CDNS", "entry": 338.6099853515625, "stop": 308.74442908515095, "current": 341.9700012207031, "r": 0.1125047140983436}, {"ticker": "161890", "entry": 95100.0, "stop": 79921.43092159486, "current": 96800.0, "r": 0.11200001734146499}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 165500.0, "r": 0.0}, {"ticker": "278470", "entry": 338000.0, "stop": 286622.8624105194, "current": 338000.0, "r": 0.0}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 31.489999771118164, "r": -0.16258441446934574}, {"ticker": "CIFR", "entry": 22.655000686645508, "stop": 17.219999176066082, "current": 21.56999969482422, "r": -0.1996321417223704}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 526.4149780273438, "r": -0.2565890416001395}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1181000.0, "r": -0.2813920722066452}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1056.6099853515625, "r": -0.32662107521426115}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 193.75, "r": -0.4657426303288176}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 308.70001220703125, "r": -0.6386155534005946}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1113.699951171875, "r": -1.3417942277896224}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

