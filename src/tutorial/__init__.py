__all__ = ["__version__", "Runner", "Tutorial"]

from importlib.metadata import (
    PackageNotFoundError,
    version,
)

from .tutorial_runner import *

try:
    __version__ = version("example-project")
except PackageNotFoundError:
    # package is not installed
    __version__ = None
