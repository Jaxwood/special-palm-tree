from typing import List


def storage_amount(lines: List[str]) -> int:
    # total length except begin and end
    size = 0
    memory = 0
    for line in lines:
        i = 0
        while i < len(line):
           # check begin and end of line
            if i == 0 or i == len(line) - 1:
                # do not increment memory
                size += 1
                i += 1
            # check for hexadecimal
            elif line[i] == '\\' and line[i+1] == 'x':
                size += 4
                memory += 1
                i += 4
            # check for escaped quote
            elif line[i] == '\\' and line[i+1] == '"':
                size += 2
                memory += 1
                i += 2
            # check for escaped backslash
            elif line[i] == '\\' and line[i+1] == '\\':
                size += 2
                memory += 1
                i += 2
            # otherwise increase by one
            else:
                size += 1
                memory += 1
                i += 1
    return size - memory
