from typing import Dict, List, Tuple
import re


class Aunt:
    def __init__(self, num: int, chars: Dict[str, int]) -> None:
        self.num = num
        self.chars = chars

    def matches(self, traits: List[str]) -> bool:
        for trait in traits:
            if self.chars.get(trait[0]) != None and self.chars.get(trait[0]) != trait[1]:
                return False
        return True

    def advanced_match(self, traits: List[str]) -> bool:
        for trait in traits:
            if self.chars.get(trait[0]) != None:
                if trait[0] == 'trees':
                    if self.chars.get(trait[0]) <= trait[1]:
                        return False
                elif trait[0] == 'cats':
                    if self.chars.get(trait[0]) <= trait[1]:
                        return False
                elif trait[0] == 'pomeranians':
                    if self.chars.get(trait[0]) >= trait[1]:
                        return False
                elif trait[0] == 'goldfish':
                    if self.chars.get(trait[0]) >= trait[1]:
                        return False
                elif self.chars.get(trait[0]) != trait[1]:
                    return False
        return True


def parse(raw: List[str]) -> List[Aunt]:
    regex = re.compile('Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')
    aunts = []
    for r in raw:
        [(num, c1, n1, c2, n2, c3, n3)] = regex.findall(r)
        aunts.append(
            Aunt(int(num), dict([
                (c1, int(n1)),
                (c2, int(n2)),
                (c3, int(n3))
            ])))

    return aunts


def find_aunt_sue(traits: List[str], raw: List[Tuple[str, int]], advanced: bool = False) -> int:
    aunts = parse(raw)
    for aunt in aunts:
        if advanced:
            if aunt.advanced_match(traits):
                return aunt.num
        else:
            if aunt.matches(traits):
                return aunt.num
    return 0
