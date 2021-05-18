from typing import Any
import simplejson as json


def summer(json: Any, sum: int) -> int:
    """recursively sum the json"""
    if isinstance(json, str):
        return sum
    if isinstance(json, int):
        return sum + int(json)
    for k in json:
        if isinstance(json, dict):
            sum = summer(json[k], sum)
        else:
            sum = summer(k, sum)
    return sum


def sum(raw: str) -> int:
    parsed = json.loads(raw)
    return summer(parsed, 0)
