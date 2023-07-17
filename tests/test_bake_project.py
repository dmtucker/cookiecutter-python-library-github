"""Test cookiecutter-python-library-github."""


import contextlib
import os
import shutil
import subprocess

import pytest


@contextlib.contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """Call cookies.bake and delete the directory it creates after."""
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        shutil.rmtree(result.project_path)


@pytest.mark.parametrize(
    "extra_context",
    [
        {},
        {"maintainer_name": "O'connor"},
    ],
)
def test_bake(cookies, extra_context):
    """Ensure the tests pass after being baked with different contexts."""
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        assert result.exception is None
        assert result.exit_code == 0
        assert result.project_path.is_dir()
        assert (
            subprocess.check_call(
                ["tox", "run"],
                cwd=result.project_path,
                env={"GITHUB_ACTIONS": "true", "PATH": os.environ["PATH"]},
            )
            == 0
        )
