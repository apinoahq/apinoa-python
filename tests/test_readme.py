"""Every `client.<platform>.<operation>(...)` call in README.md names a real method and real parameters,
so the examples cannot drift from the SDK."""

import ast
import inspect
import pathlib
import re

from apinoa import Apinoa

README = (pathlib.Path(__file__).parent.parent / "README.md").read_text()


def calls():
    for block in re.findall(r"```python\n(.*?)```", README, re.S):
        for node in ast.walk(ast.parse(block)):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Attribute):
                owner = node.func.value
                if isinstance(owner.value, ast.Name) and owner.value.id == "client":
                    yield owner.attr, node.func.attr, [k.arg for k in node.keywords if k.arg]


def test_readme_calls_exist() -> None:
    client = Apinoa(api_key="k")
    found = list(calls())
    assert len(found) >= 8
    for group, method, kwargs in found:
        fn = getattr(getattr(client, group), method)
        params = inspect.signature(fn).parameters
        for k in kwargs:
            assert k in params, f"client.{group}.{method}() has no parameter {k!r}"
