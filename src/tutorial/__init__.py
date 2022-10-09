__all__ = ["__version__", "Runner", "Tutorial"]

from typing import Union

try:
    from importlib.metadata import (
        PackageNotFoundError,
        version,
    )


except ModuleNotFoundError:

    from importlib_metadata import (  # type: ignore
        PackageNotFoundError,
        version,
    )


from .tutorial_runner import (
    Runner,
    Tutorial,
)

__version__: Union[str, None]

try:
    __version__ = version("example-project")
except PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"
except NameError:
    # importlib import failed
    __version__ = None
