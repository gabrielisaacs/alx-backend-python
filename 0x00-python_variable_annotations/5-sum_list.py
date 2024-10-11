#!/usr/bin/env python3
"""
Type-annotated function which takes a list of floats
and returns their sum as float
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    args:
        input_list(List[float]): floats
    return:
        float: sum(input_list)
    """
    return sum(input_list)
