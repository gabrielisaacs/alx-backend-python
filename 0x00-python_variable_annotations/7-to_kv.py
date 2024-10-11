#!/usr/bin/env python3
"""
type-annotated function which takes a string and an int or float
and returns a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a int or float, returns a tuple.
    The tuple contains the string and the square of the number as a float.
    """
    return (k, float(v ** 2))
