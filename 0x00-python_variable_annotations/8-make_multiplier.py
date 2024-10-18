#!/usr/bin/env python3
"""Creates a simple annotated function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function is returned"""
    return lambda num: multiplier * num