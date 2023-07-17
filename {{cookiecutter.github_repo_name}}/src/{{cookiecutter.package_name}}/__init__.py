"""Define the top-level API for {{ cookiecutter.project_name }}."""


import importlib.metadata


__all__ = [
    "__version__",
]
__version__ = importlib.metadata.version("{{ cookiecutter.distribution_name }}")
