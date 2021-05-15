def houses(path: str) -> int:
    """find all houses visited atleast once"""
    current = (0, 0)
    visited = {current}
    for s in path:
        x, y = current
        if s == '>':
            x += 1
        if s == '<':
            x -= 1
        if s == '^':
            y += 1
        if s == 'v':
            y -= 1
        current = (x, y)
        visited.add(current)
    return len(visited)


def robot_houses(path: str) -> int:
    """find all houses visited atleast once
    with the robot as help"""
    santa = (0, 0)
    robot = (0, 0)
    visited = {santa}
    for i in range(0, len(path)):
        x, y = santa if i % 2 == 0 else robot
        s = path[i]
        if s == '>':
            x += 1
        if s == '<':
            x -= 1
        if s == '^':
            y += 1
        if s == 'v':
            y -= 1
        if i % 2 == 0:
            santa = (x, y)
        else:
            robot = (x, y)
        visited.add((x, y))
    return len(visited)
