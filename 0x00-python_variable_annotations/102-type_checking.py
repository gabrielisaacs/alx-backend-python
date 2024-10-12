#!/usr/bin/env python3
"""
Using mypy to validate the piece of code
and applying the necessary changes.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into an array by repeating each element of
    the input tuple 'lst' a number of times specified
    by 'factor'. Returns a list of integers.

    Args:
        lst (Tuple[int, ...]): A tuple containing integers to zoom into.
        factor (int, optional): The number of times to repeat
        each element. Defaults to 2.

    Returns:
        List[int]: A list of integers with each element
        of the input tuple repeated.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
