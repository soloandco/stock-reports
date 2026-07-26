# 관찰 종목

모니터링 대상 종목. 30분 폴링으로 상태 변화 시 [알림](../alerts/index.md)이 발송됩니다. 판정·Stage·TT·현재가는 각 종목의 **최신 분석 스냅샷** 기준입니다. **경과**는 매수후보 연속 경과 거래일(D+N) — 전환일이 D+0이며, 백테스트상 후보는 **D+5 이내 진입이 우선**이고 D+10을 넘기면 기대값이 감쇠합니다(⚠ 표시). 이격·실질 손익비 등 진입 타이밍 상세는 각 종목 스냅샷의 '진입 · 손절 · 타겟' 표에 있습니다.

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
| [**009150**](009150.md) | [삼성전기](009150.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | ₩1,326,000 |  | 2 | 6/8 | KRX |
| [**066570**](066570.md) | [LG전자](066570.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | ₩169,200 |  | 2 | 5/8 | KRX |
| [**161890**](161890.md) | [한국콜마](161890.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | ₩100,200 |  | 2 | 7/8 | KRX |
| [**278470**](278470.md) | [에이피알](278470.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | ₩354,000 |  | 2 | 6/8 | KOSDAQ |
| [**329180**](329180.md) | [HD현대중공업](329180.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | ₩485,500 |  | 4 | 4/8 | KRX |
| [**AAPL**](AAPL.md) | [Apple](AAPL.md) | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | $333.02 | D+5 | 2 | 8/8 | NASDAQ |
| [**AMD**](AMD.md) | [Advanced Micro Devices](AMD.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> <span class="verdict-reason">(변동성과대)</span> | $521.95 |  | 2 | 8/8 | NASDAQ |
| [**APLD**](APLD.md) | [Applied Digital](APLD.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $27.19 |  | 3 | 5/8 | NASDAQ |
| [**ASTS**](ASTS.md) | [AST SpaceMobile](ASTS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $56.20 |  | 3 | 3/8 | NASDAQ |
| [**AVGO**](AVGO.md) | [Broadcom](AVGO.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $381.92 |  | 1 | 6/8 | NASDAQ |
| [**BA**](BA.md) | [Boeing](BA.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $209.52 |  | 3 | 2/8 | NYSE |
| [**BE**](BE.md) | [Bloom Energy](BE.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $184.89 |  | 3 | 5/8 | NYSE |
| [**CAT**](CAT.md) | [Caterpillar](CAT.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $888.73 |  | 2 | 7/8 | NYSE |
| [**CDNS**](CDNS.md) | [Cadence Design Systems](CDNS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $326.24 |  | 3 | 4/8 | NASDAQ |
| [**CIFR**](CIFR.md) | [Cipher Mining](CIFR.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> <span class="verdict-reason">(변동성과대)</span> | $23.15 |  | 2 | 8/8 | NASDAQ |
| [**CORZ**](CORZ.md) | [Core Scientific](CORZ.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $22.75 |  | 2 | 6/8 | NASDAQ |
| [**DHI**](DHI.md) | [D.R. Horton](DHI.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $146.76 |  | 3 | 2/8 | NYSE |
| [**DLR**](DLR.md) | [Digital Realty](DLR.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $199.08 |  | 2 | 7/8 | NYSE |
| [**GDXU**](GDXU.md) | [GDXU](GDXU.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $80.03 |  | 4 | 1/8 | NYSE |
| [**GEV**](GEV.md) | [GE Vernova](GEV.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $1,014.75 |  | 2 | 7/8 | NYSE |
| [**GOOGL**](GOOGL.md) | [Alphabet](GOOGL.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $319.74 |  | 3 | 6/8 | NASDAQ |
| [**GS**](GS.md) | [Goldman Sachs](GS.md) | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | $1,061.23 | D+19⚠ | 2 | 8/8 | NYSE |
| [**IREN**](IREN.md) | [IREN Limited](IREN.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $37.07 |  | 4 | 4/8 | NASDAQ |
| [**KMI**](KMI.md) | [Kinder Morgan](KMI.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $32.86 |  | 2 | 7/8 | NYSE |
| [**KO**](KO.md) | [Coca-Cola](KO.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $82.25 |  | 2 | 7/8 | NYSE |
| [**LLY**](LLY.md) | [Eli Lilly](LLY.md) | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | $1,196.03 | D+12⚠ | 2 | 8/8 | NYSE |
| [**LUNR**](LUNR.md) | [Intuitive Machines](LUNR.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $12.92 |  | 3 | 4/8 | NASDAQ |
| [**MS**](MS.md) | [Morgan Stanley](MS.md) | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | $214.48 | D+19⚠ | 2 | 8/8 | NYSE |
| [**MSFT**](MSFT.md) | [Microsoft](MSFT.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $381.70 |  | 4 | 0/8 | NASDAQ |
| [**NVDA**](NVDA.md) | [NVIDIA](NVDA.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $206.84 |  | 2 | 6/8 | NASDAQ |
| [**PCAR**](PCAR.md) | [Paccar](PCAR.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $132.24 |  | 2 | 6/8 | NASDAQ |
| [**PLTR**](PLTR.md) | [Palantir](PLTR.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $122.92 |  | 4 | 0/8 | NASDAQ |
| [**PM**](PM.md) | [Philip Morris](PM.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $193.00 |  | 2 | 7/8 | NYSE |
| [**PYPL**](PYPL.md) | [PayPal](PYPL.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $56.15 |  | 1 | 3/8 | NASDAQ |
| [**QCOM**](QCOM.md) | [Qualcomm](QCOM.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $166.97 |  | 3 | 3/8 | NASDAQ |
| [**QPUX**](QPUX.md) | [QPUX](QPUX.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $12.97 |  | 4 | 0/8 | NASDAQ |
| [**RDW**](RDW.md) | [RedWire](RDW.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $8.69 |  | 3 | 4/8 | NYSE |
| [**RKLB**](RKLB.md) | [Rocket Lab](RKLB.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $63.91 |  | 3 | 4/8 | NASDAQ |
| [**SKWD**](SKWD.md) | [Skyward Specialty Insurance](SKWD.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(이격과대)</span> | $60.46 |  | 2 | 7/8 | NASDAQ |
| [**SNPS**](SNPS.md) | [Synopsys](SNPS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $373.47 |  | 3 | 2/8 | NASDAQ |
| [**SOUN**](SOUN.md) | [SOUN](SOUN.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $6.16 |  | 4 | 0/8 | NASDAQ |
| [**SOXS**](SOXS.md) | [SOXS 반도체 베어 3X](SOXS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $51.53 |  | 4 | 1/8 | NYSE |
| [**SOXX**](SOXX.md) | [SOXX 반도체 ETF](SOXX.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $527.01 |  | 2 | 7/8 | NASDAQ |
| [**SPCX**](SPCX.md) | [SpaceX 추적 종목](SPCX.md) |  |  |  |  |  | NASDAQ |
| [**USD**](USD.md) | [ProShares Ultra Semiconductors (2x)](USD.md) | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | $85.74 |  | 2 | 6/8 | NASDAQ |
