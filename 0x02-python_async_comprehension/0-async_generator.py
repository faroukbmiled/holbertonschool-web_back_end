#!/usr/bin/env python3
""" async """
import asyncio
import random


async def async_generator():
    """async gen"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
