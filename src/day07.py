import re
from typing import Deque, Dict, List, Tuple
from collections import deque


class Instruction:
    def __init__(self) -> None:
        pass


class AssignmentInstruction(Instruction):
    def __init__(self, left: str, right: str) -> None:
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'{self.left} -> {self.right}'

    def execute(self, state: Dict[str, int]) -> Tuple[Dict[str, int], bool]:
        if self.right.isnumeric():
            state[self.left] = int(self.right)
            return (state, True)
        elif state.get(self.right) is not None:
            state[self.left] = state[self.right]
            return (state, True)
        else:
            return (state, False)


class NotInstruction(Instruction):
    def __init__(self, left: str, to: str) -> None:
        self.left = left
        self.to = to

    def __repr__(self) -> str:
        return f'NOT {self.left} -> {self.to}'

    def execute(self, state: Dict[str, int]) -> Tuple[Dict[str, int], bool]:
        # 16 bits
        if state.get(self.left) is not None:
            state[self.to] = 65535 - state[self.left]
            return (state, True)
        else:
            return (state, False)


class RightShiftInstruction(Instruction):
    def __init__(self, left: str, right: int, to: str) -> None:
        self.left = left
        self.right = right
        self.to = to

    def __repr__(self) -> str:
        return f'{self.left} RSHIFT {self.right} -> {self.to}'

    def execute(self, state: Dict[str, int]) -> Tuple[Dict[str, int], bool]:
        if state.get(self.left) is not None:
            state[self.to] = state[self.left] >> int(self.right)
            return (state, True)
        else:
            return (state, False)


class LeftShiftInstruction(Instruction):
    def __init__(self, left: str, right: int, to: str) -> None:
        self.left = left
        self.right = right
        self.to = to

    def __repr__(self) -> str:
        return f'{self.left} LSHIFT {self.right} -> {self.to}'

    def execute(self, state: Dict[str, int]) -> Tuple[Dict[str, int], bool]:
        if state.get(self.left) is not None:
            state[self.to] = state[self.left] << int(self.right)
            return (state, True)
        else:
            return (state, False)


class OrInstruction(Instruction):
    def __init__(self, left: str, right: str, to: str) -> None:
        self.left = left
        self.right = right
        self.to = to

    def __repr__(self) -> str:
        return f'{self.left} OR {self.right} -> {self.to}'

    def execute(self, state: Dict[str, int]) -> Tuple[Dict[str, int], bool]:
        if state.get(self.left) is not None and state.get(self.right) is not None:
            state[self.to] = state[self.left] | state[self.right]
            return (state, True)
        else:
            return (state, False)


class AndInstruction(Instruction):
    def __init__(self, left: str, right: str, to: str) -> None:
        self.left = left
        self.right = right
        self.to = to

    def __repr__(self) -> str:
        return f'{self.left} AND {self.right} -> {self.to}'

    def execute(self, state: Dict[str, int]) -> Tuple[Dict[str, int], bool]:
        if state.get(self.left) is not None and state.get(self.right) is not None:
            state[self.to] = state[self.left] & state[self.right]
            return (state, True)
        elif self.left.isnumeric() and state.get(self.right) is not None:
            state[self.to] = int(self.left) & state[self.right]
            return (state, True)
        else:
            return (state, False)


def parse(instructions: List[str]) -> Deque[Instruction]:
    result: Deque[Instruction] = deque()
    assignmentRegex = re.compile('(\w+) -> (\w+)')
    andRegex = re.compile('(\w+) AND (\w+) -> (\w+)')
    orRegex = re.compile('(\w+) OR (\w+) -> (\w+)')
    leftshiftRegex = re.compile('(\w+) LSHIFT (\d+) -> (\w+)')
    rightshiftRegex = re.compile('(\w+) RSHIFT (\d+) -> (\w+)')
    notRegex = re.compile('NOT (\w+) -> (\w+)')
    for inst in instructions:
        if assignmentRegex.match(inst):
            [(num, registry)] = assignmentRegex.findall(inst)
            result.append(AssignmentInstruction(registry, num))
        if andRegex.match(inst):
            [(l, r, t)] = andRegex.findall(inst)
            result.append(AndInstruction(l, r, t))
        if orRegex.match(inst):
            [(l, r, t)] = orRegex.findall(inst)
            result.append(OrInstruction(l, r, t))
        if leftshiftRegex.match(inst):
            [(l, r, t)] = leftshiftRegex.findall(inst)
            result.append(LeftShiftInstruction(l, r, t))
        if rightshiftRegex.match(inst):
            [(l, r, t)] = rightshiftRegex.findall(inst)
            result.append(RightShiftInstruction(l, r, t))
        if notRegex.match(inst):
            [(l, r)] = notRegex.findall(inst)
            result.append(NotInstruction(l, r))
    return result


def circuit(rawInstructions: List[str]) -> Dict[str, int]:
    instructions = parse(rawInstructions)
    state = {}
    while len(instructions) > 0:
        instruction = instructions.popleft()
        (state, done) = instruction.execute(state)
        if not done:
            instructions.append(instruction)
    return state
