from functools import reduce
from typing import List, Tuple


def subset(array: List[int], num: int) -> List[Tuple[int]]:
    result = []

    def find(arr, num, path=()):
        if not arr:
            return
        if arr[0] == num:
            result.append(path + (arr[0],))
        else:
            find(arr[1:], num - arr[0], path + (arr[0],))
            find(arr[1:], num, path)
    find(array, num)
    return result


def product(xs: List[int]) -> int:
    return reduce(lambda acc, n: acc * n, xs)


def package(arr: List[str], size: int) -> int:
    nums = list(map(int, arr))
    n = sum(map(int, nums)) // size
    sorted_all = sorted(subset(nums, n), key=len)
    l = len(sorted_all[0])
    return min(map(product, filter(lambda x: len(x) == l, sorted_all)))
