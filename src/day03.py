from typing import Tuple


def move(s: str, coord: Tuple[int, int]) -> Tuple[int, int]:
    """calculate next move"""
    x, y = coord
    if s == '>':
        x += 1
    if s == '<':
        x -= 1
    if s == '^':
        y += 1
    if s == 'v':
        y -= 1
    return (x, y)


def houses(path: str) -> int:
    """find all houses visited atleast once"""
    current = (0, 0)
    visited = {current}
    for s in path:
        current = move(s, current)
        visited.add(current)
    return len(visited)


def robot_houses(path: str) -> int:
    """find all houses visited atleast once
    with the help of the robot"""
    santa = (0, 0)
    robot = (0, 0)
    visited = {santa}
    for i in range(0, len(path)):
        x, y = move(path[i], santa if i % 2 == 0 else robot)
        if i % 2 == 0:
            santa = (x, y)
        else:
            robot = (x, y)
        visited.add((x, y))
    return len(visited)
