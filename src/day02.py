from typing import List, Set, Dict, Tuple, Optional


def wrapping_paper(strs: List[str]) -> int:
    """find the amount of wrapping paper"""
    sum = 0
    for s in strs:
        [l, w, h] = sorted(map(int, s.split('x')))
        sum += 2*l*w + 2*w*h + 2*h*l + l*w
    return sum
