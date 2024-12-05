import sys
from typing import List


def get_data(file:str) -> List[str]:

    with open(sys.argv[1]) as f:
        return list(''.join([line.strip() for line in f.readlines()]))


def compute(data:List[str]) -> None:

    print(data.count('(') - data.count(')'))


def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
