#!/usr/bin/env python3
"""Executes multiple coroutines at same time with async"""

from asyncio import run
from time import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measuring total execution time for
    wait_n(n, max_delay).

    Parameters:
       n(int) - number of iterations
       max_delay(int) - sleep time between each iteration

    Returns total_time / n
    """
    then: float = time()
    res: float = run(wait_n(n, max_delay))
    now: float = time()
    return (now - then)/n