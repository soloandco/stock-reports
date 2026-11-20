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

    예시: $100에 사서 손절을 $90에 뒀다면 1R = $10.
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
| [**KO**](../snapshots/KO-2026-11-21.md) Coca-Cola | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 06-30 | $82.65 | $96.99 | 🟢 +17.4% | +4.7R | -17.9% | +1.0% | 관측 144일 | <span class="js-shares" data-ticker="KO">—</span> | <span class="js-pnl" data-ticker="KO">—</span> |
| [**LH**](../snapshots/LH-2026-11-21.md) Labcorp | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-05 | $308.65 | $367.29 | 🟢 +19.0% | +4.1R | -19.9% | +3.7% | 46일 | <span class="js-shares" data-ticker="LH">—</span> | <span class="js-pnl" data-ticker="LH">—</span> |
| [**ADP**](../snapshots/ADP-2026-11-21.md) Automatic Data Processing | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-05 | $260.26 | $301.71 | 🟢 +15.9% | +3.5R | -17.7% | +6.0% | 46일 | <span class="js-shares" data-ticker="ADP">—</span> | <span class="js-pnl" data-ticker="ADP">—</span> |
| [**SKWD**](../snapshots/SKWD-2026-11-21.md) Skyward Specialty Insurance | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-02 | $55.01 | $64.43 | 🟢 +17.1% | +2.9R | -19.6% | +10.2% | 49일 | <span class="js-shares" data-ticker="SKWD">—</span> | <span class="js-pnl" data-ticker="SKWD">—</span> |
| [**SJM**](../snapshots/SJM-2026-11-21.md) J M Smucker | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-08 | $119.45 | $133.69 | 🟢 +11.9% | +2.4R | -15.0% | +11.1% | 43일 | <span class="js-shares" data-ticker="SJM">—</span> | <span class="js-pnl" data-ticker="SJM">—</span> |
| [**XLV**](../snapshots/XLV-2026-11-21.md) 헬스케어 섹터 ETF | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-11 | $165.36 | $177.32 | 🟢 +7.2% | +2.3R | -9.6% | +7.7% | 70일 | <span class="js-shares" data-ticker="XLV">—</span> | <span class="js-pnl" data-ticker="XLV">—</span> |
| [**AAPL**](../snapshots/AAPL-2026-11-21.md) Apple | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 07-13 | $318.73 | $342.56 | 🟢 +7.5% | +1.5R | -11.5% | +16.0% | 관측 131일 | <span class="js-shares" data-ticker="AAPL">—</span> | <span class="js-pnl" data-ticker="AAPL">—</span> |
| [**CB**](../snapshots/CB-2026-11-21.md) Chubb | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-21 | $354.95 | $371.65 | 🟢 +4.7% | +1.4R | -7.6% | +11.0% | 30일 | <span class="js-shares" data-ticker="CB">—</span> | <span class="js-pnl" data-ticker="CB">—</span> |
| [**CINF**](../snapshots/CINF-2026-11-21.md) Cincinnati Financial | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-30 | $181.19 | $186.54 | 🟢 +3.0% | +0.8R | -6.4% | +14.6% | 21일 | <span class="js-shares" data-ticker="CINF">—</span> | <span class="js-pnl" data-ticker="CINF">—</span> |
| [**ED**](../snapshots/ED-2026-11-21.md) Consolidated Edison | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 11-10 | $119.28 | $119.32 | 🟢 +0.0% | +0.0R | -3.7% | +18.5% | 10일 | <span class="js-shares" data-ticker="ED">—</span> | <span class="js-pnl" data-ticker="ED">—</span> |
| [**EVRG**](../snapshots/EVRG-2026-11-21.md) Evergy | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-30 | $85.93 | $85.93 | ⚪ +0.0% | +0.0R | -3.0% | +15.0% | 21일 | <span class="js-shares" data-ticker="EVRG">—</span> | <span class="js-pnl" data-ticker="EVRG">—</span> |
| [**REGN**](../snapshots/REGN-2026-11-21.md) Regeneron Pharmaceuticals | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 11-19 | $923.34 | $920.69 | 🔴 -0.3% | -0.0R | -6.0% | +31.6% | 1일 | <span class="js-shares" data-ticker="REGN">—</span> | <span class="js-pnl" data-ticker="REGN">—</span> |
| [**GEN**](../snapshots/GEN-2026-11-21.md) Gen Digital | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 11-12 | $29.69 | $29.19 | 🔴 -1.7% | -0.2R | -5.4% | +37.2% | 8일 | <span class="js-shares" data-ticker="GEN">—</span> | <span class="js-pnl" data-ticker="GEN">—</span> |
| [**MSFT**](../snapshots/MSFT-2026-11-21.md) Microsoft | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-16 | $490.30 | $484.52 | 🔴 -1.2% | -0.3R | -3.5% | +24.5% | 65일 | <span class="js-shares" data-ticker="MSFT">—</span> | <span class="js-pnl" data-ticker="MSFT">—</span> |
| [**DLTR**](../snapshots/DLTR-2026-11-21.md) Dollar Tree | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 11-12 | $141.27 | $137.96 | 🔴 -2.3% | -0.3R | -5.2% | +40.4% | 8일 | <span class="js-shares" data-ticker="DLTR">—</span> | <span class="js-pnl" data-ticker="DLTR">—</span> |
| [**ALLE**](../snapshots/ALLE-2026-11-21.md) Allegion | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 11-17 | $186.75 | $183.68 | 🔴 -1.6% | -0.4R | -3.1% | +25.6% | 3일 | <span class="js-shares" data-ticker="ALLE">—</span> | <span class="js-pnl" data-ticker="ALLE">—</span> |
| [**KMB**](../snapshots/KMB-2026-11-21.md) Kimberly Clark | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 11-02 | $108.25 | $106.38 | 🔴 -1.7% | -0.4R | -3.1% | +26.0% | 18일 | <span class="js-shares" data-ticker="KMB">—</span> | <span class="js-pnl" data-ticker="KMB">—</span> |
| [**OMC**](../snapshots/OMC-2026-11-21.md) Omnicom Group | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 11-04 | $87.51 | $85.16 | 🔴 -2.7% | -0.5R | -3.1% | +32.0% | 16일 | <span class="js-shares" data-ticker="OMC">—</span> | <span class="js-pnl" data-ticker="OMC">—</span> |
| [**ICE**](../snapshots/ICE-2026-11-21.md) Intercontinental Exchange | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 11-09 | $174.05 | $170.09 | 🔴 -2.3% | -0.5R | -2.4% | +25.9% | 11일 | <span class="js-shares" data-ticker="ICE">—</span> | <span class="js-pnl" data-ticker="ICE">—</span> |
| [**HUM**](../snapshots/HUM-2026-11-21.md) Humana | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-05 | $404.07 | $389.91 | 🔴 -3.5% | -0.5R | -3.5% | +39.3% | 46일 | <span class="js-shares" data-ticker="HUM">—</span> | <span class="js-pnl" data-ticker="HUM">—</span> |
| [**XLP**](../snapshots/XLP-2026-11-21.md) 필수소비재 섹터 ETF | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 11-04 | $91.96 | $90.50 | 🔴 -1.6% | -0.5R | -1.5% | +17.2% | 16일 | <span class="js-shares" data-ticker="XLP">—</span> | <span class="js-pnl" data-ticker="XLP">—</span> |
| [**PSA**](../snapshots/PSA-2026-11-21.md) Public Storage | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 11-02 | $333.24 | $325.72 | 🔴 -2.3% | -0.6R | -1.8% | +23.1% | 18일 | <span class="js-shares" data-ticker="PSA">—</span> | <span class="js-pnl" data-ticker="PSA">—</span> |
| [**BBY**](../snapshots/BBY-2026-11-21.md) Best Buy | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 11-10 | $104.10 | $97.95 | 🔴 -5.9% | -0.8R | -1.4% | +44.6% | 10일 | <span class="js-shares" data-ticker="BBY">—</span> | <span class="js-pnl" data-ticker="BBY">—</span> |
| [**PPG**](../snapshots/PPG-2026-11-21.md) PPG Industries | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 11-05 | $123.32 | $117.18 | 🔴 -5.0% | -0.9R | -0.8% | +35.3% | 15일 | <span class="js-shares" data-ticker="PPG">—</span> | <span class="js-pnl" data-ticker="PPG">—</span> |
| [**LLY**](../snapshots/LLY-2026-11-21.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 11-16 | $1,431.67 | $1,348.31 | 🔴 -5.8% | -1.0R | -0.2% | +38.2% | 4일 | <span class="js-shares" data-ticker="LLY">—</span> | <span class="js-pnl" data-ticker="LLY">—</span> |
| [**SWKS**](../snapshots/SWKS-2026-11-21.md) Skyworks Solutions | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-05 | $83.91 | $73.91 | 🔴 -11.9% | -1.2R | +1.9% | +71.7% | 46일 | <span class="js-shares" data-ticker="SWKS">—</span> | <span class="js-pnl" data-ticker="SWKS">—</span> |
| [**PYPL**](../snapshots/PYPL-2026-11-21.md) PayPal | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-29 | $56.95 | $53.29 | 🔴 -6.4% | -1.3R | +1.5% | +33.9% | 22일 | <span class="js-shares" data-ticker="PYPL">—</span> | <span class="js-pnl" data-ticker="PYPL">—</span> |
| [**PNW**](../snapshots/PNW-2026-11-21.md) Pinnacle West Capital | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-27 | $106.30 | $101.26 | 🔴 -4.7% | -1.4R | +1.4% | +22.7% | 24일 | <span class="js-shares" data-ticker="PNW">—</span> | <span class="js-pnl" data-ticker="PNW">—</span> |
| [**PSX**](../snapshots/PSX-2026-11-21.md) Phillips 66 | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-05 | $269.72 | $239.38 | 🔴 -11.3% | -1.8R | +5.7% | +47.8% | 46일 | <span class="js-shares" data-ticker="PSX">—</span> | <span class="js-pnl" data-ticker="PSX">—</span> |
| [**XLE**](../snapshots/XLE-2026-11-21.md) 에너지 섹터 ETF | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 09-11 | $65.14 | $60.58 | 🔴 -7.0% | -1.9R | +3.5% | +27.4% | 70일 | <span class="js-shares" data-ticker="XLE">—</span> | <span class="js-pnl" data-ticker="XLE">—</span> |
| [**DOCU**](../snapshots/DOCU-2026-11-21.md) DocuSign | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-23 | $85.27 | $74.56 | 🔴 -12.6% | -1.9R | +6.9% | +51.8% | 28일 | <span class="js-shares" data-ticker="DOCU">—</span> | <span class="js-pnl" data-ticker="DOCU">—</span> |
| [**NDSN**](../snapshots/NDSN-2026-11-21.md) Nordson | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | 10-05 | $334.43 | $307.22 | 🔴 -8.1% | -2.2R | +4.8% | +29.0% | 46일 | <span class="js-shares" data-ticker="NDSN">—</span> | <span class="js-pnl" data-ticker="NDSN">—</span> |

**합계** 32포지션 · 평균 +0.2R · 양의 R 10/32

<script type="application/json" id="pos-data">
[{"ticker": "KO", "entry": 82.6500015258789, "stop": 79.58074854770946, "current": 96.98999786376953, "r": 4.6721454503379665}, {"ticker": "LH", "entry": 308.6499938964844, "stop": 294.24045744138505, "current": 367.2900085449219, "r": 4.069528178866964}, {"ticker": "ADP", "entry": 260.260009765625, "stop": 248.3662021038046, "current": 301.7099914550781, "r": 3.485005211788418}, {"ticker": "SKWD", "entry": 55.0099983215332, "stop": 51.816288771641226, "current": 64.43000030517578, "r": 2.9495487415132025}, {"ticker": "SJM", "entry": 119.44999694824219, "stop": 113.63428139942769, "current": 133.69000244140625, "r": 2.448538855389311}, {"ticker": "XLV", "entry": 165.36000061035156, "stop": 160.2250376804351, "current": 177.32000732421875, "r": 2.329132045761768}, {"ticker": "AAPL", "entry": 318.7300109863281, "stop": 303.02416303776556, "current": 342.55999755859375, "r": 1.5172683862921645}, {"ticker": "CB", "entry": 354.95001220703125, "stop": 343.4057109171369, "current": 371.6499938964844, "r": 1.4465996053023975}, {"ticker": "CINF", "entry": 181.19000244140625, "stop": 174.6644377047669, "current": 186.5399932861328, "r": 0.819851010700691}, {"ticker": "ED", "entry": 119.27999877929688, "stop": 114.85268919586858, "current": 119.31999969482422, "r": 0.009035039175274694}, {"ticker": "EVRG", "entry": 85.93000030517578, "stop": 83.34433728969253, "current": 85.93000030517578, "r": 0.0}, {"ticker": "REGN", "entry": 923.3400268554688, "stop": 865.6940687789934, "current": 920.6900024414062, "r": -0.04597068905588964}, {"ticker": "GEN", "entry": 29.690000534057617, "stop": 27.620561911250434, "current": 29.190000534057617, "r": -0.2416114179418148}, {"ticker": "MSFT", "entry": 490.29998779296875, "stop": 467.75222603301404, "current": 484.5199890136719, "r": -0.25634468027608276}, {"ticker": "DLTR", "entry": 141.27000427246094, "stop": 130.79615666389455, "current": 137.9600067138672, "r": -0.31602498740640045}, {"ticker": "ALLE", "entry": 186.75, "stop": 177.97017673221018, "current": 183.6750030517578, "r": -0.3502344927059412}, {"ticker": "KMB", "entry": 108.25, "stop": 103.08834489929653, "current": 106.37999725341797, "r": -0.362287427210542}, {"ticker": "OMC", "entry": 87.51000213623047, "stop": 82.52298586621299, "current": 85.16000366210938, "r": -0.47122334215140993}, {"ticker": "ICE", "entry": 174.0500030517578, "stop": 166.04758127805644, "current": 170.08999633789062, "r": -0.4948510370799364}, {"ticker": "HUM", "entry": 404.07000732421875, "stop": 376.2195775037673, "current": 389.9100036621094, "r": -0.5084303457216751}, {"ticker": "XLP", "entry": 91.95999908447266, "stop": 89.1483521242496, "current": 90.49500274658203, "r": -0.5210456215222702}, {"ticker": "PSA", "entry": 333.239990234375, "stop": 319.71498797053954, "current": 325.7200012207031, "r": -0.5560064883522862}, {"ticker": "BBY", "entry": 104.09500122070312, "stop": 96.58620672795256, "current": 97.94999694824219, "r": -0.8183742781073162}, {"ticker": "PPG", "entry": 123.31999969482422, "stop": 116.26603572274874, "current": 117.18000030517578, "r": -0.8704324850473929}, {"ticker": "LLY", "entry": 1431.6700439453125, "stop": 1345.3723470477985, "current": 1348.31005859375, "r": -0.9659584015383366}, {"ticker": "SWKS", "entry": 83.91000366210938, "stop": 75.31621799170047, "current": 73.91000366210938, "r": -1.1636315337061676}, {"ticker": "PYPL", "entry": 56.95000076293945, "stop": 54.0682841670979, "current": 53.290000915527344, "r": -1.2700762638122203}, {"ticker": "PNW", "entry": 106.30000305175781, "stop": 102.71204127351827, "current": 101.26000213623047, "r": -1.4046974931823966}, {"ticker": "PSX", "entry": 269.7200012207031, "stop": 252.91199946436447, "current": 239.375, "r": -1.8053901743114336}, {"ticker": "XLE", "entry": 65.13999938964844, "stop": 62.72915451156144, "current": 60.58000183105469, "r": -1.8914520797423109}, {"ticker": "DOCU", "entry": 85.2699966430664, "stop": 79.68353783727808, "current": 74.55999755859375, "r": -1.9171356053633926}, {"ticker": "NDSN", "entry": 334.42999267578125, "stop": 322.0358625562242, "current": 307.2200012207031, "r": -2.195393399343343}]
</script>

!!! warning "투자 유의 / Disclaimer"
    자동 규칙이 낸 신호를 기록한 개인 사이트입니다. **투자 자문이 아니며**, 매매 판단과 책임은 본인에게 있습니다.
    수치는 yfinance 기준이며 늦거나 틀릴 수 있습니다.

