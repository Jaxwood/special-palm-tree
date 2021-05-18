from typing import List
import re
from functools import reduce


class Reindeer:
    def __init__(self, name: str, amount: int, seconds: int, rest: int) -> None:
        self.name = name
        self.amount = amount
        self.seconds = seconds
        self.rest = rest
        self.distance = 0
        self.until = self.seconds

    def __repr__(self) -> str:
        return f'{self.name}, {self.amount}, {self.seconds}, {self.rest}'

    def tick(self, second: int) -> None:
        if second <= self.until:
            self.distance += self.amount
        elif second == self.until + self.rest:
            self.until += self.seconds + self.rest
        else:
            return None

    def total(self) -> int:
        return self.distance


def parse(raw: List[str]) -> List[Reindeer]:
    regex = re.compile(
        '(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    result: List[Reindeer] = []
    for r in raw:
        [(name, amount, second, rest)] = regex.findall(r)
        result.append(Reindeer(name, int(amount), int(second), int(rest)))
    return result


def travel(raw: List[str], seconds: int) -> int:
    reindeers = parse(raw)
    for i in range(1, seconds + 1):
        for r in reindeers:
            r.tick(i)
    return reduce(lambda acc, r: max(acc, r.total()), reindeers, 0)
