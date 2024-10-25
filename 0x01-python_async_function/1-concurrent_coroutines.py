#!/usr/bin/env python3
"""
Module for concurrent coroutines.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run `wait_random` `n` times with the specified `max_delay`
    and return the list of delays in ascending order
    args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay for wait_random
    returns:
        List[float]: List of delay times in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
