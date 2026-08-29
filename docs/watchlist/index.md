# 관찰 종목

모니터링 대상 종목. 30분 폴링으로 상태 변화 시 [알림](../alerts/index.md)이 발송됩니다. 판정·Stage·TT·현재가는 각 종목의 **최신 분석 스냅샷** 기준입니다. **경과**는 매수후보 연속 경과 거래일(D+N) — 전환일이 D+0이며, 매수 추천은 **D+5까지만 유효**합니다. 이를 넘기면 '만료'로 표시되고 푸시 알림도 나가지 않습니다(백테스트상 지연 진입은 기대값 감쇠 — 비매수로 내려갔다 재전환하면 D+0 새 추천으로 부활). 이격·실질 손익비 등 진입 타이밍 상세는 각 종목 스냅샷의 '진입 · 손절 · 타겟' 표에 있습니다.

<div class="snap-filters">
<label class="sf-label" for="sf-market">시장</label>
<select class="sf-select" id="sf-market" data-f="market">
<option value="">전체</option>
<option value="KRX">KRX</option>
<option value="KOSDAQ">KOSDAQ</option>
<option value="NASDAQ">NASDAQ</option>
<option value="NYSE">NYSE</option>
</select>
<label class="sf-label" for="sf-verdict">판정</label>
<select class="sf-select" id="sf-verdict" data-f="verdict">
<option value="">전체</option>
<option value="cand">매수후보</option>
<option value="watch">매수관찰</option>
<option value="nobuy">매수불가</option>
</select>
</div>

| 종목 | 기업명 | 판정 | 현재가 | 경과 | Stage | TT | 시장 |
|------|--------|------|-------:|------|-------|----|------|
| [**009150**](009150.md) | [삼성전기](009150.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | ₩1,421,000 |  | 2 | 6/8 | KRX |
| [**066570**](066570.md) | [LG전자](066570.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | ₩201,500 |  | 2 | 7/8 | KRX |
| [**161890**](161890.md) | [한국콜마](161890.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(과열)</span> | ₩161,700 |  | 2 | 8/8 | KRX |
| [**278470**](278470.md) | [에이피알](278470.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(이격과대)</span> | ₩461,500 |  | 2 | 8/8 | KOSDAQ |
| [**329180**](329180.md) | [HD현대중공업](329180.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | ₩457,000 |  | 4 | 1/8 | KRX |
| [**AAPL**](AAPL.md) | [Apple](AAPL.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $314.58 |  | 2 | 7/8 | NASDAQ |
| [**AMD**](AMD.md) | [Advanced Micro Devices](AMD.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $476.67 |  | 2 | 7/8 | NASDAQ |
| [**APLD**](APLD.md) | [Applied Digital](APLD.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $27.44 |  | 4 | 2/8 | NASDAQ |
| [**ASTS**](ASTS.md) | [AST SpaceMobile](ASTS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $61.44 |  | 4 | 2/8 | NASDAQ |
| [**AVGO**](AVGO.md) | [Broadcom](AVGO.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $371.54 |  | 3 | 5/8 | NASDAQ |
| [**BA**](BA.md) | [Boeing](BA.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $209.89 |  | 3 | 3/8 | NYSE |
| [**BE**](BE.md) | [Bloom Energy](BE.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $217.83 |  | 2 | 6/8 | NYSE |
| [**BITX**](BITX.md) | [2x Bitcoin Strategy ETF](BITX.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $18.43 |  | 1 | 2/8 | NYSE |
| [**CAT**](CAT.md) | [Caterpillar](CAT.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $817.00 |  | 3 | 6/8 | NYSE |
| [**CDNS**](CDNS.md) | [Cadence Design Systems](CDNS.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $347.55 |  | 2 | 5/8 | NASDAQ |
| [**CIFR**](CIFR.md) | [Cipher Mining](CIFR.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $16.77 |  | 3 | 3/8 | NASDAQ |
| [**CORZ**](CORZ.md) | [Core Scientific](CORZ.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $17.62 |  | 3 | 3/8 | NASDAQ |
| [**DHI**](DHI.md) | [D.R. Horton](DHI.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $145.26 |  | 3 | 2/8 | NYSE |
| [**DLR**](DLR.md) | [Digital Realty](DLR.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $192.10 |  | 2 | 7/8 | NYSE |
| [**GDX**](GDX.md) | [GDX 금광주 ETF](GDX.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $103.69 |  | 1 | 7/8 | NYSE |
| [**GDXU**](GDXU.md) | [GDXU](GDXU.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $189.93 |  | 4 | 2/8 | NYSE |
| [**GEV**](GEV.md) | [GE Vernova](GEV.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $953.83 |  | 3 | 6/8 | NYSE |
| [**GOOGL**](GOOGL.md) | [Alphabet](GOOGL.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $340.65 |  | 3 | 5/8 | NASDAQ |
| [**GS**](GS.md) | [Goldman Sachs](GS.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $1,040.87 |  | 2 | 7/8 | NYSE |
| [**IBIT**](IBIT.md) | [IBIT 비트코인 현물 ETF](IBIT.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $45.29 |  | 1 | 3/8 | NASDAQ |
| [**IREN**](IREN.md) | [IREN Limited](IREN.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $40.53 |  | 4 | 2/8 | NASDAQ |
| [**KMI**](KMI.md) | [Kinder Morgan](KMI.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $31.54 |  | 3 | 5/8 | NYSE |
| [**KO**](KO.md) | [Coca-Cola](KO.md) | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | $89.06 | D+7 만료 | 2 | 8/8 | NYSE |
| [**LLY**](LLY.md) | [Eli Lilly](LLY.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $1,176.10 |  | 2 | 7/8 | NYSE |
| [**LUNR**](LUNR.md) | [Intuitive Machines](LUNR.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $16.18 |  | 4 | 3/8 | NASDAQ |
| [**MS**](MS.md) | [Morgan Stanley](MS.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $214.86 |  | 2 | 7/8 | NYSE |
| [**MSFT**](MSFT.md) | [Microsoft](MSFT.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $505.06 |  | 2 | 4/8 | NASDAQ |
| [**NVDA**](NVDA.md) | [NVIDIA](NVDA.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $227.98 |  | 2 | 7/8 | NASDAQ |
| [**PCAR**](PCAR.md) | [Paccar](PCAR.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $126.54 |  | 2 | 6/8 | NASDAQ |
| [**PLTR**](PLTR.md) | [Palantir](PLTR.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $185.93 |  | 1 | 5/8 | NASDAQ |
| [**PM**](PM.md) | [Philip Morris](PM.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $190.48 |  | 2 | 7/8 | NYSE |
| [**PYPL**](PYPL.md) | [PayPal](PYPL.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $61.47 |  | 2 | 5/8 | NASDAQ |
| [**QCOM**](QCOM.md) | [Qualcomm](QCOM.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $164.78 |  | 4 | 2/8 | NASDAQ |
| [**QPUX**](QPUX.md) | [QPUX](QPUX.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $16.29 |  | 4 | 1/8 | NASDAQ |
| [**RDW**](RDW.md) | [RedWire](RDW.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $11.27 |  | 3 | 4/8 | NYSE |
| [**RKLB**](RKLB.md) | [Rocket Lab](RKLB.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $67.53 |  | 4 | 3/8 | NASDAQ |
| [**SKWD**](SKWD.md) | [Skyward Specialty Insurance](SKWD.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $57.65 |  | 2 | 7/8 | NASDAQ |
| [**SNPS**](SNPS.md) | [Synopsys](SNPS.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $464.89 |  | 1 | 4/8 | NASDAQ |
| [**SOUN**](SOUN.md) | [SOUN](SOUN.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $7.22 |  | 4 | 2/8 | NASDAQ |
| [**SOXS**](SOXS.md) | [SOXS 반도체 베어 3X](SOXS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $45.35 |  | 4 | 1/8 | NYSE |
| [**SOXX**](SOXX.md) | [SOXX 반도체 ETF](SOXX.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $525.43 |  | 2 | 7/8 | NASDAQ |
| [**SPCX**](SPCX.md) | [SpaceX 추적 종목](SPCX.md) |  |  |  |  |  | NASDAQ |
| [**USD**](USD.md) | [ProShares Ultra Semiconductors (2x)](USD.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $88.82 |  | 2 | 7/8 | NASDAQ |
