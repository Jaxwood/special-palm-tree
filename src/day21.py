from typing import List, Tuple
import uuid

Equipment = Tuple[str, int, int, int]

# Weapon Cost  Damage  Armor
weapons = [
    ('Dagger',        8,     4,       0),
    ('Shortsword',   10,     5,       0),
    ('Warhammer',    25,     6,       0),
    ('Longsword',    40,     7,       0),
    ('Greataxe',     74,     8,       0),
]

# Armor Cost  Damage  Armor
armor = [
    ('Cloth',        0,      0,       0),
    ('Leather',      13,     0,       1),
    ('Chainmail',    31,     0,       2),
    ('Splintmail',   53,     0,       3),
    ('Bandedmail',   75,     0,       4),
    ('Platemail',   102,     0,       5),
]

# Rings Cost  Damage  Armor
rings = [
    ('left',           0,     0,       0),
    ('right',          0,     0,       0),
    ('Damage + 1',    25,     1,       0),
    ('Damage + 2',    50,     2,       0),
    ('Damage + 3',   100,     3,       0),
    ('Defense + 1',   20,     0,       1),
    ('Defense + 2',   40,     0,       2),
    ('Defense + 3',   80,     0,       3),
]


class Player:
    def __init__(self, name: str, hit: int, dmg: int = 0, armor: int = 0) -> None:
        self.name = name
        self.hit = hit
        self.dmg = dmg
        self.armor = armor
        self.cost = 0

    def defend(self, dmg: int) -> None:
        self.hit = self.hit - \
            (dmg - self.armor if dmg - self.armor >= 0 else 1)

    def equip(self, dmg: Equipment, armor: Equipment, left: Equipment, right: Equipment) -> None:
        self.dmg = dmg[2] + left[2] + right[2]
        self.armor = armor[3] + left[3] + right[3]
        self.cost = dmg[1] + armor[1] + left[1] + right[1]

    def is_dead(self) -> bool:
        return self.hit <= 0

    def is_alive(self) -> bool:
        return self.hit > 0

    def total_cost(self) -> bool:
        return self.cost


def fight() -> int:
    # equip armor
    simulations: List[Player] = []
    for weapon in weapons:
        for arm in armor:
            for left in rings:
                for right in rings:
                    if left[0] != right[0]:
                        player = Player(str(uuid.uuid4()), 100)
                        player.equip(weapon, arm, left, right)
                        simulations.append(player)

    results: List[int] = []
    for player in simulations:
        boss = Player('boss', 109, 8, 2)
        while player.is_alive() and boss.is_alive():
            boss.defend(player.dmg)
            player.defend(boss.dmg)
        if boss.is_dead() and player.is_alive():
            results.append(player.total_cost())
    return min(results)
