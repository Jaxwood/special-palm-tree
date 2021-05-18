from typing import Dict, List, Set, Tuple
from functools import reduce
from itertools import permutations
import re


def parse(arrangement: List[str]) -> Dict[Tuple[str, str], int]:
    regex = re.compile(
        '(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).')
    result: Dict[Tuple[str, str], int] = {}
    for a in arrangement:
        [(person, net, amount, other)] = regex.findall(a)
        result[(person, other)] = int(
            amount) if net == 'gain' else int(amount) * -1
    return result


def collect(acc: Set[str], kv: Tuple[Tuple[str, str], int]) -> Set[str]:
    for k in kv:
        acc.add(k)
    return acc


def seating(arrangement: List[str]) -> int:
    preferences = parse(arrangement)
    participants = list(permutations(
        list(reduce(collect, preferences, set()))))
    best = 0
    for suggestion in participants:
        sum = 0
        for i in range(len(suggestion)):
            sum += preferences[(suggestion[i], suggestion[i+1])] + preferences[(suggestion[i+1], suggestion[i])] if i+1 < len(
                suggestion) else preferences[(suggestion[i], suggestion[0])] + preferences[(suggestion[0], suggestion[i])]
        best = max(sum, best)
    return best
