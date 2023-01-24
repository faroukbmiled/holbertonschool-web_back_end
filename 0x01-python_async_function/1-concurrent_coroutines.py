#!/usr/bin/env python3
"""async"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """ async wait_n """
    list = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        list.append(delay)
        sort = sorted(list)
    return sort
