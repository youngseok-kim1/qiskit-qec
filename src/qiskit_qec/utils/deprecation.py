from __future__ import annotations
import functools
import inspect
import warnings
from collections.abc import Callable
from typing import Any, Type

def deprecate_function(
    msg: str, 
    stacklevel: int = 2,
    category: Type[Warning] = DeprecationWarning,
    *,
    since: str | None = None,
):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(msg, category=category, stacklevel=stacklevel)
            return func(*args, **kwargs)
        return wrapper
    return decorator
