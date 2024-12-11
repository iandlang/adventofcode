import numpy as np
import sys
from decorators.timer import timer as timeit


def get_data(file:str) -> np.ndarray[str]:

    with open(file) as f:
        return [int(c) for c in f.read().strip().split(',')]


def compute(data:np.ndarray[str]) -> None:

    d = {i:0 for i in range(9)}

    for i in data:
        d[i] += 1

    for _ in range(256):
        d2 = d.copy()
        for timer, fish in d.items():
            if timer == 0:
                d2[6] += d[0]
                d2[8] += d[0]
                d2[0] = 0
            else:
                d2[timer - 1] += d[timer]
                d2[timer] -= d[timer]
        d = d2.copy()

    result = sum(d.values())
    print(result)

    answer = None
    if answer:
        assert(result == answer)


@timeit
def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
