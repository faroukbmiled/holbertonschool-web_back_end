#!/usr/bin/env python3
""" tsk 1 advanced """
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the sum of a list of floats"""
    if lst:
        return lst[0]
    else:
        return None
