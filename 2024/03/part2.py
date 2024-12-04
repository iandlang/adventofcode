import re
import sys
from typing import List


def get_data(file:str) -> List[str]:

    with open(sys.argv[1]) as f:
        return [line.strip() for line in f]


def compute(data:List[str]) -> None:

    result=0
    enabled = True

    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|(don\'t\(\)|do\(\))", ''.join(data)):
        if match.groups()[2] == "don't()":
            enabled = False
        elif match.groups()[2] == "do()":
            enabled = True
        else:
            result += int(match.groups()[0]) * int(match.groups()[1]) * enabled

    print(result)


def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
