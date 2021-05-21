from typing import Dict, List, Tuple
import math

Grid = Dict[Tuple[int, int], str]


def parse(raw: List[str]) -> Grid:
    """parse initial grid"""
    result = {}
    for i, line in enumerate(raw):
        for j, c in enumerate(line):
            result[(j, i)] = c
    return result


def tuple_sum(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    """add two tuples"""
    [x, y] = a
    [z, w] = b
    return (x+z, y+w)


def is_edge(grid: Grid, coord: Tuple[int, int]) -> bool:
    """check if an edge coordinate"""
    wide = int(math.sqrt(len(grid))) - 1
    return coord in set([(0, 0), (0, wide), (wide, 0), (wide, wide)])


def tick(grid: Grid, edge: bool = False) -> Grid:
    """simulate one step"""
    result: Grid = {}
    neighbors = [(1, 0), (0, 1), (1, 1), (-1, -1),
                 (-1, 0), (0, -1), (-1, 1), (1, -1)]
    for g in grid:
        next = map(lambda x: tuple_sum(x, g), neighbors)
        on = 0
        # count how many lights are on
        for n in next:
            candidate = grid.get(n)
            if candidate != None and candidate == '#':
                on = on + 1

        # update state
        if edge and is_edge(grid, g):
            result[g] = '#'
        elif grid.get(g) == '#':
            result[g] = '#' if on == 2 or on == 3 else '.'
        else:
            result[g] = '#' if on == 3 else '.'
    return result


def light_switcher(raw: List[str], steps: int, edge: bool = False) -> int:
    """runs simulation for x steps"""
    grid = parse(raw)
    # set edges on
    if edge:
        for g in grid:
            if is_edge(grid, g):
                grid[g] = '#'
    # run simulation
    for _ in range(steps):
        grid = tick(grid, edge)
    return len(list(filter(lambda x: x == '#', grid.values())))
