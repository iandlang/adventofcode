from functools import cache
import numpy as np
from pprint import pprint as pp
from decorators.timer import timer

def load_data(file:str) -> dict:

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

    return {'program': program, 'registers': registers}

def solve(data: dict) -> int:
    answer = data['program']

    A0 = 0
    inc = 1
    search = 1
    print(f"incrementing by {inc} looking for {search} characters")

    while True:

        A = A0
        B = 0
        C = 0
        output = []

        while A > 0:

            B = A % 8
            B = B ^ 1
            C = A // 2**B
            B = B ^ 4
            A = A // 8
            B = B ^ C
            output.append(B % 8)

            if output != answer[:len(output)]:
                break
            elif len(output) == search:
                print(f"A0:{A0} found match for first {len(output)} digits output:{output}")
                if len(output) == 16:
                    break
                elif len(output) == 7:
                    inc = 1
                else:
                    inc *= 8
                search += 1
                print(f"incrementing by {inc} looking for {search} characters")

        if output == answer:
            break

        A0 += inc

    result = A0
    return A0


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
