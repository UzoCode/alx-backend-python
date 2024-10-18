#!/usr/bin/env python3
"""Creates simple annotated function"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Here is Sum of a list of floats"""
    total: float = 0
    for num in input_list:
        total += num
    return total
