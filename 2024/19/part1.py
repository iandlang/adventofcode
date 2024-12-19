import numpy as np
import re
import sys
from decorators.timer import timer


def get_data(file:str) -> np.ndarray[str]:

    with open(file) as f:
       carpets, patterns = f.read().split("\n\n")

    carpets = tuple(carpets.split(", "))
    patterns = tuple(patterns.splitlines())

    return carpets, patterns


def solve(pattern, carpets):

    if pattern == '':
        return True

    for carpet in carpets:
        match =  re.match(f"^{carpet}(.*)", pattern)
        if match:
            if solve(match[1], carpets):
                return True

    return False


def compute(carpets, patterns) -> None:

    result = sum(solve(pattern,carpets) for pattern in patterns)
    print(result)

    answer = 269
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    sys.setrecursionlimit(10000)
    carpets, patterns  = get_data(sys.argv[1])
    compute(carpets, patterns)


if __name__ == "__main__":
    main()
