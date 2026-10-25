"""Published aggregates persist through regeneration and remain clearly historical."""
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from sitegen import research_update, strategy_comparison


def test_public_table_matches_frozen_results_and_contains_all_experiments():
    data = json.loads(research_update.DATA.read_text(encoding='utf-8'))
    md = '\n'.join(research_update.lines())
    assert len(data['groups']) == 9
    for group in data['groups']:
        assert group['title'] in md
        for row in group['rows']:
            assert f"{row['total_return']:+.2%}" in md
            assert f"{row['mdd']:.2%}" in md
    assert md.count('data-testid="research-update"') == 1
    assert '0/20개' in md and '1.78%p' in md
    assert '독립된 시장 표본이나 미래 승률이 아닙니다' in md
    assert '보호 구간은 미사용' in md
    for line in md.splitlines():
        if line.lstrip().startswith('|'):
            assert line.count('|') <= 4


def test_generated_page_keeps_public_research_without_private_inputs(monkeypatch, tmp_path):
    monkeypatch.setattr(strategy_comparison.cfg, 'STRATEGY_COMPARISON_JSON', tmp_path / 'absent.json')
    assert research_update.START in '\n'.join(strategy_comparison.lines())


def test_public_payload_has_aggregate_allowlist_only():
    data = json.loads(research_update.DATA.read_text(encoding='utf-8'))
    assert set(data) == {'as_of', 'published_on', 'start', 'end', 'seed_cash', 'seeds',
                         'benchmark', 'groups', 'attribution', 'entry_wins'}
    for group in data['groups']:
        assert set(group) == {'id', 'title', 'trial', 'source_sha256', 'rows'}
        for row in group['rows']:
            assert set(row) == {'id', 'total_return', 'mdd', 'minimum', 'maximum'}
    assert set(data['attribution']) == {'components', 'source_sha256'}
    assert set(data['attribution']['components']) == {'cash', 'selection', 'timing', 'costs'}


def test_renderer_uses_supplied_values_not_hardcoded_returns(monkeypatch, tmp_path):
    data = json.loads(research_update.DATA.read_text(encoding='utf-8'))
    row = next(r for r in data['groups'][8]['rows'] if r['id'] == 'E50')
    row['total_return'], row['mdd'] = 0.1234, -0.2345
    path = tmp_path / 'aggregate.json'
    path.write_text(json.dumps(data), encoding='utf-8')
    monkeypatch.setattr(research_update, 'DATA', path)
    md = '\n'.join(research_update.lines())
    assert '| 200일 배분·50일 진입 | +12.34% | -23.45% |' in md
