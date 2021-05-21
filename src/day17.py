from typing import List


def combi(nums: List[int], total: int, acc: int) -> int:
    """recursively call the combi function to calculate"""
    if total < 0:
        return 0
    if total == 0:
        return 1
    if len(nums) == 0:
        return acc

    n, rest = nums[0], nums[1:]

    return combi(rest, total - n, acc) + combi(rest, total, acc)
