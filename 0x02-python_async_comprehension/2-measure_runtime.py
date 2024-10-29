#!/usr/bin/env python3
"""
A coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
"""

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the runtime of executing async_comprehension
    four times in parallel
    args:
        No aguements
    returns:
        a float: runtime for executing the task
    """
    start_time = time.perf_counter()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    end_time = time.perf_counter()
    return end_time - start_time
