import re
import string
import sys
from typing import List


def get_data(file:str) -> List[str]:

    with open(sys.argv[1]) as f:
        return [line.strip() for line in f.readlines()]


def compute(data:List[str]) -> None:

    result = 0

    for line in data:

        b1 = False
        slist = []
        for s1 in string.ascii_lowercase:
            for s2 in string.ascii_lowercase:
                slist.append(s1+s2)
        for s in slist:
            if len(re.findall(s, line)) >= 2:
                b1 = True
                break

        b2 = False
        for s in string.ascii_lowercase:
            if len(re.findall(f"{s}.{s}", line)) > 0:
                b2 = True
                break

        result += b1 and b2

    print(result)


def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
