import os
import functools
import logging
from typing import Optional

import pytest

log = logging.getLogger(__name__)


def iter_args_kwargs(args, kwargs):
    yield from args
    yield from kwargs.values()


CHECK_API_VERSION = os.getenv("CHECK_API_VERSION")


def api_version_check(min_version: Optional[int] = None, max_version: Optional[int] = None):
    def check(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log.info(args)
            log.info(kwargs)
            if CHECK_API_VERSION == "NOT_CHECKING_FOR_SUPPLY_SERVER":
                return func(*args, **kwargs)
            for value in iter_args_kwargs(args, kwargs):
                if hasattr(value, "api_ver"):
                    if min_version is not None and max_version is not None:
                        if value.api_ver < min_version or value.api_ver > max_version:
                            pytest.skip(
                                f"API required MIN version: {min_version}, "
                                f"API required MAX version: {max_version}"
                                f"current version: {value.api_ver}",
                            )
                    elif min_version is not None and max_version is None:
                        if value.api_ver < min_version:
                            pytest.skip(
                                f"API required MIN version: {min_version}, " f"current version: {value.api_ver}",
                            )
                    elif max_version and min_version is None:
                        if max_version < value.api_ver:
                            pytest.skip(
                                f"API required MAX version: {max_version}, " f"current version: {value.api_ver}",
                            )
                    else:
                        pass
                    return func(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return check
