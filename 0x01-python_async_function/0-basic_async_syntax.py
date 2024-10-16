#!/usr/bin/env python3

import asyncio
import random

"""
This asynchronous coroutine takes interger argument of
max_delay and ten.
It waits for the random delay and return it
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    function that generates random delay between 0 and max_delay
    wait for the delay
    and return value of delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
