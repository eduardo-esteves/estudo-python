from typing import Any


def is_iterable(obj: Any) -> bool:
    try:
        iter(obj)
        return True
    except TypeError:
        return False


def has_attr(obj: Any, attr: str) -> bool:
    return hasattr(obj, attr)
