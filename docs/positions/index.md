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
| [**MS**](../snapshots/MS-2026-07-07.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $220.71 | 🟢 +4.2% | +0.8R | -9.4% | +11.8% | 7일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**GEV**](../snapshots/GEV-2026-07-07.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $1,102.51 | $1,147.62 | 🟢 +4.1% | +0.5R | -12.6% | +22.1% | 7일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**BA**](../snapshots/BA-2026-07-07.md) Boeing | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-03 | $226.49 | $232.65 | 🟢 +2.7% | +0.5R | -8.5% | +14.9% | 4일 | <span class="js-shares" data-ticker="BA">—</span> | <span class="js-pnl" data-ticker="BA">—</span> |
| [**BE**](../snapshots/BE-2026-07-07.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $275.01 | $292.51 | 🟢 +6.4% | +0.3R | -25.8% | +53.5% | 7일 | <span class="js-shares" data-ticker="BE">—</span> | <span class="js-pnl" data-ticker="BE">—</span> |
| [**KO**](../snapshots/KO-2026-07-07.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $82.87 | 🟢 +0.3% | +0.1R | -4.0% | +10.8% | 7일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**PM**](../snapshots/PM-2026-07-07.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $183.12 | 🟢 +0.1% | +0.0R | -5.4% | +15.6% | 7일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**KMI**](../snapshots/KMI-2026-07-07.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $31.75 | 🟢 +0.1% | +0.0R | -4.6% | +13.3% | 5일 | <span class="js-shares" data-ticker="KMI">—</span> | <span class="js-pnl" data-ticker="KMI">—</span> |
| [**LLY**](../snapshots/LLY-2026-07-09.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,215.83 | ⚪ +0.0% | +0.0R | -6.3% | +18.8% | 0일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**GS**](../snapshots/GS-2026-07-07.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-25 | $1,076.91 | $1,049.20 | 🔴 -2.6% | -0.4R | -3.3% | +20.4% | 12일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**CAT**](../snapshots/CAT-2026-07-09.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $991.41 | $948.08 | 🔴 -4.4% | -0.5R | -3.7% | +29.5% | 7일 | <span class="js-shares" data-ticker="CAT">—</span> | <span class="js-pnl" data-ticker="CAT">—</span> |

**합계** 10포지션 · 평균 +0.1R · 양의 R 7/10

<script type="application/json" id="pos-data">
[{"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 220.7050018310547, "r": 0.7677255397123444}, {"ticker": "GEV", "entry": 1102.510009765625, "stop": 1002.9343461066205, "current": 1147.6199951171875, "r": 0.4530221913061111}, {"ticker": "BA", "entry": 226.49000549316406, "stop": 212.86704640762295, "current": 232.64500427246094, "r": 0.45181070725152184}, {"ticker": "BE", "entry": 275.010009765625, "stop": 217.05686725842352, "current": 292.5050048828125, "r": 0.30188173341960717}, {"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 82.87000274658203, "r": 0.07167907704836293}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 183.11500549316406, "r": 0.025495784360154674}, {"ticker": "KMI", "entry": 31.719999313354492, "stop": 30.30535238679012, "current": 31.7549991607666, "r": 0.024741047928553018}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1215.8299560546875, "r": 0.0}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1049.19921875, "r": -0.4458578601135539}, {"ticker": "CAT", "entry": 991.4099731445312, "stop": 912.5806793261623, "current": 948.0800170898438, "r": -0.5496682001810689}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

