"""저장된 국면 전환 연구 결과를 기존 방식별 기록에 표시한다."""
import hashlib
import json


def lines(baseline, source, labels):
    path = source.with_name('regime_switch_validation.json')
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding='utf-8'))
    if hashlib.sha256(source.read_bytes()).hexdigest() != data['inputs']['data/strategy_comparison.json']:
        return ['## 국면 전환 검증', '', '기준 비교가 변경되어 전환 연구를 다시 계산해야 합니다.', '']
    names = dict(labels, cash='현금')
    accounts, full = data['accounts'], data['posthoc_full']
    spy, wf = data['benchmark'], accounts['walk_forward']
    out = ['<div data-testid="regime-switch-report"></div>', '', '## 상승·하락에 따라 바꾸면 더 유리한가', '',
           '**과거 순위는 상승 진입 스윙, 하락 진입 SUE입니다. SPY보다 지속적으로 유리하다는 근거는 아직 부족합니다.**', '',
           f"계산 기준 {data['as_of']} · 기존 비교와 같은 536종목·초기 $10,000·건당 비용 포함 10% · 20개 주문 우선순위", '',
           '### 국면별 과거 순위', '',
           f"{baseline['start']}~{baseline['end']} 전체 계좌 수익률 중앙값입니다. 해당 국면에만 새로 진입하고, 그 밖의 기간에도 보유분은 원래 규칙대로 청산합니다.", '',
           '| 방식 | 상승 시 진입 | 하락 시 진입 |', '|---|---:|---:|']
    for key in ('base', 'rsi', 'sue', 'pistol', 'book'):
        cells = {c['gate']: c for c in baseline['cells'] if c['strategy'] == key}
        out.append(f"| {names[key]} | {cells['up']['total_return']:+.2%} | {cells['down']['total_return']:+.2%} |")
    down = next(c for c in baseline['cells'] if c['strategy'] == 'sue' and c['gate'] == 'down')
    con = down['runs'][0]['regime_contribution']
    out += ['', '**하락장 안에서만 얻은 수익률이 아닙니다.** SUE 하락 진입 계좌의 시드 0은 실제 진입 10건이며, '
            f"초기자금 대비 손익 기여는 하락일 {con['down']:+.2%}, 상승일 {con['up']:+.2%}입니다. 상승 전환 뒤의 회복 수익도 포함합니다.", '',
            '하락 관측은 48거래일뿐입니다. SUE를 검증된 하락장 방어 수단으로 해석하지 않습니다. 공매도·인버스 전략은 이번 후보에 없습니다.', '',
            '### 결과를 보고 고른 조합: 상승 스윙 + 하락 SUE', '',
            f"전체 기간 {baseline['start']}~{baseline['end']}: 조합 **{full['total_return']:+.2%}**, SPY **{data['benchmark_full']['total_return']:+.2%}**. "
            f"차이는 {(full['excess'] * 100):+.2f}%p입니다.", '',
            '두 수익률을 더하지 않고 한 계좌의 현금·종목 한도를 공유해 재계산했습니다. 기존 전체 성적을 보고 고른 사후 조합이므로 검증 성과로 인정하지 않습니다.', '',
            '### 과거 정보만으로 분기마다 선택한 재현', '',
            '2024년을 초기 학습으로 두고 분기 시작 전일까지의 순자산 수익률로 선택했습니다. '
            '완료 포지션 중앙값 100건 이상·그 진입일 중앙값 50일 이상·양의 수익을 모두 충족해야 합니다. 없으면 신규 진입을 쉬며, 보유분은 계속 관리합니다.', '',
            f"평가 {data['start']}~{data['end']}. 이 날짜부터 모든 계좌를 같은 현금으로 새로 시작했습니다.", '',
            '| 계좌 | 순수익 중앙값 | 최대낙폭 중앙값 |', '|---|---:|---:|']
    for key, label in [('walk_forward','분기별 과거 정보 선택'), ('posthoc','사후 조합'), ('static','2024년만으로 단일 선택')]:
        row = accounts[key]
        out.append(f"| {label} | {row['total_return']:+.2%} | {row['mdd']:.2%} |")
    out += [f"| SPY 보유 | {spy['total_return']:+.2%} | {spy['mdd']:.2%} |", '| 현금 | 0.00% | 0.00% |', '',
            f"단일 선택 대조군은 {names[data['static_choice']]}입니다. 2024년에 표본과 양의 수익 조건을 함께 충족한 매매법이 없었습니다. 따라서 단일 매매법 대비 전환 효과를 입증하는 대조군은 되지 못합니다.", '',
            '| 분기 선택일 | 상승 시 새 진입 | 하락 시 새 진입 |', '|---|---|---|']
    for row in data['schedule']:
        out.append(f"| {row['start']} | {names[row['up']]} | {names[row['down']]} |")
    out += ['', '실제로 재현된 정책은 첫 분기 현금, 이후 상승 시 스윙·하락 시 신규 진입 중지였습니다. '
            '여러 매매법 사이의 전환 효과나 하락장 SUE 효과를 확인한 결과는 아닙니다.', '',
            '**자격 기준의 한계:** SUE는 63거래일 보유·최대 10포지션이므로 마지막 학습 시점까지의 502거래일에서 완료 100건을 확보할 수 없습니다. '
            '따라서 이번 규칙 아래에서 SUE는 선택 불가능했습니다. 수익성이 나빠 탈락했다는 뜻이 아니며, 다섯 방식에 동등한 선택 기회를 준 검증도 아닙니다. '
            '결과를 본 뒤 기준을 낮추지 않고 이 한계를 공개합니다.', '',
            '마지막 선택 시점(2025-12-31까지)의 표본 진단입니다. 완료 포지션 수 / 그 진입일 수의 시드 중앙값이며, 독립 표본 수는 아닙니다.', '',
            '| 방식 | 상승 완료 / 진입일 | 하락 완료 / 진입일 |', '|---|---:|---:|']
    final_training = data['training'][data['schedule'][-1]['start']]
    for key in ('base', 'rsi', 'sue', 'pistol', 'book'):
        up, down_sample = final_training['up'][key], final_training['down'][key]
        out.append(f"| {names[key]} | {up['closed_median']:g} / {up['entry_days_median']:g} | {down_sample['closed_median']:g} / {down_sample['entry_days_median']:g} |")
    out += ['',
            f"분기별 선택 계좌의 순수익 범위는 **{wf['return_min']:+.2%}~{wf['return_max']:+.2%}**, SPY 초과는 **{wf['beat_spy']}/20개** 우선순위입니다. "
            f"중앙값 초과수익은 {wf['excess'] * 100:+.2f}%p이며, 시드 범위는 신뢰구간이 아닙니다.", '',
            '### 과최적화 점검과 판정', '',
            f"사전에 고정한 시드 0의 전체 순수익은 {wf['runs'][0]['total_return']:+.2%}입니다. "
            f"SPY 대비 누적수익 차이의 조건부 99% 구간은 **{data['paired_99_interval'][0] * 100:+.2f}~{data['paired_99_interval'][1] * 100:+.2f}%p**로 0을 포함합니다.", '',
            '20거래일 원형 블록을 5,000회 재표집했습니다. 두 계좌의 같은 날 수익을 함께 뽑았으며, 정책을 다시 학습하지 않은 실현 경로 진단입니다. 연구자 선택 편향 전체를 보정한 구간은 아닙니다.', '',
            '| 시드 0 구간 | 분기별 선택 | SPY |', '|---|---:|---:|']
    for year, value in data['yearly_seed0']['walk_forward'].items():
        label = '2026년 1~2월' if year == '2026' else year + '년'
        out.append(f"| {label} | {value:+.2%} | {data['yearly_seed0']['spy'][year]:+.2%} |")
    out += ['', '**판정: 역사적 우월성 조건 미충족, 채택 보류.** 중앙값은 앞섰지만 99% 구간 하한이 음수이고 2025년 시드 0 성과도 SPY보다 낮습니다.', '',
            '이번에는 선택 규칙·표본 하한·국면 정의·평가 기간을 계산 전에 고정하고 결과에 맞춰 바꾸지 않았습니다. '
            '다만 전략 정의와 전체 과거 구간을 이미 여러 차례 보았으므로 시간 순서를 지킨 재현도 미관측 표본 검증은 아닙니다. 2026-03 이후 보호 구간은 평가하지 않았습니다.', '',
            '다음 판단에는 고정 규칙을 유지한 새 기간의 계좌 기록과 추가 하락 국면이 필요합니다. 하락 표본을 억지로 늘리려고 기준을 낮추거나 이번 결과로 조건을 다시 고르지 않습니다.', '',
            '[반복 탐색과 백테스트 과최적화의 근거: Bailey 외](https://escholarship.org/uc/item/4w1110bb).', '',
            '재현 파일: `research_regime_switch_validation.py` · `data/regime_switch_validation.json` · `docs/prereg-2026-10-23-regime-switch.md`.', '',
            '이후 표는 기존 전체 기간 비교이며, 위 2025년 이후 평가와 기간이 다릅니다.', '']
    return out
