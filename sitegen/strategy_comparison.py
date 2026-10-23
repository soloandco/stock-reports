"""같은 계좌 조건의 연구 비교. 계산은 core, 사이트는 저장 결과만 읽는다."""
import json

from sitegen import config as cfg
from sitegen import regime_switch

LABEL = {'base': '스윙', 'rsi': 'RSI', 'book': '단타', 'pistol': '권총 1시간', 'sue': 'SUE 상위'}
GATE = {'all': '전체', 'up': '상승 진입', 'down': '하락 진입'}


def lines():
    if not cfg.STRATEGY_COMPARISON_JSON.exists():
        return ['## 시장 상황별 계좌 비교', '', '공통 조건 비교 결과를 아직 생성하지 않았습니다.', '']
    data = json.loads(cfg.STRATEGY_COMPARISON_JSON.read_text(encoding='utf-8'))
    out = ['## 시장 상황별 계좌 비교', '',
           '**비용 차감 후 전체 계좌 수익률** 순서입니다. 과거 비교이며 최적 전략의 검증 결과는 아닙니다.', '',
           f"기간 {data['start']}~{data['end']} · 공통 {len(data['universe'])}종목 · 초기자금 ${data['seed_cash']:,.0f}", '',
           '나스닥 종합지수의 전일 종가가 SMA200 위면 상승, 이하면 하락으로 분류합니다. '
           '국면은 새 진입만 제어하고 보유분은 기존 규칙으로 청산합니다.', '',
           f"상승 {data['regime_days']['up']}일 · 하락 {data['regime_days']['down']}일 · 미상 {data['regime_days']['unknown']}일", '',
           f"두 주기의 시작 전 준비 봉·종료 가격이 부족한 {len(data['coverage_excluded'])}종목은 모든 방식에서 제외했습니다.", '',
           f"재무 캐시 또는 시작 전 SUE 계산 이력이 부족한 {len(data['fundamentals_excluded'])}종목도 모든 방식에서 제외했습니다.", '',
           '**공통 자금 배분: 한 번 매수할 때 초기자금의 10%를 비용 포함 예산으로 예약합니다.**', '',
           '쉬는 기간의 현금까지 포함한 같은 기간 수익률입니다. 상승·하락 진입 수익률을 합치면 안 됩니다.', '',
           '| 방식·진입 조건 | 순수익률 | 최대낙폭 |', '|---|---:|---:|']
    for cell in data['cells']:
        out.append(f"| {LABEL[cell['strategy']]} · {GATE[cell['gate']]} | **{cell['total_return']:+.2%}** | {cell['mdd']:.2%} |")
    out += [f"| SPY 보유 | {data['benchmark']['total_return']:+.2%} | {data['benchmark']['mdd']:.2%} |",
            '| 현금 유지 | 0.00% | 0.00% |', '',
            '**공통 조건:** 수수료·슬리피지 각각 편도 0.05%, 정수 주식, 차입 없음. '
            '종목 합산 초기자금 20%, 최대 10포지션, 방식별 하루 예약 5건입니다.', '',
            '이 표에는 손절 위험 1%·총 위험 6% 한도를 적용하지 않습니다. SUE도 같은 매수 예산을 받습니다. '
            '기존 위험 기준은 아래 별도 표에서 확인합니다.', '',
            'SPY는 같은 자금·기간·비용의 완전 투자 비교대상으로, 종목당 20% 제한을 적용하지 않습니다. '
            '세금·환율·별도 배당 현금흐름·현금 이자는 미반영입니다.', '',
            f"동시 신호 우선순위 {data['seeds']}개 시드의 중앙값입니다. 아래 범위는 통계적 신뢰구간이 아닙니다.", '',
            '| 방식·조건 | 수익률 최소~최대 | CAGR 중앙값 |', '|---|---:|---:|']
    for c in data['cells']:
        out.append(f"| {LABEL[c['strategy']]} · {GATE[c['gate']]} | {c['return_min']:+.2%}~{c['return_max']:+.2%} | {c['cagr']:+.2%} |")
    out += ['', '### 같은 날짜의 계좌 경로', '',
            '각 항목을 펼치면 시드 0 계좌의 일별 순자산을 봅니다. 표의 중앙값 수익률과 다른 실행입니다.', '']
    for c in data['cells']:
        values = c['curve']['equity']
        spy = data['benchmark']['equity']
        low, high = min(*values, *spy, data['seed_cash']), max(*values, *spy, data['seed_cash'])
        def points(seq):
            return ' '.join(f'{10 + i / max(len(seq)-1,1)*340:.1f},{150-(v-low)/max(high-low,1)*130:.1f}' for i,v in enumerate(seq))
        name = f"{LABEL[c['strategy']]} · {GATE[c['gate']]}"
        stats = c['runs'][0]
        con = stats['regime_contribution']
        out += [f'<details><summary>{name} · 시드 0 {stats["total_return"]:+.2%}</summary>',
                f'<svg viewBox="0 0 360 170" role="img" aria-label="{name} 순자산, 파랑 전략 회색 SPY" style="width:100%;max-width:420px">'
                f'<polyline points="{points(spy)}" fill="none" stroke="#999" stroke-width="2"/>'
                f'<polyline points="{points(values)}" fill="none" stroke="#2979cc" stroke-width="2"/></svg>',
                f'<p>파랑: 전략 · 회색: SPY<br>세로 범위 ${low:,.0f}~${high:,.0f}<br>{data["start"]}~{data["end"]}</p>',
                f'<p>진입 {stats["taken"]}건 · 체결 제외 {stats["skipped"]}건<br>최저 현금 ${stats["min_cash"]:,.2f}</p>',
                f'<p>초기자금 대비 일별 손익 기여<br>상승 {con["up"]:+.2%} · 하락 {con["down"]:+.2%} · 미상 {con["unknown"]:+.2%}</p>',
                '</details>', '']
    out += ['### 기존 손절 위험 기준 비교', '',
            '초기자금 기준 거래 위험 1%·총 위험 6%를 적용한 별도 결과입니다. 위 공통 자금 순위와 섞지 않습니다.', '',
            '손절선이 없는 SUE는 이 표에서 제외합니다. 임의 손절선을 추가하지 않았습니다.', '',
            '| 방식·진입 조건 | 순수익률 | 최대낙폭 |', '|---|---:|---:|']
    for c in data['risk_cells']:
        out.append(f"| {LABEL[c['strategy']]} · {GATE[c['gate']]} | {c['total_return']:+.2%} | {c['mdd']:.2%} |")
    out += ['', '**권총 체결:** 신호 마감 후 다음 시간봉 시가 매수. 선 이탈 확인 후 다음 봉 시가 청산입니다.', '',
            '**SUE 체결:** 공시 당시 알려진 재무로 계산합니다. 다음 거래일 종가 진입, 63거래일 보유하며 손절 주문은 없습니다.', '',
            '같은 매수 예산을 비교한 결과이며, 같은 손실 위험을 뜻하지 않습니다.', '',
            '단타·권총 보유분은 체결에 사용한 시간봉 가격으로 평가합니다. '
            '조정주가 기준 정수 수량이므로 당시 실제 주문 수량과는 다를 수 있습니다.', '',
            '**포함 범위:** 스윙·RSI·단타·권총 1시간·SUE의 교정 경로입니다. '
            '15/30분봉은 같은 기간 자료가 없어 제외했습니다. 실전 알림 대상과는 다릅니다.', '',
            '**해석 한계:** 이미 탐색한 과거 구간입니다. 현재 캐시 모집단의 잔여 생존편향과 '
            '체결 가정을 포함합니다. 다음 하락장 홀드아웃과 실제 계좌 성과를 대신하지 않습니다.', '',
            '이 비교로 운영 알림이나 신규 진입 차단 규칙을 자동 변경하지 않습니다.', '']
    return regime_switch.lines(data, cfg.STRATEGY_COMPARISON_JSON, LABEL) + out
