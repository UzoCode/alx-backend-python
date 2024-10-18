#!/usr/bin/env python3
"""Creates a simple annotated function"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Here sums up a list of floats"""
    total: float = 0
    for num in mxd_lst:
        total += num
    return total
