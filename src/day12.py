from typing import Any
import simplejson as json


def sum_all(json: Any, sum: int) -> int:
    """recursively sum the json"""
    if isinstance(json, str):
        return sum
    if isinstance(json, int):
        return sum + int(json)
    for k in json:
        if isinstance(json, dict):
            sum = sum_all(json[k], sum)
        else:
            sum = sum_all(k, sum)
    return sum


def sum_except_red(json: Any, sum: int) -> int:
    """recursively sum the json"""
    if isinstance(json, str):
        return sum
    if isinstance(json, int):
        return sum + int(json)
    for k in json:
        if k == 'red':
            continue
        if isinstance(json, dict):
            if any(filter(lambda x: json[x] == 'red', json)):
                continue
            else:
                sum = sum_except_red(json[k], sum)
        else:
            sum = sum_except_red(k, sum)
    return sum


def sum(raw: str, all: bool = True) -> int:
    parsed = json.loads(raw)
    return sum_all(parsed, 0) if all else sum_except_red(parsed, 0)
