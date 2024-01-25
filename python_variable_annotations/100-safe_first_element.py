#!/usr/bin/env python3
""" tsk 1 advanced """

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """annotatiosafe_first_elementn"""
    if lst:
        return lst[0]
    else:
        return None
