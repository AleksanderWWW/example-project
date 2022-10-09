__all__ = ["__version__", "Runner", "Tutorial"]

try:
    from importlib.metadata import (
        PackageNotFoundError,
        version,
    )

    try:
        __version__ = version("example-project")
    except PackageNotFoundError:
        # package is not installed
        __version__ = None

except ModuleNotFoundError:
    __version__ = "0.0.1"

from .tutorial_runner import (
    Runner,
    Tutorial,
)
