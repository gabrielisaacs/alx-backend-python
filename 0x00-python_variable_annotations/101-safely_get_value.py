#!/usr/bin/env python3
"""
Augmenting the code with the correct
duck-typed annotations
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary or return the default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
