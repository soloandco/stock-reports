# 오픈 포지션

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
| [**KO**](../snapshots/KO-2026-09-09.md) Coca-Cola | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 06-30 | $82.65 | $88.42 | 🟢 +7.0% | +1.9R | -10.0% | +10.8% | 관측 71일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-09-09.md) NVIDIA | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 08-04 | $206.64 | $225.73 | 🟢 +9.2% | +1.2R | -15.2% | +25.5% | 관측 36일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**066570**](../snapshots/066570-2026-09-05.md)  | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 08-05 | ₩165,500 | ₩201,500 | 🟢 +21.8% | +1.0R | -35.1% | +68.3% | 관측 31일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**USD**](../snapshots/USD-2026-09-09.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-31 | $77.55 | $89.64 | 🟢 +15.6% | +0.8R | -31.1% | +74.7% | 관측 40일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**MS**](../snapshots/MS-2026-09-09.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 06-30 | $211.72 | $216.30 | 🟢 +2.2% | +0.4R | -7.5% | +24.9% | 관측 71일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**009150**](../snapshots/009150-2026-09-05.md)  | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-13 | ₩1,289,000 | ₩1,401,000 | 🟢 +8.7% | +0.3R | -35.4% | +129.0% | 관측 54일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**PM**](../snapshots/PM-2026-09-09.md) Philip Morris | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 06-30 | $182.87 | $184.78 | 🟢 +1.0% | +0.2R | -6.2% | +25.0% | 관측 71일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**DLR**](../snapshots/DLR-2026-09-09.md) Digital Realty | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-04 | $187.79 | $189.52 | 🟢 +0.9% | +0.2R | -6.6% | +27.5% | 관측 5일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**GEV**](../snapshots/GEV-2026-09-09.md) GE Vernova | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-08 | $971.38 | $971.38 | ⚪ +0.0% | +0.0R | -9.1% | +45.7% | 0일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**KMI**](../snapshots/KMI-2026-09-09.md) Kinder Morgan | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-08 | $31.98 | $31.98 | ⚪ +0.0% | +0.0R | -4.7% | +23.3% | 0일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-09-09.md) SOXX 반도체 ETF | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-18 | $529.02 | $528.40 | 🔴 -0.1% | -0.0R | -11.9% | +60.4% | 관측 53일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-09-09.md) Apple | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-13 | $318.73 | $316.22 | 🔴 -0.8% | -0.2R | -4.2% | +25.6% | 관측 58일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**278470**](../snapshots/278470-2026-09-04.md)  | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-02 | ₩432,500 | ₩406,000 | 🔴 -6.1% | -0.5R | -6.5% | +71.8% | 관측 2일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**AMD**](../snapshots/AMD-2026-09-09.md) Advanced Micro Devices | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-13 | $543.98 | $505.74 | 🔴 -7.0% | -0.6R | -6.0% | +75.3% | 관측 58일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**GS**](../snapshots/GS-2026-09-09.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 06-25 | $1,076.91 | $1,036.68 | 🔴 -3.7% | -0.6R | -2.1% | +33.9% | 관측 76일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**LLY**](../snapshots/LLY-2026-09-09.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-09 | $1,215.83 | $1,123.86 | 🔴 -7.6% | -1.2R | +1.4% | +42.0% | 관측 62일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-09-09.md) Paccar | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-30 | $133.87 | $122.50 | 🔴 -8.5% | -1.6R | +3.5% | +38.2% | 관측 41일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-09-09.md) Skyward Specialty Insurance | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 08-08 | $63.67 | $56.53 | 🔴 -11.2% | -1.7R | +5.0% | +50.7% | 관측 32일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |

**합계** 18포지션 · 평균 -0.0R · 양의 R 8/18

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 88.41999816894531, "r": 1.8799351777473006}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 225.72999572753906, "r": 1.2470273704370893}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 201500.0, "r": 1.0362833807227483}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 89.6449966430664, "r": 0.7649214318010809}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 216.30499267578125, "r": 0.39176569842087194}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1401000.0, "r": 0.2918140008068913}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 184.77999877929688, "r": 0.19875501721977962}, {"ticker": "DLR", "entry": 187.7899932861328, "stop": 177.01335135985073, "current": 189.52000427246094, "r": 0.1605334016071345}, {"ticker": "GEV", "entry": 971.3800048828125, "stop": 882.5460238522224, "current": 971.3800048828125, "r": 0.0}, {"ticker": "KMI", "entry": 31.979999542236328, "stop": 30.486922988132996, "current": 31.979999542236328, "r": 0.0}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 528.4000244140625, "r": -0.009737552353877323}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 316.2200012207031, "r": -0.15981370594223293}, {"ticker": "278470", "entry": 432500.0, "stop": 379472.18390413764, "current": 406000.0, "r": -0.499737721653367}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 505.739990234375, "r": -0.558522626771728}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1036.6800537109375, "r": -0.6472870872284259}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1123.8599853515625, "r": -1.2083106816751132}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 122.5, "r": -1.6050121194030729}, {"ticker": "SKWD", "entry": 63.66999816894531, "stop": 59.36272420763139, "current": 56.529998779296875, "r": -1.6576608439065705}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

