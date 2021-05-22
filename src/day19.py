from typing import Dict, List


def parse(raw: List[str]) -> Dict[str, List[str]]:
    result = {}
    for r in raw:
        [f, t] = r.split(' => ')
        if result.get(f) != None:
            lst = result.get(f)
            lst.append(t)
            result[f] = lst
        else:
            result[f] = [t]

    return result


def replace_once(raw: List[str], molecule: str) -> int:
    replacements = parse(raw)
    combinations = set()
    for i, m in enumerate(molecule):
        # pattern can also be of length 2
        substr = molecule[i:i+2]
        if replacements.get(m) != None:
            for r in replacements.get(m):
                new = molecule[:i] + r + molecule[i+1:]
                combinations.add(new)
        if replacements.get(substr) != None:
            for r in replacements.get(substr):
                new = molecule[:i] + r + molecule[i+2:]
                combinations.add(new)

    return len(combinations)
