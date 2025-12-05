import numpy as np
import re
from decorators.timer import timer
from functools import cache

def load_data(file: str) -> dict:
    with open(file) as f:
        carpets, patterns = f.read().split("\n\n")

    carpets = tuple(carpets.split(", "))
    patterns = tuple(patterns.splitlines())

    return {'carpets': carpets, 'patterns': patterns}


@cache
def count_matches(pattern, carpets):
    if pattern == '':
        return 1
    else:
        return sum(count_matches(pattern[re.match(carpet, pattern).end():], carpets) for carpet in carpets if re.match(carpet, pattern))


def solve(data: dict) -> int:
    import sys
    sys.setrecursionlimit(10000)

    carpets = data['carpets']
    patterns = data['patterns']

    result = sum(count_matches(pattern, carpets) for pattern in patterns)
    return result


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
