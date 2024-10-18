#!/usr/bin/env python3
"""Execues multiple coroutines at same time worth async"""

import asyncio
from typing import Callable, Coroutine, List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Creating many coroutines defined by <max_delay>

    Parameters:
      n(int): number of times to call wait_random
      max_delay(int): delay value to pass to wait_random

    Returns:
      list of all return values of <max_delay> sorted in ascending
      order without using sort
    """
    return [
        await task for task in asyncio.as_completed(
            [wait_random(max_delay) for _ in range(n)]
        )
    ]