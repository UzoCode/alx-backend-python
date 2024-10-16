import asyncio
import importlib.util
from typing import List


"""
dynamically Load the module
"""
spec = importlib.util.spec_from_file_location(
    "wait_random", "./0-basic_async_syntax.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

"""
`wait_random` is accessed from the dynamical module
"""
wait_random = module.wait_random

"""
This module Defines the async routine wait_n
creating asyncio list
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that create a list of asyncio tasks
    stores result in delayed list when task ends

    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
