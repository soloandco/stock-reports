# 가상 포지션

!!! info "알림 기준 성적은 방식별 기록에 있습니다"
    이 페이지는 과거 **판정 기록**에서 매수 전환을 다시 만든 가상 포지션입니다. 알림이 나가지 않은 전환도 들어가서 건수가 [방식별 기록](../strategies/index.md)보다 많습니다. 실제로 알림이 나간 추천의 추천가·목표가·손절가와 「추천대로 했다면」 금액은 방식별 기록에서 보세요.

현재 **매수** 판정인 종목의 진입가 대비 현재 수익률·R-배수. 진입가 = 비매수→매수로 전환된 **첫 스냅샷 가격**, 현재가 = **최신 스냅샷 가격**입니다.

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
    | **+5R** | 목표 도달 (5:1 리워드) |
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
| [**NVDA**](../snapshots/NVDA-2026-10-01.md) NVIDIA | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 08-04 | $206.64 | $228.38 | 🟢 +10.5% | +1.4R | -16.2% | +24.0% | 관측 58일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**KO**](../snapshots/KO-2026-10-01.md) Coca-Cola | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 06-30 | $82.65 | $86.07 | 🟢 +4.1% | +1.1R | -7.5% | +13.8% | 관측 93일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**XLK**](../snapshots/XLK-2026-10-01.md) XLK 테크놀로지 섹터 ETF | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-11 | $187.67 | $195.75 | 🟢 +4.3% | +1.1R | -7.9% | +14.8% | 19일 | <span class="js-shares" data-ticker="XLK">—</span> | <span class="js-pnl" data-ticker="XLK">—</span> |
| [**066570**](../snapshots/066570-2026-09-05.md)  | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 08-05 | ₩165,500 | ₩201,500 | 🟢 +21.8% | +1.0R | -35.1% | +68.3% | 관측 31일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**MSFT**](../snapshots/MSFT-2026-10-01.md) Microsoft | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-16 | $490.30 | $512.90 | 🟢 +4.6% | +1.0R | -8.8% | +17.6% | 14일 | <span class="js-shares" data-ticker="MSFT">—</span> | <span class="js-pnl" data-ticker="MSFT">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-10-01.md) Apple | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-13 | $318.73 | $333.02 | 🟢 +4.5% | +0.9R | -9.0% | +19.3% | 관측 80일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**PM**](../snapshots/PM-2026-10-01.md) Philip Morris | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 06-30 | $182.87 | $190.98 | 🟢 +4.4% | +0.8R | -9.3% | +20.9% | 관측 93일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-10-01.md) SOXX 반도체 ETF | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-18 | $529.02 | $568.64 | 🟢 +7.5% | +0.6R | -18.2% | +49.0% | 관측 75일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**XLV**](../snapshots/XLV-2026-10-01.md) XLV 헬스케어 섹터 ETF | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-11 | $165.36 | $168.41 | 🟢 +1.8% | +0.6R | -4.9% | +13.4% | 19일 | <span class="js-shares" data-ticker="XLV">—</span> | <span class="js-pnl" data-ticker="XLV">—</span> |
| [**USD**](../snapshots/USD-2026-09-18.md)  | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-16 | $79.68 | $84.65 | 🟢 +6.2% | +0.5R | -18.1% | +55.4% | 1일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**BE**](../snapshots/BE-2026-10-01.md) Bloom Energy | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-28 | $262.87 | $276.98 | 🟢 +5.4% | +0.3R | -19.8% | +68.6% | 2일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**009150**](../snapshots/009150-2026-09-05.md)  | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-13 | ₩1,289,000 | ₩1,401,000 | 🟢 +8.7% | +0.3R | -35.4% | +129.0% | 관측 54일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**AMD**](../snapshots/AMD-2026-10-01.md) Advanced Micro Devices | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-28 | $607.87 | $611.76 | 🟢 +0.6% | +0.1R | -9.1% | +41.8% | 2일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**PLTR**](../snapshots/PLTR-2026-10-01.md) Palantir | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-28 | $187.48 | $187.05 | 🔴 -0.2% | -0.0R | -7.2% | +37.4% | 2일 | <span class="js-shares" data-ticker="PLTR">—</span> | <span class="js-pnl" data-ticker="PLTR">—</span> |
| [**QCOM**](../snapshots/QCOM-2026-10-01.md) Qualcomm | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-28 | $187.48 | $184.04 | 🔴 -1.8% | -0.2R | -7.8% | +50.1% | 2일 | <span class="js-shares" data-ticker="QCOM">—</span> | <span class="js-pnl" data-ticker="QCOM">—</span> |
| [**278470**](../snapshots/278470-2026-09-04.md)  | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-02 | ₩432,500 | ₩406,000 | 🔴 -6.1% | -0.5R | -6.5% | +71.8% | 관측 2일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**LLY**](../snapshots/LLY-2026-10-01.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-09 | $1,215.83 | $1,159.25 | 🔴 -4.7% | -0.7R | -1.7% | +37.7% | 관측 84일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**XLE**](../snapshots/XLE-2026-10-01.md) XLE 에너지 섹터 ETF | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-11 | $65.14 | $61.50 | 🔴 -5.6% | -1.5R | +2.0% | +25.5% | 19일 | <span class="js-shares" data-ticker="XLE">—</span> | <span class="js-pnl" data-ticker="XLE">—</span> |

**합계** 18포지션 · 평균 +0.4R · 양의 R 13/18

<script type="application/json" id="pos-data">
[{"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 228.3800048828125, "r": 1.4201355203834396}, {"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 86.07499694824219, "r": 1.1159052208221714}, {"ticker": "XLK", "entry": 187.6699981689453, "stop": 180.24549056948115, "current": 195.75, "r": 1.0882879063438269}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 201500.0, "r": 1.0362833807227483}, {"ticker": "MSFT", "entry": 490.29998779296875, "stop": 467.75222603301404, "current": 512.9000244140625, "r": 1.0023184057777248}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 333.0199890136719, "r": 0.909850781323246}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 190.97999572753906, "r": 0.843926816968869}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 568.6400146484375, "r": 0.6222658308408942}, {"ticker": "XLV", "entry": 165.36000061035156, "stop": 160.2250376804351, "current": 168.41000366210938, "r": 0.5939678812457225}, {"ticker": "USD", "entry": 79.67520141601562, "stop": 69.30391305341799, "current": 84.6500015258789, "r": 0.4796704069866659}, {"ticker": "BE", "entry": 262.8699951171875, "stop": 222.03754390565308, "current": 276.97900390625, "r": 0.345534210424207}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1401000.0, "r": 0.2918140008068913}, {"ticker": "AMD", "entry": 607.8699951171875, "stop": 555.948517188526, "current": 611.760009765625, "r": 0.07492110786565552}, {"ticker": "PLTR", "entry": 187.47999572753906, "stop": 173.59302344922938, "current": 187.0500030517578, "r": -0.030963745528092067}, {"ticker": "QCOM", "entry": 187.47999572753906, "stop": 169.74023758658802, "current": 184.0399932861328, "r": -0.1939148445020361}, {"ticker": "278470", "entry": 432500.0, "stop": 379472.18390413764, "current": 406000.0, "r": -0.499737721653367}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1159.25, "r": -0.7433531265359468}, {"ticker": "XLE", "entry": 65.13999938964844, "stop": 62.72915451156144, "current": 61.5, "r": -1.5098438820073619}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

