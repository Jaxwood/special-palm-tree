from math import ceil, sqrt
from functools import reduce
from typing import Set


def factors(num: int) -> Set[int]:
    result = set()
    for i in range(1, ceil(num / 2)):
        if num % i == 0:
            if i in result or (num / i) in result:
                return result
            result.add(i)
            result.add(int(num / i))
    return result


def deliverable(until: int) -> int:
    house = 750000
    while True:
        facts = factors(house)
        sum = reduce(lambda acc, n: acc + n * 10, facts, 0)
        if sum >= until:
            return house
        house = house + 1


def limited_deliverable(until: int) -> int:
    house = 750000
    while True:
        facts = filter(lambda x: x * 50 >= house, factors(house))
        sum = reduce(lambda acc, n: acc + n * 11, facts, 0)
        if sum >= until:
            return house
        house = house + 1
