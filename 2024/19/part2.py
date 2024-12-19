import numpy as np
import re
import sys
from decorators.timer import timer
from functools import cache

def get_data(file:str) -> np.ndarray[str]:

    with open(file) as f:
       carpets, patterns = f.read().split("\n\n")

    carpets = tuple(carpets.split(", "))
    patterns = tuple(patterns.splitlines())

    return carpets, patterns


@cache
def solve(pattern, carpets):

    if pattern == '':
        return 1
    else:
        return sum(solve(pattern[re.match(carpet, pattern).end():], carpets) for carpet in carpets if re.match(carpet, pattern))


def compute(carpets, patterns) -> None:


    result = sum(solve(pattern,carpets) for pattern in patterns)
    print(result)

    answer = 758839075658876
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    sys.setrecursionlimit(10000)
    carpets, patterns  = get_data(sys.argv[1])
    compute(carpets, patterns)


if __name__ == "__main__":
    main()
