#!/usr/bin/env python3
"""
function to measure execution time with integers
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for running wait_n(n, max_delay)
    and returns the average time per call
    args:
        n (int): The number of calls to wait_n
        max_delay (int): The maximum delay for each call

    returns:
        float: The average time for each call
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()

    total_time: float = end_time - start_time
    return total_time / n
