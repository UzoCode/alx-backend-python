#!/usr/bin/env python3
"""Creates a smple annotated function"""


from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Here sums up a list of floats"""
    return (k, v*v)