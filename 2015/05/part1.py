import re
import sys
from typing import List


def get_data(file:str) -> List[str]:

    with open(sys.argv[1]) as f:
        return [line.strip() for line in f.readlines()]


def compute(data:List[str]) -> None:

    result = 0

    for line in data:

        b1 = len(re.findall('a|e|i|o|u', line)) >= 3
        b2 = any(t[0] == t[1] for t in zip(list(line), list(line)[1:]))
        b3 = not any([s in line for s in ['ab', 'cd', 'pq', 'xy']])

        result += b1 and b2 and b3

    print(result)


def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
