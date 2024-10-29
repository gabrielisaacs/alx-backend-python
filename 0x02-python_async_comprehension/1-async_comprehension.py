#!/usr/bin/env python3
"""
A coroutine that takes no arguments and collects 10
random numbers over async_generator and return them
"""

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random numbers using async
    comprehension over async_generator
    args:
        no aguements
    returns:
        10 random floats
    """
    return [n async for n in async_generator()]
