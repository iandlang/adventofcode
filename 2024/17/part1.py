from functools import cache
import numpy as np
from pprint import pprint as pp
import sys
from decorators.timer import timer


def get_data(file:str) -> np.ndarray[str]:

    registers = {}
    with open(file) as f:
        for line in [line.strip() for line in f]:
            if 'Register A' in line:
                registers['A'] = int(line.split()[-1])
            if 'Register B' in line:
                registers['B'] = int(line.split()[-1])
            if 'Register C' in line:
                registers['C'] = int(line.split()[-1])
            if 'Program' in line:
               program = list(map(int, line.split()[-1].split(",")))

    return program, registers


def compute(program,registers) -> None:

    A = registers["A"]
    B = registers["B"]
    C = registers["C"]

    program = [(program[i],program[i+1])for i in range(0,len(program),2)]

    ip = 0
    output = []

    while ip < len(program):

        opcode = program[ip][0]
        operand = program[ip][1]

        if 0 <= operand <= 3:
            combo = operand
        elif operand == 4:
            combo = A
        elif operand == 5:
            combo = B
        elif operand == 6:
            combo = C

        if opcode == 0:
            A = int(A/2**combo)
        elif opcode == 1:
            B = B ^ operand
        elif opcode == 2:
            B = combo % 8
        elif opcode == 3:
            if A == 0:
                pass
                ip += 1
                continue
            else:
                ip = operand
                continue
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            output.append(combo%8)
        elif opcode == 6:
            B = int(A/2**combo)
        elif opcode == 7:
            C = int(A/2**combo)

        ip += 1

    result = ",".join(map(str, output))
    print(result)

    answer = '5,1,4,0,5,1,0,2,6'
    if answer:
        assert(result in answer)


@timer
def main() -> None:

    program,registers = get_data(sys.argv[1])
    compute(program,registers)


if __name__ == "__main__":
    main()
