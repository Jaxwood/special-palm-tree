from typing import List, Tuple
from itertools import permutations
import re


class Recipe:
    def __init__(self, name: str, capacity: int, durability: int, flavor: int, texture: int, calories: int) -> None:
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def __repr__(self) -> str:
        return f'{self.name}: {self.capacity} {self.durability} {self.flavor} {self.texture} {self.calories}'


def parse(raw: List[str]) -> List[Recipe]:
    result = []
    regex = re.compile(
        '(\w+): capacity (-?\w+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')
    for r in raw:
        [(name, capacity, durability, flavor, texture, calories)] = regex.findall(r)
        result.append(Recipe(name, int(capacity), int(durability),
                             int(flavor), int(texture), int(calories)))
    return result


def mix2(raw: List[str], calories: int, limit: bool = False) -> int:
    recipes = parse(raw)
    # generate combinations of teaspoons
    teaspoons: List[int] = []
    for i in range(1, calories-len(recipes)+1):
        for j in range(1, calories-i+1):
            if sum([i, j]) == calories:
                perm = permutations([i, j])
                for p in perm:
                    teaspoons.append(p)
    return score(recipes, teaspoons, limit)


def mix4(raw: List[str], calories: int, limit: bool = False) -> int:
    recipes = parse(raw)
    # generate combinations of teaspoons
    teaspoons: List[int] = []
    for i in range(1, calories-len(recipes)+1):
        for j in range(1, calories-i+1):
            if sum([i, j]) > calories:
                continue
            for k in range(1, calories-j+1):
                if sum([i, j, k]) > calories:
                    continue
                for l in range(1, calories-k+1):
                    if sum([i, j, k, l]) == calories:
                        perm = permutations([i, j, k, l])
                        for p in perm:
                            teaspoons.append(p)
    return score(recipes, teaspoons, limit)


def score(recipes: List[Recipe], teaspoons: List[int], limit: bool) -> int:
    best = 0
    # mix and find the best one
    for xs in teaspoons:
        cap = 0
        dur = 0
        fla = 0
        tex = 0
        cal = 0
        for i, x in enumerate(xs):
            cap = cap + recipes[i].capacity*x
            dur = dur + recipes[i].durability*x
            fla = fla + recipes[i].flavor*x
            tex = tex + recipes[i].texture*x
            cal = cal + recipes[i].calories*x
        cap = cap if cap > 0 else 0
        dur = dur if dur > 0 else 0
        fla = fla if fla > 0 else 0
        tex = tex if tex > 0 else 0
        cal = cal if cal > 0 else 0
        if limit:
            if cal == 500:
                best = max(best, cap*dur*fla*tex)
        else:
            best = max(best, cap*dur*fla*tex)
    return best
