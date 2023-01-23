#!/usr/bin/env python3
""" tsk 9"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return the sum of a list of floats"""
    return [(i, len(i)) for i in lst]
