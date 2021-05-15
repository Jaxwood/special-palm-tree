from typing import List


def parse(s: str) -> List[int]:
    return sorted(map(int, s.split('x')))


def wrapping_paper(strs: List[str]) -> int:
    """find the amount of wrapping paper"""
    sum = 0
    for s in strs:
        [l, w, h] = parse(s)
        sum += 2*l*w + 2*w*h + 2*h*l + l*w
    return sum


def calculate_bowtie(strs: List[str]) -> int:
    """find the amount of bowtie"""
    sum = 0
    for s in strs:
        [l, w, h] = parse(s)
        sum += l*w*h+l+l+w+w
    return sum
