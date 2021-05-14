def floors(str):
    """find the end floor"""
    floor = 0
    for i in str:
        if i == '(':
            floor += 1
        else:
            floor -= 1
    return floor


def basement(str):
    """find the basement floor"""
    floor = 0
    cnt = 0
    for i in str:
        if i == '(':
            floor += 1
        else:
            floor -= 1
        cnt += 1
        if floor == -1:
            return cnt
    return 0
