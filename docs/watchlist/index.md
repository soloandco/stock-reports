# 관찰 종목

모니터링 대상 종목. 30분 폴링으로 상태 변화 시 [알림](../alerts/index.md)이 발송됩니다. 판정·Stage·TT·현재가는 각 종목의 **최신 분석 스냅샷** 기준입니다. **경과**는 매수 상태 연속 경과 거래일(D+N) · 전환일이 D+0이며, 매수 추천은 **D+5까지만 유효**합니다. 이를 넘기면 '만료'로 표시되고 푸시 알림도 나가지 않습니다(백테스트상 지연 진입은 기대값 감쇠 — 비매수로 내려갔다 재전환하면 D+0 새 추천으로 부활). 이격·실질 손익비 등 진입 타이밍 상세는 각 종목 스냅샷의 '진입 · 손절 · 타겟' 표에 있습니다.

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
<option value="buy">매수</option>
<option value="nobuy">매수불가</option>
</select>
</div>

| 종목 | 기업명 | 판정 | 현재가 | 경과 | Stage | TT | 시장 |
|------|--------|------|-------:|------|-------|----|------|
| [**009150**](009150.md) | [삼성전기](009150.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | ₩1,401,000 | D+40 만료 | 2 | 6/8 | KRX |
| [**066570**](066570.md) | [LG전자](066570.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | ₩201,500 | D+23 만료 | 2 | 7/8 | KRX |
| [**161890**](161890.md) | [한국콜마](161890.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(이격과대)</span> | ₩145,800 |  | 2 | 8/8 | KRX |
| [**329180**](329180.md) | [HD현대중공업](329180.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | ₩436,500 |  | 4 | 1/8 | KRX |
| [**AAPL**](AAPL.md) | [Apple](AAPL.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $328.21 | D+40 만료 | 2 | 7/8 | NASDAQ |
| [**AMD**](AMD.md) | [Advanced Micro Devices](AMD.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $456.16 | D+40 만료 | 2 | 7/8 | NASDAQ |
| [**APLD**](APLD.md) | [Applied Digital](APLD.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $25.91 |  | 4 | 2/8 | NASDAQ |
| [**ASTS**](ASTS.md) | [AST SpaceMobile](ASTS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $62.13 |  | 4 | 2/8 | NASDAQ |
| [**AVGO**](AVGO.md) | [Broadcom](AVGO.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $357.16 |  | 3 | 3/8 | NASDAQ |
| [**BA**](BA.md) | [Boeing](BA.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $210.51 |  | 4 | 3/8 | NYSE |
| [**BE**](BE.md) | [Bloom Energy](BE.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $235.55 | D+2 | 2 | 7/8 | NYSE |
| [**BITX**](BITX.md) | [2x Bitcoin Strategy ETF](BITX.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $19.18 |  | 1 | 3/8 | NYSE |
| [**CAT**](CAT.md) | [Caterpillar](CAT.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $800.14 |  | 3 | 5/8 | NYSE |
| [**CDNS**](CDNS.md) | [Cadence Design Systems](CDNS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $304.88 |  | 3 | 2/8 | NASDAQ |
| [**CIFR**](CIFR.md) | [Cipher Mining](CIFR.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $17.37 |  | 4 | 4/8 | NASDAQ |
| [**CORZ**](CORZ.md) | [Core Scientific](CORZ.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $17.90 |  | 3 | 3/8 | NASDAQ |
| [**DHI**](DHI.md) | [D.R. Horton](DHI.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $144.41 |  | 3 | 2/8 | NYSE |
| [**DLR**](DLR.md) | [Digital Realty](DLR.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $187.79 | D+1 | 2 | 7/8 | NYSE |
| [**GDX**](GDX.md) | [GDX 금광주 ETF](GDX.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $101.49 |  | 1 | 7/8 | NYSE |
| [**GDXU**](GDXU.md) | [GDXU](GDXU.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $173.82 |  | 4 | 3/8 | NYSE |
| [**GEV**](GEV.md) | [GE Vernova](GEV.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $941.84 |  | 3 | 6/8 | NYSE |
| [**GOOGL**](GOOGL.md) | [Alphabet](GOOGL.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $342.48 | D+1 | 2 | 6/8 | NASDAQ |
| [**GS**](GS.md) | [Goldman Sachs](GS.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $1,037.93 | D+52 만료 | 2 | 7/8 | NYSE |
| [**IBIT**](IBIT.md) | [IBIT 비트코인 현물 ETF](IBIT.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $46.35 |  | 1 | 3/8 | NASDAQ |
| [**IONQ**](IONQ.md) | [IonQ](IONQ.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $39.02 |  | 4 | 1/8 | NYSE |
| [**IREN**](IREN.md) | [IREN Limited](IREN.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $41.65 |  | 4 | 2/8 | NASDAQ |
| [**KMI**](KMI.md) | [Kinder Morgan](KMI.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $31.60 |  | 3 | 4/8 | NYSE |
| [**KO**](KO.md) | [Coca-Cola](KO.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $88.81 | D+49 만료 | 2 | 8/8 | NYSE |
| [**LLY**](LLY.md) | [Eli Lilly](LLY.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $1,159.60 | D+42 만료 | 2 | 7/8 | NYSE |
| [**LUNR**](LUNR.md) | [Intuitive Machines](LUNR.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $14.70 |  | 4 | 3/8 | NASDAQ |
| [**MS**](MS.md) | [Morgan Stanley](MS.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $217.15 | D+49 만료 | 2 | 8/8 | NYSE |
| [**MSFT**](MSFT.md) | [Microsoft](MSFT.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $510.12 |  | 2 | 5/8 | NASDAQ |
| [**NVDA**](NVDA.md) | [NVIDIA](NVDA.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $228.45 | D+24 만료 | 2 | 8/8 | NASDAQ |
| [**PCAR**](PCAR.md) | [Paccar](PCAR.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $124.51 | D+27 만료 | 2 | 6/8 | NASDAQ |
| [**PLTR**](PLTR.md) | [Palantir](PLTR.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $182.53 |  | 1 | 4/8 | NASDAQ |
| [**PM**](PM.md) | [Philip Morris](PM.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $186.17 | D+49 만료 | 2 | 6/8 | NYSE |
| [**PYPL**](PYPL.md) | [PayPal](PYPL.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $56.82 |  | 2 | 4/8 | NASDAQ |
| [**QCOM**](QCOM.md) | [Qualcomm](QCOM.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $168.57 |  | 1 | 3/8 | NASDAQ |
| [**QPUX**](QPUX.md) | [QPUX](QPUX.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $13.43 |  | 4 | 0/8 | NASDAQ |
| [**RDW**](RDW.md) | [RedWire](RDW.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $10.37 |  | 3 | 3/8 | NYSE |
| [**RKLB**](RKLB.md) | [Rocket Lab](RKLB.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $63.81 |  | 4 | 3/8 | NASDAQ |
| [**SKWD**](SKWD.md) | [Skyward Specialty Insurance](SKWD.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $58.09 | D+20 만료 | 2 | 7/8 | NASDAQ |
| [**SNPS**](SNPS.md) | [Synopsys](SNPS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $416.31 |  | 4 | 1/8 | NASDAQ |
| [**SOUN**](SOUN.md) | [SOUN](SOUN.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $6.74 |  | 4 | 1/8 | NASDAQ |
| [**SOXS**](SOXS.md) | [SOXS 반도체 베어 3X](SOXS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $51.60 |  | 4 | 2/8 | NYSE |
| [**SOXX**](SOXX.md) | [SOXX 반도체 ETF](SOXX.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $502.20 | D+35 만료 | 2 | 7/8 | NASDAQ |
| [**SPCX**](SPCX.md) | [SpaceX 추적 종목](SPCX.md) |  |  |  |  |  | NASDAQ |
| [**USD**](USD.md) | [ProShares Ultra Semiconductors (2x)](USD.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $85.17 | D+26 만료 | 2 | 6/8 | NASDAQ |
