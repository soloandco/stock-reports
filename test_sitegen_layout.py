"""gen.py 분할 구조 지키기 (2026-10-02).

본체는 sitegen/ 패키지에 있고 gen.py 는 실행 입구다. 테스트가 경로를 바꿔 끼울 때 「함수를
부르는 쪽이 보는 이름」을 바꿔야 먹는다. 못 먹으면 테스트가 실제 사이트 원고(docs/)에 쓴다.
"""
import ast
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import gen  # noqa: E402
from sitegen import config as cfg  # noqa: E402

PKG = ROOT / "sitegen"


def test_siblings_are_imported_as_modules_only():
    """sitegen 모듈끼리는 `from sitegen import 모듈` 로만 가져오고 「모듈.이름」으로 부른다."""
    mods = {p.stem for p in PKG.glob("*.py")}
    bad = []
    files = sorted(PKG.glob("*.py")) + [ROOT / "gen.py"]
    assert len(files) > 6
    for f in files:
        for node in ast.walk(ast.parse(f.read_text(encoding="utf-8"))):
            if isinstance(node, ast.ImportFrom) and node.module and node.module.startswith("sitegen."):
                bad.append(f"{f.name}:{node.lineno} from {node.module} import ...")
            if isinstance(node, ast.ImportFrom) and node.module == "sitegen":
                bad += [f"{f.name}:{node.lineno} {a.name}" for a in node.names if a.name not in mods]
    assert not bad, "\n".join(bad)


def test_no_function_argument_shadows_a_module_alias():
    """함수 인자·지역 이름이 sitegen 모듈 이름과 같으면 `market.x` 같은 글이 무엇을 뜻하는지 헷갈린다."""
    aliases = {p.stem for p in PKG.glob("*.py")} | {"cfg"}
    bad = []
    for f in sorted(PKG.glob("*.py")) + [ROOT / "gen.py"]:
        for n in ast.parse(f.read_text(encoding="utf-8")).body:
            if isinstance(n, ast.FunctionDef):
                names = {a.arg for a in ast.walk(n) if isinstance(a, ast.arg)}
                names |= {x.id for x in ast.walk(n) if isinstance(x, ast.Name) and isinstance(x.ctx, ast.Store)}
                bad += [f"{f.name}:{n.name} {x}" for x in names & aliases]
    assert not bad, "\n".join(bad)


def test_patching_gen_is_refused_with_home():
    # monkeypatch 로 시험하면 정리 단계의 되돌리기도 거부당한다. 그래서 setattr 를 직접 쓴다
    with pytest.raises(AttributeError, match="sitegen.config.OUT_WL"):
        setattr(gen, "OUT_WL", Path("x"))
    with pytest.raises(AttributeError):
        setattr(gen, "OUT_WLL", Path("x"))      # 오타 난 새 이름도 막는다
    gen.main = gen.main                          # gen 이 직접 정의한 이름은 바꿀 수 있다


def test_reading_gen_sees_current_value(monkeypatch, tmp_path):
    monkeypatch.setattr(cfg, "OUT_WL", tmp_path)
    assert gen.OUT_WL == tmp_path


def test_every_old_name_still_resolves():
    for name in gen._HOMES:
        getattr(gen, name)


def test_patch_targets_exist_in_source():
    """테스트가 바꿔 끼우는 "sitegen.모듈.이름" 이 그 모듈에 실제로 정의돼 있는가."""
    defined = {}
    for f in PKG.glob("*.py"):
        names = set()
        for n in ast.parse(f.read_text(encoding="utf-8")).body:
            if isinstance(n, ast.FunctionDef):
                names.add(n.name)
            elif isinstance(n, ast.Assign):
                names |= {x.id for t in n.targets for x in ast.walk(t) if isinstance(x, ast.Name)}
        defined[f.stem] = names
    pat = re.compile(r"""setattr\(\s*["']sitegen\.(\w+)\.(\w+)["']""")
    files = sorted(ROOT.glob("test_*.py")) + sorted((ROOT.parent / "tests").glob("test_*.py"))
    bad, seen = [], 0
    for f in files:
        for mod, name in pat.findall(f.read_text(encoding="utf-8")):
            seen += 1
            if name not in defined.get(mod, ()):
                bad.append(f"{f.name}: sitegen.{mod}.{name}")
    assert seen >= 20
    assert not bad, "없는 이름을 바꿔 끼운다:\n" + "\n".join(bad)
