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

| 종목 | 판정 | 진입일 | 진입가 | 현재가 | 수익률 | R | 손절까지 | 타겟까지 | 보유 |
|------|------|--------|--------|--------|--------|---|---------|---------|------|
| [**MS**](../snapshots/MS-2026-07-07.md) Morgan Stanley | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-30 | $211.72 | $220.71 | 🟢 +4.2% | +0.8R | -9.4% | +11.8% | 7일 |
| [**GEV**](../snapshots/GEV-2026-07-07.md) GE Vernova | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $1,102.51 | $1,147.62 | 🟢 +4.1% | +0.5R | -12.6% | +22.1% | 7일 |
| [**BA**](../snapshots/BA-2026-07-07.md) Boeing | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-03 | $226.49 | $232.65 | 🟢 +2.7% | +0.5R | -8.5% | +14.9% | 4일 |
| [**BE**](../snapshots/BE-2026-07-07.md) Bloom Energy | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $275.01 | $292.51 | 🟢 +6.4% | +0.3R | -25.8% | +53.5% | 7일 |
| [**KO**](../snapshots/KO-2026-07-07.md) Coca-Cola | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $82.65 | $82.87 | 🟢 +0.3% | +0.1R | -4.0% | +10.8% | 7일 |
| [**PM**](../snapshots/PM-2026-07-07.md) Philip Morris | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 06-30 | $182.87 | $183.12 | 🟢 +0.1% | +0.0R | -5.4% | +15.6% | 7일 |
| [**KMI**](../snapshots/KMI-2026-07-07.md) Kinder Morgan | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $31.72 | $31.75 | 🟢 +0.1% | +0.0R | -4.6% | +13.3% | 5일 |
| [**LLY**](../snapshots/LLY-2026-07-09.md) Eli Lilly | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 07-09 | $1,215.83 | $1,215.83 | ⚪ +0.0% | +0.0R | -6.3% | +18.8% | 0일 |
| [**GS**](../snapshots/GS-2026-07-07.md) Goldman Sachs | <span class="verdict-sort">0</span><span class="verdict verdict-cand">매수후보</span> | 06-25 | $1,076.91 | $1,049.20 | 🔴 -2.6% | -0.4R | -3.3% | +20.4% | 12일 |
| [**CAT**](../snapshots/CAT-2026-07-09.md) Caterpillar | <span class="verdict-sort">1</span><span class="verdict verdict-watch">매수관찰</span> | 07-02 | $991.41 | $948.08 | 🔴 -4.4% | -0.5R | -3.7% | +29.5% | 7일 |

**합계** 10포지션 · 평균 +0.1R · 양의 R 7/10

!!! warning "투자 유의 / Disclaimer"
    이 사이트는 기술적 분석 프레임워크(Weinstein·Minervini·Turtle)의 **판정 결과를 기록**한 것으로,
    **투자 권유나 매매 추천이 아닙니다.** 모든 투자 책임은 투자자 본인에게 있습니다.
    수치는 분석 시점의 yfinance 데이터 기준이며 지연·오류가 있을 수 있습니다.

