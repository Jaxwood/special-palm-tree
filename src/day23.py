from typing import List, Dict


class Instruction:
    def __init__(self):
        pass

    def execute(self, idx: int, memory: Dict[str, int]) -> int:
        return 0


class JIO(Instruction):
    def __init__(self, name: str, reg: str, val: int):
        self.name = name
        self.reg = reg
        self.val = val

    def execute(self, idx: int, memory: Dict[str, int]) -> int:
        if memory[self.reg] == 1:
            return idx + self.val
        else:
            return idx + 1

    def __repr__(self):
        return f'{self.name} {self.reg} {self.val}'


class TPL(Instruction):
    def __init__(self, name: str, reg: str):
        self.name = name
        self.reg = reg

    def execute(self, idx: int, memory: Dict[str, int]) -> int:
        memory[self.reg] *= 3
        return idx + 1

    def __repr__(self):
        return f'{self.name} {self.reg}'


class JMP(Instruction):
    def __init__(self, name: str, val: int):
        self.name = name
        self.val = val

    def execute(self, idx: int, memory: Dict[str, int]) -> int:
        return idx + self.val

    def __repr__(self):
        return f'{self.name} {self.val}'


class INC(Instruction):
    def __init__(self, name: str, reg: str):
        self.name = name
        self.reg = reg

    def execute(self, idx: int, memory: Dict[str, int]) -> int:
        memory[self.reg] += 1
        return idx + 1

    def __repr__(self):
        return f'{self.name} {self.reg}'


class HLF(Instruction):
    def __init__(self, name: str, reg: str):
        self.name = name
        self.reg = reg

    def execute(self, idx: int, memory: Dict[str, int]) -> int:
        memory[self.reg] //= 2
        return idx + 1

    def __repr__(self):
        return f'{self.name} {self.reg}'


class JIE(Instruction):
    def __init__(self, name: str, reg: str, val: int):
        self.name = name
        self.reg = reg
        self.val = val

    def execute(self, idx: int, memory: Dict[str, int]) -> int:
        if memory[self.reg] % 2 == 0:
            return idx + self.val
        else:
            return idx + 1

    def __repr__(self):
        return f'{self.name} {self.reg} {self.val}'


def parse(data: List[str]) -> List[Instruction]:
    result = []
    for d in data:
        if d.startswith('jio'):
            segs = d.split(' ')
            result.append(JIO(segs[0], segs[1].strip(','), int(segs[2])))
        elif d.startswith('tpl'):
            segs = d.split(' ')
            result.append(TPL(segs[0], segs[1]))
        elif d.startswith('jmp'):
            segs = d.split(' ')
            result.append(JMP(segs[0], int(segs[1])))
        elif d.startswith('inc'):
            segs = d.split(' ')
            result.append(INC(segs[0], segs[1]))
        elif d.startswith('hlf'):
            segs = d.split(' ')
            result.append(HLF(segs[0], segs[1]))
        elif d.startswith('jie'):
            segs = d.split(' ')
            result.append(JIE(segs[0], segs[1].strip(','), int(segs[2])))
        else:
            print(f'unexpected {d}')
    return result


def run(data: List[str], override: bool = False) -> int:
    inst = parse(data)
    regs = {'a': 1 if override else 0, 'b': 0}
    idx = 0
    while True:
        if (idx < len(inst)):
            i = inst[idx]
        else:
            return regs['b']
        idx = i.execute(idx, regs)
