# 관찰 종목

판정·현재가는 각 종목의 **최신 분석 스냅샷** 기준입니다. 표는 옆으로 밀면 더 보입니다.

??? info "경과·만료 표시 설명"
    30분 폴링으로 상태가 바뀌면 [알림](../alerts/index.md)이 발송됩니다. **경과**는 매수 상태 연속 경과 거래일(D+N) · 전환일이 D+0이며, 매수 추천은 **D+5까지만 유효**합니다. 이를 넘기면 '만료'로 표시되고 푸시 알림도 나가지 않습니다(백테스트상 지연 진입은 기대값 감쇠 — 비매수로 내려갔다 재전환하면 D+0 새 추천으로 부활). 관찰 등록 때 이미 매수 상태였던 종목은 전환일을 알 수 없어 '시작일 미상'으로 표시하고 새 추천으로 보지 않습니다. 이격·실질 손익비 등 진입 타이밍 상세는 각 종목 스냅샷의 '진입 · 손절 · 타겟' 표에 있습니다.

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

| 종목 | 판정 | 현재가 | 경과 | Stage | TT | 시장 |
|------|------|-------:|------|-------|----|------|
| [**AAPL**](AAPL.md)<br><span class="wl-name">Apple</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $339.75 | D+52 만료 | 2 | 7/7 | NASDAQ |
| [**AMD**](AMD.md)<br><span class="wl-name">Advanced Micro Devices</span> | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(과열)</span> | $623.77 |  | 2 | 7/7 | NASDAQ |
| [**APLD**](APLD.md)<br><span class="wl-name">Applied Digital</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $28.54 |  | 4 | 3/7 | NASDAQ |
| [**ASTS**](ASTS.md)<br><span class="wl-name">AST SpaceMobile</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $63.69 |  | 4 | 3/7 | NASDAQ |
| [**AVGO**](AVGO.md)<br><span class="wl-name">Broadcom</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $364.54 |  | 3 | 2/7 | NASDAQ |
| [**BA**](BA.md)<br><span class="wl-name">Boeing</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $197.72 |  | 4 | 2/7 | NYSE |
| [**BE**](BE.md)<br><span class="wl-name">Bloom Energy</span> | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(이격과대)</span> | $276.45 |  | 2 | 7/7 | NYSE |
| [**CAT**](CAT.md)<br><span class="wl-name">Caterpillar</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $808.30 |  | 3 | 5/7 | NYSE |
| [**CDNS**](CDNS.md)<br><span class="wl-name">Cadence Design Systems</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $302.95 |  | 3 | 1/7 | NASDAQ |
| [**CIFR**](CIFR.md)<br><span class="wl-name">Cipher Mining</span> | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $19.09 |  | 1 | 4/7 | NASDAQ |
| [**CORZ**](CORZ.md)<br><span class="wl-name">Core Scientific</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $18.79 |  | 3 | 3/7 | NASDAQ |
| [**DHI**](DHI.md)<br><span class="wl-name">D.R. Horton</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $144.13 |  | 4 | 1/7 | NYSE |
| [**DLR**](DLR.md)<br><span class="wl-name">Digital Realty</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $185.67 | D+1 | 2 | 5/7 | NYSE |
| [**GDX**](GDX.md)<br><span class="wl-name">GDX 금광주 ETF</span> | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $97.81 |  | 1 | 6/7 | NYSE |
| [**GDXU**](GDXU.md)<br><span class="wl-name">GDXU</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $151.70 |  | 4 | 3/7 | NYSE |
| [**GEV**](GEV.md)<br><span class="wl-name">GE Vernova</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $950.47 |  | 3 | 5/7 | NYSE |
| [**GOOGL**](GOOGL.md)<br><span class="wl-name">Alphabet</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $351.16 | D+2 | 2 | 6/7 | NASDAQ |
| [**GS**](GS.md)<br><span class="wl-name">Goldman Sachs</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $950.01 |  | 3 | 4/7 | NYSE |
| [**IBIT**](IBIT.md)<br><span class="wl-name">IBIT 비트코인 현물 ETF</span> | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $48.83 |  | 1 | 3/7 | NASDAQ |
| [**INOD**](INOD.md)<br><span class="wl-name">Innodata</span> | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $64.24 |  | 2 | 4/7 | NASDAQ |
| [**IONQ**](IONQ.md)<br><span class="wl-name">IonQ</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $40.74 |  | 3 | 2/7 | NYSE |
| [**IREN**](IREN.md)<br><span class="wl-name">IREN Limited</span> | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $48.55 |  | 1 | 3/7 | NASDAQ |
| [**KMI**](KMI.md)<br><span class="wl-name">Kinder Morgan</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $31.28 |  | 3 | 4/7 | NYSE |
| [**KO**](KO.md)<br><span class="wl-name">Coca-Cola</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $88.61 | D+61 만료 | 2 | 7/7 | NYSE |
| [**LLY**](LLY.md)<br><span class="wl-name">Eli Lilly</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $1,170.50 | D+54 만료 | 2 | 6/7 | NYSE |
| [**LUNR**](LUNR.md)<br><span class="wl-name">Intuitive Machines</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $16.24 |  | 4 | 4/7 | NASDAQ |
| [**MS**](MS.md)<br><span class="wl-name">Morgan Stanley</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $200.22 | D+61 만료 | 2 | 5/7 | NYSE |
| [**MSFT**](MSFT.md)<br><span class="wl-name">Microsoft</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $498.00 | D+4 | 2 | 6/7 | NASDAQ |
| [**NVDA**](NVDA.md)<br><span class="wl-name">NVIDIA</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $228.87 | D+36 만료 | 2 | 7/7 | NASDAQ |
| [**PCAR**](PCAR.md)<br><span class="wl-name">Paccar</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $113.90 |  | 3 | 4/7 | NASDAQ |
| [**PLTR**](PLTR.md)<br><span class="wl-name">Palantir</span> | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(이격과대)</span> | $184.99 |  | 2 | 6/7 | NASDAQ |
| [**PM**](PM.md)<br><span class="wl-name">Philip Morris</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $190.24 | D+61 만료 | 2 | 7/7 | NYSE |
| [**PYPL**](PYPL.md)<br><span class="wl-name">PayPal</span> | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $52.89 |  | 2 | 2/7 | NASDAQ |
| [**QCOM**](QCOM.md)<br><span class="wl-name">Qualcomm</span> | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(이격과대)</span> | $198.27 |  | 2 | 6/7 | NASDAQ |
| [**RDW**](RDW.md)<br><span class="wl-name">RedWire</span> | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $11.77 |  | 1 | 6/7 | NYSE |
| [**RKLB**](RKLB.md)<br><span class="wl-name">Rocket Lab</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $71.98 |  | 4 | 4/7 | NASDAQ |
| [**SKWD**](SKWD.md)<br><span class="wl-name">Skyward Specialty Insurance</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $55.91 | D+32 만료 | 2 | 5/7 | NASDAQ |
| [**SNPS**](SNPS.md)<br><span class="wl-name">Synopsys</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $409.24 |  | 4 | 2/7 | NASDAQ |
| [**SOUN**](SOUN.md)<br><span class="wl-name">SOUN</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $6.12 |  | 4 | 0/7 | NASDAQ |
| [**SOXS**](SOXS.md)<br><span class="wl-name">SOXS 반도체 베어 3X</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $32.42 |  | 4 | 0/7 | NYSE |
| [**SOXX**](SOXX.md)<br><span class="wl-name">SOXX 반도체 ETF</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $572.78 | D+47 만료 | 2 | 7/7 | NASDAQ |
| [**SPCX**](SPCX.md)<br><span class="wl-name">SpaceX 추적 종목</span> |  |  |  |  |  | NASDAQ |
| [**XLB**](XLB.md)<br><span class="wl-name">XLB 소재 섹터 ETF</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $50.53 |  | 3 | 3/7 | NYSE |
| [**XLC**](XLC.md)<br><span class="wl-name">XLC 커뮤니케이션 섹터 ETF</span> | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $113.52 |  | 1 | 4/7 | NYSE |
| [**XLE**](XLE.md)<br><span class="wl-name">XLE 에너지 섹터 ETF</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $61.77 | D+7 만료 | 2 | 7/7 | NYSE |
| [**XLF**](XLF.md)<br><span class="wl-name">XLF 파이낸셜 섹터 ETF</span> | <span class="verdict-sort">2</span><span class="verdict verdict-nobuy">매수불가</span> <span class="verdict-reason">(기준미달)</span> | $54.79 |  | 2 | 3/7 | NYSE |
| [**XLI**](XLI.md)<br><span class="wl-name">XLI 산업재 섹터 ETF</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $170.29 |  | 3 | 3/7 | NYSE |
| [**XLK**](XLK.md)<br><span class="wl-name">XLK 테크놀로지 섹터 ETF</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $196.26 | D+7 만료 | 2 | 7/7 | NYSE |
| [**XLP**](XLP.md)<br><span class="wl-name">XLP 필수소비재 섹터 ETF</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $82.72 |  | 3 | 3/7 | NYSE |
| [**XLRE**](XLRE.md)<br><span class="wl-name">XLRE 리츠 섹터 ETF</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $42.49 |  | 3 | 3/7 | NYSE |
| [**XLU**](XLU.md)<br><span class="wl-name">XLU 유틸리티 섹터 ETF</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도후보</span> | $40.53 |  | 3 | 2/7 | NYSE |
| [**XLV**](XLV.md)<br><span class="wl-name">XLV 헬스케어 섹터 ETF</span> | <span class="verdict-sort">0</span><span class="verdict verdict-buy">매수</span> | $169.91 | D+7 만료 | 2 | 7/7 | NYSE |
| [**XLY**](XLY.md)<br><span class="wl-name">XLY 임의소비재 섹터 ETF</span> | <span class="verdict-sort">9</span><span class="verdict verdict-nobuy">매도관찰</span> | $112.33 |  | 4 | 1/7 | NYSE |
