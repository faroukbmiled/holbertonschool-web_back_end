#!/usr/bin/env python3
""" tsk 8"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make_multiplier function"""
    def multiply_by(n: float) -> float:
        return n * multiplier
    return multiply_by
