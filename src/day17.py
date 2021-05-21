from typing import List, Tuple


def combi(nums: List[int], total: int, acc: List[int]) -> List[int]:
    if total < 0:
        return []
    if total == 0:
        return [acc]
    if len(nums) == 0:
        return []

    n, rest = nums[0], nums[1:]

    return combi(rest, total - n, acc+1) + combi(rest, total, acc)


def combi_min_length(nums: List[int], total: int, acc: int) -> int:
    result = combi(nums, total, acc)
    lowest = min(result)
    return len(list(filter(lambda x: x == lowest, result)))
