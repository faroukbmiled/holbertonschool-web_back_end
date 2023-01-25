#!/usr/bin/env python3
"""async"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async_comprehension"""
    async_gen = async_generator()
    return [num async for num in async_gen if num < 10]
