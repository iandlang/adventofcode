import re
import sys
from typing import List


def get_data(file:str) -> List[List[int]]:

    with open(sys.argv[1]) as f:
        return [[int(x) for x in line.strip().split(" ")] for line in f]


def compute(data:List[List[int]]) -> None:

    result = 0

    for line in data:
        tuples = list(zip(line,line[1:]))
        diffs = [abs(b - a) for a, b in tuples]
        signs = [b > a for a, b in tuples]
        result += min(diffs) > 0 and max(diffs) < 4 and len(set(signs)) == 1

    print(result)


def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
