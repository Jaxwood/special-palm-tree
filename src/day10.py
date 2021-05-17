def look_and_say(candidate: str, times: int) -> str:
    result = candidate
    for _ in range(times):
        result = tick(result, '')
    return result


def tick(candidate: str, result: str) -> str:
    i = 0
    while i < len(candidate):
        c = candidate[i]
        j = i + 1
        while j < len(candidate) and c == candidate[j]:
            j += 1
        result += f'{j-i}{c}'
        i = j
    return result
