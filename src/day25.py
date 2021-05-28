from typing import Dict, Tuple


def calculate(prev: int) -> int:
    return prev * 252533 % 33554393


def code(r: int, c: int) -> int:
    column = 1
    val = 20151125
    row = 2
    while row != r or column != c:
        val = calculate(val)
        if row == 1:
            row = column + 1
            column = 1
        else:
            row -= 1
            column += 1
    return calculate(val)
