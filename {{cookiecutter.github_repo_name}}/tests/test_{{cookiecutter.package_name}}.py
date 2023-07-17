"""Test {{ cookiecutter.package_name }}."""


import {{ cookiecutter.package_name }}


def test_version() -> None:
    """Ensure the package has a __version__ string."""
    assert isinstance({{ cookiecutter.package_name }}.__version__, str)
