#!/usr/bin/env python3
"""
Modifying the code from wait_n into a new function task_wait_n
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run `task_wait_random` `n` times with the specified `max_delay`
    and return the list of delays in ascending order

    args:
        n (int): Number of times to call task_wait_random
        max_delay (int): Maximum delay for task_wait_random

    returns:
        List[float]: List of delay times
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return sorted(delays)
