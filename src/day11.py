from typing import Dict, List


def is_valid(candidate: str) -> bool:
    valid = False
    pairs = 0
    j = 0
    for i in range(len(candidate)):
        # check pairs
        if j < i and i < len(candidate) - 1 and candidate[i] == candidate[i+1]:
            pairs += 1
            j = i + 1
        # do not allow i, l or o
        if candidate[i] == 'i' or candidate[i] == 'l' or candidate[i] == 'o':
            return False
        # check increasing characters
        if i < len(candidate) - 2 and ord(candidate[i]) + 1 == ord(candidate[i+1]) and ord(candidate[i+2]) - 1 == ord(candidate[i+1]):
            valid = True

    return valid and pairs > 1


def roll(candidate: str, idx: int) -> str:
    result = list(candidate)
    banned = set(['o', 'l', 'i'])
    if candidate[idx] == 'z':
        result[idx] = 'a'
        return roll(''.join(result), idx - 1)
    result[idx] = chr(ord(candidate[idx]) + 1) if chr(ord(candidate[idx]) +
                                                      1) not in banned else chr(ord(candidate[idx]) + 2)
    return ''.join(result)


def roll_password(candidate: str, force: bool = False) -> str:
    while force or is_valid(candidate) == False:
        force = False
        candidate = roll(candidate, len(candidate) - 1)
    return candidate
