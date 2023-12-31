import sys
from .authToken import Token
from .user import User
from .island import Island
from .Exceptions import *

__all__ = (
    "Token",
    "User",
    "UserNotFound",
    "InvalidPassword",
    "InvalidUsername",
    "InvalidEmail",
    "ExistingUser",
    "Island",
)

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "mg_model"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
