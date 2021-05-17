from typing import Callable, Dict, List, Set
import re
from itertools import permutations


def find_distance(routes: List[str], min_or_max: Callable[[int, int], int]) -> int:
    compass: Dict[(str, str), int] = {}
    result: int = 0
    regex = re.compile('(\w+) to (\w+) = (\d+)')
    cities: Set[str] = set()
    for route in routes:
        [(start, end, dist)] = regex.findall(route)
        compass[(start, end)] = int(dist)
        compass[(end, start)] = int(dist)
        cities.add(start)
        cities.add(end)
    perm = permutations(cities)
    for candidate in list(perm):
        sum = 0
        for i, c in enumerate(candidate):
            if i < len(candidate) - 1:
                sum += compass[(c, candidate[i+1])]
        result = sum if result == 0 else min_or_max(sum, result)
    return result
