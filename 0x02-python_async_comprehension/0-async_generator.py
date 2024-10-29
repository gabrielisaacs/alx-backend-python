#!/usr/bin/env python3
"""
An asynchronous coroutine called async_generator that takes
no arguments and yield a random number between 0 and 10
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    The coroutine loops 10 times, each time asynchronously
    wait 1 sec, then yield a random float between 0 and 10
    args:
        no aguements
    yields:
        a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
