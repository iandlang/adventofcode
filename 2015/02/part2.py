import sys
from typing import List


def get_data(file:str) -> List[int]:

    with open(sys.argv[1]) as f:
        return [[int(c) for c in line.strip().split("x")] for line in f.readlines()]


def compute(data:List[int]) -> None:

    result = 0

    for t in data:
        t.sort()
        result += 2*t[0] + 2*t[1] + t[0]*t[1]*t[2]

    print(result)


def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
