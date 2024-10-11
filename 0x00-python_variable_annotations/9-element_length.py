#!/usr/bin/env python3

from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of sequences and returns a list of tuples containing
    each sequence and its length.
    """
    return [(i, len(i)) for i in lst]