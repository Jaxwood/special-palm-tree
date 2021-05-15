import enum
import re
from typing import List, Tuple


class Type(enum.Enum):
    Toggle = 1
    On = 2
    Off = 3


def parse(instruction: str) -> Tuple[Type, Tuple[int, int], Tuple[int, int]]:
    regex = re.compile('(\d+)')
    [x, y, z, w] = map(int, regex.findall(instruction))
    if instruction[:6] == "toggle":
        return [Type.Toggle, (x, z+1), (y, w+1)]
    if instruction[:7] == "turn on":
        return [Type.On, (x, z+1), (y, w+1)]
    if instruction[:8] == "turn off":
        return [Type.Off, (x, z+1), (y, w+1)]


def light_up(instructions: List[str]) -> int:
    """light according to the instructions"""
    state = {}
    for i in range(0, 1000):
        for j in range(0, 1000):
            state[(i, j)] = 0
    for instruction in instructions:
        [cmd, [x, y], [z, w]] = parse(instruction)
        if cmd == Type.Toggle:
            for i in range(x, y):
                for j in range(z, w):
                    state[(i, j)] = 1 if state[(i, j)] == 0 else 0
        elif cmd == Type.On:
            for i in range(x, y):
                for j in range(z, w):
                    state[(i, j)] = 1
        else:
            for i in range(x, y):
                for j in range(z, w):
                    state[(i, j)] = 0
    sum = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            sum += 1 if state[(i, j)] == 1 else 0
    return sum


def brightness(instructions: List[str]) -> int:
    """light according to the instructions"""
    state = {}
    for i in range(0, 1000):
        for j in range(0, 1000):
            state[(i, j)] = 0
    for instruction in instructions:
        [cmd, [x, y], [z, w]] = parse(instruction)
        if cmd == Type.Toggle:
            for i in range(x, y):
                for j in range(z, w):
                    state[(i, j)] += 2
        elif cmd == Type.On:
            for i in range(x, y):
                for j in range(z, w):
                    state[(i, j)] += 1
        else:
            for i in range(x, y):
                for j in range(z, w):
                    state[(i, j)] -= 1 if state[(i, j)] > 0 else 0
    sum = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            sum += state[(i, j)]
    return sum
