from collections import deque
from typing import Dict, Tuple
import sys
from decorators.timer import timer


def get_data(file:str) -> Tuple[Dict[str, int], deque]:

    bits = {}
    ops = deque([])
    bop = {'AND':'&','OR':'|','XOR':'^'}

    with open(file) as f:
        for line in f:
            line = line.strip()
            if ":" in line:
                gate,bit = line.split(": ")
                bits[gate] = int(bit)
            elif "->" in line:
                (bit1,op,bit2,eq,bit3) = line.split()
                ops.append((bit1,bop[op],bit2,bit3))

    return bits, ops


def compute(bits:Dict[str, int], ops:deque) -> None:

    while ops:
        (bit1,op,bit2,bit3) = ops.popleft()
        if bit1 in bits and bit2 in bits:
            bits[bit3] = eval(f"bits['{bit1}'] {op} bits['{bit2}']")
        else:
            ops.append((bit1,op,bit2,bit3))

    result = sum(bits[f"z{str(i).zfill(2)}"] * 2**i for i in range(46))

    print(result)

    answer = 48063513640678
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    bits, ops = get_data(sys.argv[1])
    compute(bits, ops)


if __name__ == "__main__":
    main()
