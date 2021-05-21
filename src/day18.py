from typing import Dict, List, Tuple

Grid = Dict[Tuple[int, int], str]


def parse(raw: List[str]) -> Grid:
    result = {}
    for i, line in enumerate(raw):
        for j, c in enumerate(line):
            result[(j, i)] = c
    return result


def tuple_sum(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    [x, y] = a
    [z, w] = b
    return (x+z, y+w)


def tick(grid: Grid) -> Grid:
    result: Grid = {}
    neighbors = [(1, 0), (0, 1), (1, 1), (-1, -1),
                 (-1, 0), (0, -1), (-1, 1), (1, -1)]
    for g in grid:
        next = map(lambda x: tuple_sum(x, g), neighbors)
        on = 0
        for n in next:
            candidate = grid.get(n)
            if candidate != None and candidate == '#':
                on = on + 1
        if grid.get(g) == '#':
            result[g] = '#' if on == 2 or on == 3 else '.'
        else:
            result[g] = '#' if on == 3 else '.'
    return result


def light_switcher(raw: List[str], steps: int) -> int:
    grid = parse(raw)
    for _ in range(steps):
        grid = tick(grid)
    return len(list(filter(lambda x: x == '#', grid.values())))
