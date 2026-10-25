"""Render the frozen public aggregate, without importing private analysis code."""
import json
from pathlib import Path

START = '<!-- research-update-2026-10-25:start -->'
END = '<!-- research-update-2026-10-25:end -->'
DATA = Path(__file__).resolve().parents[1] / 'docs/strategies/research-2026-10-25.json'

LABELS = {
    'BASE': '기존 스윙', 'SLOTS20': '최대 20포지션', 'EQUITY20': '20포지션·순자산 예산',
    'LIQUID10': '거래대금 우선', 'PULLBACK10': '최근 수익률 낮은 순',
    'EQUITY_LIQUID20': '순자산·거래대금 우선', 'EQUITY_PULLBACK20': '순자산·최근 수익률 순',
    'SPY70_EQUITY30': 'SPY70·스윙30 (기존 청산)',
    'S': '선정', 'E': '진입', 'X': '청산', 'SE': '선정·진입', 'SX': '선정·청산',
    'EX': '진입·청산', 'SEX': '선정·진입·청산', 'SX_SLOTS20': '선정·청산·20포지션',
    'SX_EQUITY20': '선정·청산·순자산 예산', 'FINAL': '이전 최종 결합안',
    'C': 'SPY70·스윙30', 'G': '진입 국면 제한 제거', 'T': '5ATR 청산',
    'CG': 'SPY 혼합·국면 제한 제거', 'CT': 'SPY70·스윙30·5ATR',
    'GT': '국면 제한 제거·5ATR', 'CGT': 'SPY 혼합·국면 제한 제거·5ATR',
    'FIXED': '고정 70/30', 'WEEKLY70': '주간 70/30 재배분',
    'TREND_SWING': '상승장 스윙 확대', 'TREND_CORE': '상승장 SPY 확대',
    'VOL_SWING': '저변동 상승장 스윙 확대', 'OLD': '기존 동적안',
    'DAILY_CASH': '매일 현금만 이동', 'WEEKLY_TRIM': '주간 일부 청산',
    'DAILY_TRIM': '매일 일부 청산', 'W200': '200일·주간', 'D200': '200일·일간',
    'W100': '100일·주간', 'D100': '100일·일간', 'W50': '50일·주간', 'D50': '50일·일간',
    'E200': '기존 200일 진입', 'E100': '100일 진입', 'E50': '50일 진입', 'ALL': '진입 국면 제한 없음',
}
NOTES = (
    '순자산 예산은 현재 계좌 가치의 10%입니다. 최대 보유와 매수 순서를 비교했습니다.',
    '선정: 126거래일 수익률이 SPY 초과. 청산: 3ATR 추적 손절.\n\n'
    '진입: 신호 다음 거래일 종가 확인 후, 그다음 거래일 시가에 매수합니다.',
    '선정·3ATR 청산에 20포지션·순자산 예산을 결합했습니다.',
    '이전 결합안에 SPY 혼합, 진입 국면 제한 제거, 5ATR 청산을 각각 조합했습니다.',
    'SPY와 스윙의 초기 자금만 나눕니다. 이후 재배분하지 않으며 5ATR 청산을 유지합니다.',
    '상승장 SPY 확대는 상승 90/10·하락 30/70입니다. 주간 판단 후 남은 현금만 옮깁니다.',
    '시장 판단은 주간으로 고정했습니다. 일부 청산은 현금 부족분만 보유 비례로 매도합니다.',
    '배분 판단의 이동평균·주기만 변경했습니다. 일부 청산 허용, 스윙 진입은 기존 200일 조건입니다.',
    '배분은 200일·일간으로 고정했습니다. 신호일 전 거래일의 지수와 이동평균으로 신규 진입을 제한합니다.',
)


def lines():
    if not DATA.exists():
        return []
    data = json.loads(DATA.read_text(encoding='utf-8'))
    groups = data['groups']
    def row(group, name):
        return next(r for r in groups[group]['rows'] if r['id'] == name)
    def table(rows):
        result = ['| 비교안 | 순수익률 | 최대낙폭 |', '|---|---:|---:|']
        for label, values in rows:
            result.append(f"| {label} | {values['total_return']:+.2%} | {values['mdd']:.2%} |")
        return result + ['']
    best = row(8, 'E50')
    spy = data['benchmark']
    out = [START, '<div id="research-2026-10-25" data-testid="research-update"></div>', '',
           '## 자금 배분·진입·청산 개선 비교', '',
           '**이전 방식보다 개선됐지만 SPY 초과 우위는 확인하지 못했습니다.**', '',
           f"분석 기준 {data['as_of']} · 공개 {data['published_on']}", '',
           f"기간 {data['start']}~{data['end']} · 초기 $10,000 · 공통 536종목", '',
           '아래 수치는 과거 모의 계좌 결과입니다. 실제 체결 계좌 실적이 아닙니다.', '',
           '수익률과 최대낙폭은 각각 20개 주문 우선순위의 중앙값입니다.', '',
           '편도 수수료 0.05%·슬리피지 0.05%, 정수 주식·차입 없음으로 비교했습니다.', '',
           'SPY도 같은 비용으로 첫 시가 매수·마지막 종가 청산합니다.', '',
           '조정주가 기준이며 세금·환율·별도 현금배당·현금이자는 제외합니다.', '',
           '### 주요 결과', '']
    out += table([
        ('기존 스윙', row(2, 'BASE')), ('선정·청산·배분 결합', row(2, 'SX_EQUITY20')),
        ('5ATR·고정 70/30', row(8, 'FIXED')), ('5ATR·고정 80/20', row(4, '80')),
        ('기존 동적안', row(6, 'OLD')), ('200일·일간 배분', row(8, 'E200')),
        ('200일 배분·50일 진입', best), ('SPY 보유', spy)])
    out += [f"50일 진입안은 기존 200일 진입보다 {(best['total_return']-row(8,'E200')['total_return'])*100:+.2f}%p 개선됐습니다.", '',
            f"SPY보다 {(spy['total_return']-best['total_return'])*100:.2f}%p 낮으며, SPY 초과는 {data['entry_wins']['E50']}/20개입니다.", '',
            '고정 혼합안 중 수익률 최고는 80/20입니다. 70/30 대비 개선은 0.11%p로 작습니다.', '',
            '고정 80/20과 동적 50일 진입은 서로 다른 비교군의 결과입니다.', '',
            '**운영 채택 없음.** 수익 개선 후보와 SPY 우월성 입증을 구분합니다.', '',
            '### 이전 결합안의 SPY 격차 분해', '',
            '수익률 중앙에 놓인 두 계좌의 평균 기여입니다. 인과 효과로 해석하지 않습니다.', '',
            '| 기여 항목 | SPY 대비 차이 |', '|---|---:|']
    for key, label in [('cash', '평균 현금 보유'), ('selection', '종목 선정'), ('timing', '투자·청산 시점'), ('costs', '추가 거래비용')]:
        out.append(f"| {label} | {data['attribution']['components'][key]*100:+.2f}%p |")
    out += ['', '시점·현금·비용이 손실 요인이고 종목 선정은 이를 일부 상쇄했습니다.', '',
            '현금을 없애면 같은 금액이 회복된다는 뜻은 아닙니다.', '',
            '### 실험별 전체 비교', '']
    for i, group in enumerate(groups):
        out += [f"??? info \"{group['title']} · 연구 {group['trial']}\"", '']
        content = NOTES[i].splitlines() + ['']
        rows = [(f"SPY {r['id']}%" if i == 4 else LABELS[r['id']], r) for r in group['rows']]
        content += table(rows)
        out += ['    ' + line if line else '' for line in content]
    out += ['### 해석 범위', '',
            '20개 순서는 주문 우선순위 민감도입니다. 독립된 시장 표본이나 미래 승률이 아닙니다.', '',
            '수익률과 최대낙폭 중앙값이 같은 계좌에서 나온다고 보장하지 않습니다.', '',
            '기존 후보 신호를 고정한 비교이며, 조기 청산 뒤 새 신호를 추가하지 않았습니다.', '',
            '5ATR는 확정 종가로 다음 날 손절을 올립니다. 최초 손절과 90일 만기는 유지합니다.', '',
            '일부 청산 실험에는 비중 조절 매도가 추가됩니다. 남은 주식은 기존 청산 규칙을 따릅니다.', '',
            '각 실험의 다중비교 보정 99% 구간 등 채택 기준을 모두 충족한 변경안은 없습니다.', '',
            '이미 탐색한 과거 구간이며, 현재 캐시 모집단의 잔여 생존편향도 포함합니다.', '',
            '전체 연구의 선택 편향을 제거한 독립 검증이 아닙니다. 2026-03 이후 보호 구간은 미사용입니다.', '',
            '[수치·원자료 해시 확인](research-2026-10-25.json)', '', END, '']
    return out
