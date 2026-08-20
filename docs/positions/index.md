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
| [**KO**](../snapshots/KO-2026-08-21.md) Coca-Cola | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $82.65 | $90.54 | 🟢 +9.5% | +2.6R | -12.1% | +1.5% | 52일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**066570**](../snapshots/066570-2026-08-21.md) LG전자 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-05 | ₩165,500 | ₩201,500 | 🟢 +21.8% | +1.0R | -35.1% | +33.9% | 16일 | <span class="js-shares" data-ticker="066570">—</span> | <span class="js-pnl" data-ticker="066570">—</span> |
| [**PM**](../snapshots/PM-2026-08-21.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $191.52 | 🟢 +4.7% | +0.9R | -9.5% | +10.5% | 52일 | <span class="js-shares" data-ticker="PM">—</span> | <span class="js-pnl" data-ticker="PM">—</span> |
| [**278470**](../snapshots/278470-2026-08-21.md) 에이피알 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | ₩338,000 | ₩383,500 | 🟢 +13.5% | +0.9R | -25.3% | +28.3% | 17일 | <span class="js-shares" data-ticker="278470">—</span> | <span class="js-pnl" data-ticker="278470">—</span> |
| [**NVDA**](../snapshots/NVDA-2026-08-21.md) NVIDIA | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-04 | $206.64 | $216.85 | 🟢 +4.9% | +0.7R | -11.8% | +16.5% | 17일 | <span class="js-shares" data-ticker="NVDA">—</span> | <span class="js-pnl" data-ticker="NVDA">—</span> |
| [**USD**](../snapshots/USD-2026-08-21.md) ProShares Ultra Semiconductors (2x) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $77.55 | $85.34 | 🟢 +10.0% | +0.5R | -27.7% | +46.5% | 21일 | <span class="js-shares" data-ticker="USD">—</span> | <span class="js-pnl" data-ticker="USD">—</span> |
| [**LLY**](../snapshots/LLY-2026-08-21.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,245.69 | 🟢 +2.5% | +0.4R | -8.5% | +15.9% | 43일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**009150**](../snapshots/009150-2026-08-21.md) 삼성전기 | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | ₩1,289,000 | ₩1,387,000 | 🟢 +7.6% | +0.3R | -34.7% | +75.9% | 39일 | <span class="js-shares" data-ticker="009150">—</span> | <span class="js-pnl" data-ticker="009150">—</span> |
| [**SOXX**](../snapshots/SOXX-2026-08-21.md) SOXX 반도체 ETF | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-18 | $529.02 | $522.35 | 🔴 -1.3% | -0.1R | -10.9% | +37.8% | 34일 | <span class="js-shares" data-ticker="SOXX">—</span> | <span class="js-pnl" data-ticker="SOXX">—</span> |
| [**GEV**](../snapshots/GEV-2026-08-21.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-31 | $982.55 | $966.56 | 🔴 -1.6% | -0.1R | -11.1% | +40.0% | 21일 | <span class="js-shares" data-ticker="GEV">—</span> | <span class="js-pnl" data-ticker="GEV">—</span> |
| [**MS**](../snapshots/MS-2026-08-21.md) Morgan Stanley | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $211.72 | $207.49 | 🔴 -2.0% | -0.4R | -3.6% | +19.0% | 52일 | <span class="js-shares" data-ticker="MS">—</span> | <span class="js-pnl" data-ticker="MS">—</span> |
| [**DLR**](../snapshots/DLR-2026-08-21.md) Digital Realty | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-25 | $199.08 | $194.22 | 🔴 -2.4% | -0.4R | -3.4% | +20.2% | 27일 | <span class="js-shares" data-ticker="DLR">—</span> | <span class="js-pnl" data-ticker="DLR">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-08-21.md) Apple | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $318.73 | $311.30 | 🔴 -2.3% | -0.5R | -2.7% | +17.5% | 39일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**PCAR**](../snapshots/PCAR-2026-08-21.md) Paccar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-30 | $133.87 | $128.94 | 🔴 -3.7% | -0.7R | -1.7% | +20.3% | 22일 | <span class="js-shares" data-ticker="PCAR">—</span> | <span class="js-pnl" data-ticker="PCAR">—</span> |
| [**RDW**](../snapshots/RDW-2026-08-21.md) RedWire | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-08 | $13.59 | $11.76 | 🔴 -13.5% | -0.8R | -4.0% | +74.3% | 13일 | <span class="js-shares" data-ticker="RDW">—</span> | <span class="js-pnl" data-ticker="RDW">—</span> |
| [**AMD**](../snapshots/AMD-2026-08-21.md) Advanced Micro Devices | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-13 | $543.98 | $469.45 | 🔴 -13.7% | -1.1R | +1.3% | +59.6% | 39일 | <span class="js-shares" data-ticker="AMD">—</span> | <span class="js-pnl" data-ticker="AMD">—</span> |
| [**GS**](../snapshots/GS-2026-08-21.md) Goldman Sachs | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-25 | $1,076.91 | $1,002.28 | 🔴 -6.9% | -1.2R | +1.2% | +26.0% | 57일 | <span class="js-shares" data-ticker="GS">—</span> | <span class="js-pnl" data-ticker="GS">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-08-21.md) Skyward Specialty Insurance | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 08-08 | $63.67 | $55.86 | 🔴 -12.3% | -1.8R | +6.3% | +37.1% | 13일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |

**합계** 18포지션 · 평균 +0.0R · 양의 R 8/18

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 90.53500366210938, "r": 2.5690297255761627}, {"ticker": "066570", "entry": 165500.0, "stop": 130760.46767739143, "current": 201500.0, "r": 1.0362833807227483}, {"ticker": "PM", "entry": 182.8699951171875, "stop": 173.26015638794763, "current": 191.52000427246094, "r": 0.9001201163713647}, {"ticker": "278470", "entry": 338000.0, "stop": 286622.8624105194, "current": 383500.0, "r": 0.8856079208530304}, {"ticker": "NVDA", "entry": 206.63999938964844, "stop": 191.33159735257087, "current": 216.85000610351562, "r": 0.6669544403875818}, {"ticker": "USD", "entry": 77.55000305175781, "stop": 61.73792995710053, "current": 85.33999633789062, "r": 0.4926610975992113}, {"ticker": "LLY", "entry": 1215.8299560546875, "stop": 1139.715449994355, "current": 1245.68994140625, "r": 0.39230347665783727}, {"ticker": "009150", "entry": 1289000.0, "stop": 905193.8779828583, "current": 1387000.0, "r": 0.2553372507060299}, {"ticker": "SOXX", "entry": 529.02001953125, "stop": 465.34948974553555, "current": 522.3499755859375, "r": -0.10475873167320553}, {"ticker": "GEV", "entry": 982.5499877929688, "stop": 859.1024131708681, "current": 966.5579833984375, "r": -0.12954490554785045}, {"ticker": "MS", "entry": 211.72000122070312, "stop": 200.01659922925953, "current": 207.49000549316406, "r": -0.3614330030389137}, {"ticker": "DLR", "entry": 199.0800018310547, "stop": 187.63590914129668, "current": 194.22000122070312, "r": -0.42467330019976707}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 311.29998779296875, "r": -0.47307367406669615}, {"ticker": "PCAR", "entry": 133.8699951171875, "stop": 126.7859395018217, "current": 128.94000244140625, "r": -0.6959280027513844}, {"ticker": "RDW", "entry": 13.59000015258789, "stop": 11.286366858996743, "current": 11.760100364685059, "r": -0.7943537684551305}, {"ticker": "AMD", "entry": 543.9849853515625, "stop": 475.5097020165894, "current": 469.4549865722656, "r": -1.0884219115195892}, {"ticker": "GS", "entry": 1076.9100341796875, "stop": 1014.7583533219587, "current": 1002.280029296875, "r": -1.2007721087004513}, {"ticker": "SKWD", "entry": 63.66999816894531, "stop": 59.36272420763139, "current": 55.86000061035156, "r": -1.8132112395774627}]
</script>

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

