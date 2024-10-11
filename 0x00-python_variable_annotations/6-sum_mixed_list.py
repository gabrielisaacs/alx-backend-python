#!/usr/bin/env python3
"""
type-annotated function which takes a list of
integers and floats then returns their sum as float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    args:
        mxd_lst (List[Union[int, float]]): a list of integers & floats
    returns:
        float: sum of mxd_lst
    """
    return sum(mxd_lst)
