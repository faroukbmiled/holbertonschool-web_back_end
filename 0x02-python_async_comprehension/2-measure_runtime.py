#!/usr/bin/env python3
""" async """
import asyncio
import time
from typing import Tuple
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> Tuple[float, float]:
    """ async """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time
