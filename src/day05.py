from typing import List


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
