#!/usr/bin/env python3
""" tsk 1 advanced """
from typing import Sequence, Optional, Any

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
