from collections import deque
from typing import Dict, Tuple
from decorators.timer import timer

def load_data(file: str) -> dict:
    bits = {}
    ops = deque([])
    bop = {'AND': '&', 'OR': '|', 'XOR': '^'}

    with open(file) as f:
        for line in f:
            line = line.strip()
            if ":" in line:
                gate, bit = line.split(": ")
                bits[gate] = int(bit)
            elif "->" in line:
                (bit1, op, bit2, eq, bit3) = line.split()
                ops.append((bit1, bop[op], bit2, bit3))

    return {'bits': bits, 'ops': ops}


def solve(data: dict) -> int:
    bits = data['bits']
    ops = data['ops']

    while ops:
        (bit1,op,bit2,bit3) = ops.popleft()
        if bit1 in bits and bit2 in bits:
            bits[bit3] = eval(f"bits['{bit1}'] {op} bits['{bit2}']")
        else:
            ops.append((bit1,op,bit2,bit3))

    result = sum(bits[f"z{str(i).zfill(2)}"] * 2**i for i in range(46))

    return result
@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
