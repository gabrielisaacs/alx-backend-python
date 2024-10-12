#!/usr/bin/env python3
"""
a type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function
that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.
    args:
        multiplier: float
    return:
        Callable: float
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies the input value by the multiplier.
        """
        return value * multiplier

    return multiplier_function
