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
