#!/usr/bin/env python3
""" tsk 7"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return the sum of a list of floats"""
    return (k, float(v**2))
