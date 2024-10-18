#!/usr/bin/env python3
"""Executes multiple coroutines at same time wtoith async"""

import asyncio
from typing import Callable, Coroutine, List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Creates many coroutines defined by <max_delay>

    Parameters:
      n(int): number of times to call wait_random
      max_delay(int): delay value passed to wait_random

    Returns:
      list of all return values of <max_delay> sorted in ascending
      order without using sort
    """
    return [
        await task for task in asyncio.as_completed(
            [task_wait_random(max_delay) for _ in range(n)]
        )
    ]