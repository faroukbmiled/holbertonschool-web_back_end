#!/usr/bin/env python3
""" tsk 1 advanced """

from typing import Sequence, Any, Optional

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """annotationsafe_first_element"""
    if lst:
        return lst[0]
    else:
        return None

