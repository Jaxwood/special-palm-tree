from collections import deque
from copy import deepcopy
from typing import Dict, List, Tuple

Player = Dict[str, int]


def create(hp: int, mana: int, dmg: int, armor: int, effects: Dict[str, int]) -> Player:
    return {
        'hp': hp,
        'mana': mana,
        'dmg': dmg,
        'armor': armor,
        'effects': effects,
    }


def magic_missile(caster: Player, target: Player) -> None:
    caster['mana'] -= cost['magic missile']
    target['hp'] -= 4


def drain(caster: Player, target: Player) -> None:
    caster['mana'] -= cost['drain']
    caster['hp'] += 2
    target['hp'] -= 2


def shield(caster: Player, target: Player) -> None:
    if 'shield' in caster['effects']:
        turn(caster, 'shield')
        caster['armor'] = 7 if caster['effects']['shield'] > 0 else 0
    else:
        caster['mana'] -= cost['shield']
        caster['effects']['shield'] = 6


def poison(caster: Player, target: Player) -> None:
    if 'poison' in caster['effects']:
        target['hp'] -= 3
        turn(caster, 'poison')
    else:
        caster['mana'] -= cost['poison']
        caster['effects']['poison'] = 6


def recharge(caster: Player, target: Player) -> None:
    if 'recharge' in caster['effects']:
        caster['mana'] += 101
        turn(caster, 'recharge')
    else:
        caster['mana'] -= cost['recharge']
        caster['effects']['recharge'] = 5


def turn(player: Player, spell: str) -> None:
    player['effects'][spell] -= 1


def can_cast(player: Player, spell: str) -> bool:
    return spell not in player['effects'] and player['mana'] > cost[spell]


cost = {
    'magic missile': 53,
    'drain': 73,
    'shield': 113,
    'poison': 173,
    'recharge': 229,
}

spells = {
    'magic missile': magic_missile,
    'drain': drain,
    'shield': shield,
    'poison': poison,
    'recharge': recharge,
}


def attack(player: Player, boss: Player) -> None:
    total = boss['dmg'] - player['armor']
    player['hp'] -= total if total > 0 else 1


def tick(player: Player, boss: Player) -> None:
    cleanup = []
    for effect in player['effects']:
        spells[effect](player, boss)
        # track empty entries
        if player['effects'][effect] == 0:
            cleanup.append(effect)
    # remove empty entries
    for clean in cleanup:
        player['effects'].pop(clean, None)


def dead(player: Player) -> bool:
    return player['hp'] <= 0


def better(spend: int, best: int) -> bool:
    return spend <= best


def part1() -> int:
    best = 0
    player = create(50, 500, 0, 0, {})
    boss = create(71, 0, 10, 0, {})
    queue = deque()
    queue.append((player, boss, 0))
    while len(queue) > 0:
        next = queue.popleft()
        for spell in spells:
            (p, b, spend) = deepcopy(next)
            # player turn
            tick(p, b)
            if can_cast(p, spell):
                spells[spell](p, b)
                spend += cost[spell]
                tick(p, b)
                if dead(b):
                    best = min(best, spend) if best != 0 else spend
                else:
                    # boss turn
                    attack(p, b)
                if not dead(p) and not dead(b) and better(spend, best if best != 0 else spend):
                    queue.append((p, b, spend))
    return best
