import numpy as np
import re
from decorators.timer import timer

def load_data(file: str) -> dict:
    with open(file) as f:
        carpets, patterns = f.read().split("\n\n")

    carpets = tuple(carpets.split(", "))
    patterns = tuple(patterns.splitlines())

    return {'carpets': carpets, 'patterns': patterns}


def can_match(pattern, carpets):
    if pattern == '':
        return True

    for carpet in carpets:
        match = re.match(f"^{carpet}(.*)", pattern)
        if match:
            if can_match(match[1], carpets):
                return True

    return False


def solve(data: dict) -> int:
    import sys
    sys.setrecursionlimit(10000)

    carpets = data['carpets']
    patterns = data['patterns']

    result = sum(can_match(pattern, carpets) for pattern in patterns)
    return result


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
