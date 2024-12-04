import re
import sys
from typing import List


def get_data(file:str) -> List[str]:

    with open(sys.argv[1]) as f:
        return [line.strip() for line in f]


def compute(data:List[str]) -> None:

    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", ''.join(data))
    print(sum(int(x) * int(y) for x, y in matches))


def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
