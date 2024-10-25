#!/usr/bin/env python3
"""
asynchronous coroutine that waits for a random delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds.
    args:
        max_delay (Union[int, float]): The maximum delay
        in seconds.
    returns:
        float: The random delay time.
    """
    rand_num = random.uniform(0, max_delay)
    await asyncio.sleep(rand_num)
    return rand_num
