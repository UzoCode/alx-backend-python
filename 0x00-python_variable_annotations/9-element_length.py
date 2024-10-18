#!/usr/bin/env python3
"""Creates a simple annotated function"""


from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> \
        List[Tuple[Sequence, int]]:
    """Both list and sequence are returned"""
    return [(i, len(i)) for i in lst]