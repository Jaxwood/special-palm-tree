from typing import Dict, List, Set


def find_nice_strings(candidates: List[str]) -> int:
    """find strings that are nice"""
    sum = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for candidate in candidates:
        vowelCount = 0
        doubleCount = 0
        banned = list(filter(lambda s: candidate.find(
            s) != -1, ['ab', 'cd', 'pq', 'xy']))
        for i in range(0, len(candidate)):
            # check for vowels
            if candidate[i] in vowels:
                vowelCount += 1
            # check for double letter
            if i != len(candidate) - 1 and candidate[i] == candidate[i+1]:
                doubleCount += 1
        sum += 1 if vowelCount > 2 and doubleCount > 0 and len(
            banned) == 0 else 0

    return sum


def has_pair(s: str) -> bool:
    """find pair with no overlap"""
    segs: Dict[str, Set[int]] = {}
    for i in range(0, len(s) - 1):
        st = s[i] + s[i + 1]
        if st in segs:
            segs[st] = segs[st].union({i, i+1})
        else:
            segs[st] = {i, i+1}
    return any(filter(lambda s: len(s) == 4, segs.values()))


def has_repeating_letter(s: str) -> bool:
    """find repeating letter"""
    for i in range(0, len(s) - 2):
        if s[i] == s[i+2]:
            return True
    return False


def find_even_nicer_strings(candidates: List[str]) -> int:
    """find even nicer strings"""
    sum = 0
    for s in candidates:
        if has_pair(s) and has_repeating_letter(s):
            sum += 1
    return sum
