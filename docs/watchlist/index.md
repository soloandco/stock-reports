# 관찰 종목

모니터링 대상 종목. 30분 폴링으로 상태 변화 시 [알림](../alerts/index.md)이 발송됩니다. 판정·Stage·TT·현재가는 각 종목의 **최신 분석 스냅샷** 기준입니다. **경과**는 매수 상태 연속 경과 거래일(D+N) · 전환일이 D+0이며, 매수 추천은 **D+5까지만 유효**합니다. 이를 넘기면 '만료'로 표시되고 푸시 알림도 나가지 않습니다(백테스트상 지연 진입은 기대값 감쇠 — 비매수로 내려갔다 재전환하면 D+0 새 추천으로 부활). 관찰 등록 때 이미 매수 상태였던 종목은 전환일을 알 수 없어 '시작일 미상'으로 표시하고 새 추천으로 보지 않습니다. 이격·실질 손익비 등 진입 타이밍 상세는 각 종목 스냅샷의 '진입 · 손절 · 타겟' 표에 있습니다.

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
| [**AAPL**](AAPL.md) | [Apple](AAPL.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $337.00 | D+49 만료 | 2 | 7/7 | NASDAQ |
| [**AMD**](AMD.md) | [Advanced Micro Devices](AMD.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> <span class="verdict-reason">(변동성과대)</span> | $545.09 | D+49 만료 | 2 | 7/7 | NASDAQ |
| [**APLD**](APLD.md) | [Applied Digital](APLD.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $26.38 |  | 4 | 2/7 | NASDAQ |
| [**ASTS**](ASTS.md) | [AST SpaceMobile](ASTS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $62.71 |  | 4 | 1/7 | NASDAQ |
| [**AVGO**](AVGO.md) | [Broadcom](AVGO.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $347.30 |  | 3 | 2/7 | NASDAQ |
| [**BA**](BA.md) | [Boeing](BA.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $197.06 |  | 4 | 2/7 | NYSE |
| [**BE**](BE.md) | [Bloom Energy](BE.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(이격과대)</span> | $280.40 |  | 2 | 7/7 | NYSE |
| [**BITX**](BITX.md) | [2x Bitcoin Strategy ETF](BITX.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $16.65 |  | 1 | 2/7 | NYSE |
| [**CAT**](CAT.md) | [Caterpillar](CAT.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $798.45 |  | 3 | 4/7 | NYSE |
| [**CDNS**](CDNS.md) | [Cadence Design Systems](CDNS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $280.76 |  | 3 | 1/7 | NASDAQ |
| [**CIFR**](CIFR.md) | [Cipher Mining](CIFR.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $16.94 |  | 3 | 2/7 | NASDAQ |
| [**CORZ**](CORZ.md) | [Core Scientific](CORZ.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $17.14 |  | 3 | 2/7 | NASDAQ |
| [**DHI**](DHI.md) | [D.R. Horton](DHI.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $140.39 |  | 4 | 1/7 | NYSE |
| [**DLR**](DLR.md) | [Digital Realty](DLR.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $184.26 |  | 3 | 4/7 | NYSE |
| [**GDX**](GDX.md) | [GDX 금광주 ETF](GDX.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $95.93 |  | 1 | 6/7 | NYSE |
| [**GDXU**](GDXU.md) | [GDXU](GDXU.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $142.17 |  | 4 | 2/7 | NYSE |
| [**GEV**](GEV.md) | [GE Vernova](GEV.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $925.35 |  | 3 | 4/7 | NYSE |
| [**GOOGL**](GOOGL.md) | [Alphabet](GOOGL.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $347.33 |  | 1 | 6/7 | NASDAQ |
| [**GS**](GS.md) | [Goldman Sachs](GS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $951.11 |  | 3 | 4/7 | NYSE |
| [**IBIT**](IBIT.md) | [IBIT 비트코인 현물 ETF](IBIT.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $43.30 |  | 1 | 3/7 | NASDAQ |
| [**IONQ**](IONQ.md) | [IonQ](IONQ.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $40.37 |  | 4 | 2/7 | NYSE |
| [**IREN**](IREN.md) | [IREN Limited](IREN.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $43.48 |  | 4 | 2/7 | NASDAQ |
| [**KMI**](KMI.md) | [Kinder Morgan](KMI.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $31.33 |  | 3 | 4/7 | NYSE |
| [**KO**](KO.md) | [Coca-Cola](KO.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $88.07 | D+58 만료 | 2 | 7/7 | NYSE |
| [**LLY**](LLY.md) | [Eli Lilly](LLY.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $1,152.32 | D+51 만료 | 2 | 6/7 | NYSE |
| [**LUNR**](LUNR.md) | [Intuitive Machines](LUNR.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $14.79 |  | 4 | 3/7 | NASDAQ |
| [**MS**](MS.md) | [Morgan Stanley](MS.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $203.48 | D+58 만료 | 2 | 5/7 | NYSE |
| [**MSFT**](MSFT.md) | [Microsoft](MSFT.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $497.75 | D+1 | 2 | 6/7 | NASDAQ |
| [**NVDA**](NVDA.md) | [NVIDIA](NVDA.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $219.34 | D+33 만료 | 2 | 6/7 | NASDAQ |
| [**PCAR**](PCAR.md) | [Paccar](PCAR.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $117.36 |  | 3 | 4/7 | NASDAQ |
| [**PLTR**](PLTR.md) | [Palantir](PLTR.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $176.24 |  | 2 | 4/7 | NASDAQ |
| [**PM**](PM.md) | [Philip Morris](PM.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $190.51 | D+58 만료 | 2 | 7/7 | NYSE |
| [**PYPL**](PYPL.md) | [PayPal](PYPL.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $52.94 |  | 2 | 2/7 | NASDAQ |
| [**QCOM**](QCOM.md) | [Qualcomm](QCOM.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $188.71 | D+1 | 2 | 5/7 | NASDAQ |
| [**QPUX**](QPUX.md) | [QPUX](QPUX.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $13.18 |  | 4 | 0/7 | NASDAQ |
| [**RDW**](RDW.md) | [RedWire](RDW.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $11.55 |  | 1 | 6/7 | NYSE |
| [**RKLB**](RKLB.md) | [Rocket Lab](RKLB.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $67.82 |  | 4 | 3/7 | NASDAQ |
| [**SKWD**](SKWD.md) | [Skyward Specialty Insurance](SKWD.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $56.60 | D+29 만료 | 2 | 6/7 | NASDAQ |
| [**SNPS**](SNPS.md) | [Synopsys](SNPS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $381.17 |  | 4 | 0/7 | NASDAQ |
| [**SOUN**](SOUN.md) | [SOUN](SOUN.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $6.00 |  | 4 | 0/7 | NASDAQ |
| [**SOXS**](SOXS.md) | [SOXS 반도체 베어 3X](SOXS.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $44.98 |  | 4 | 1/7 | NYSE |
| [**SOXX**](SOXX.md) | [SOXX 반도체 ETF](SOXX.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $519.10 | D+44 만료 | 2 | 6/7 | NASDAQ |
| [**SPCX**](SPCX.md) | [SpaceX 추적 종목](SPCX.md) |  |  |  |  |  | NASDAQ |
| [**USD**](USD.md) | [ProShares Ultra Semiconductors (2x)](USD.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $84.65 | D+1 | 2 | 5/7 | NASDAQ |
| [**XLB**](XLB.md) | [XLB 소재 섹터 ETF](XLB.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $50.73 |  | 3 | 3/7 | NYSE |
| [**XLC**](XLC.md) | [XLC 커뮤니케이션 섹터 ETF](XLC.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $112.33 |  | 3 | 3/7 | NYSE |
| [**XLE**](XLE.md) | [XLE 에너지 섹터 ETF](XLE.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $64.47 | 시작일 미상 | 2 | 7/7 | NYSE |
| [**XLF**](XLF.md) | [XLF 파이낸셜 섹터 ETF](XLF.md) | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $55.88 |  | 2 | 3/7 | NYSE |
| [**XLI**](XLI.md) | [XLI 산업재 섹터 ETF](XLI.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $169.01 |  | 3 | 3/7 | NYSE |
| [**XLK**](XLK.md) | [XLK 테크놀로지 섹터 ETF](XLK.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $188.08 | 시작일 미상 | 2 | 7/7 | NYSE |
| [**XLP**](XLP.md) | [XLP 필수소비재 섹터 ETF](XLP.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $83.49 |  | 3 | 3/7 | NYSE |
| [**XLRE**](XLRE.md) | [XLRE 리츠 섹터 ETF](XLRE.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $42.94 |  | 3 | 3/7 | NYSE |
| [**XLU**](XLU.md) | [XLU 유틸리티 섹터 ETF](XLU.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $41.67 |  | 3 | 2/7 | NYSE |
| [**XLV**](XLV.md) | [XLV 헬스케어 섹터 ETF](XLV.md) | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $168.81 | 시작일 미상 | 2 | 7/7 | NYSE |
| [**XLY**](XLY.md) | [XLY 임의소비재 섹터 ETF](XLY.md) | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $111.39 |  | 4 | 1/7 | NYSE |
