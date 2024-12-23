from functools import reduce
import sys
from typing import List
from decorators.timer import timer


def get_data(file:str) -> List[int]:

    with open(file) as f:
        return [int(c) for c in f.readlines()]


def gen(n:int) -> int:

    n = (n * 64 ^ n) % 2**24
    n = (n // 32 ^ n) % 2**24
    n = (n * 2048 ^ n) % 2**24

    return n


def compute(data:List[int]) -> None:

    result = sum(reduce(lambda n,_: gen(n), range(2000), secret) for secret in data)

    print(result)

    answer = 14082561342
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
