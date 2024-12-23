from itertools import chain
import sys
from typing import List
from decorators.timer import timer


def get_data(file:str) -> List[int]:

    with open(file) as f:
        return [int(c) for c in f.readlines()]


def gen(n):

    n = (n * 64 ^ n) % 2**24
    n = (n // 32 ^ n) % 2**24
    n = (n * 2048 ^ n) % 2**24

    return n


def compute(data:List[int]) -> None:

    buyer_price_changes = []
    for secret in data:
        n = secret
        changes = []
        d={}
        price = secret % 10
        for i in range(2000):
            n = gen(n)
            price_change = n%10 - price
            changes.append(price_change)
            price = n % 10
            if i >= 3:
                price_change_sequence = changes[i-3:i+1]
                k = tuple(changes[i-3:i+1])
                if k not in d:
                    d[k] = price
        buyer_price_changes.append(d)

    unique_price_changes = list(set(chain.from_iterable(d.keys() for d in buyer_price_changes)))

    result = max(sum(buyer.get(price_change, 0) for buyer in buyer_price_changes) for price_change in unique_price_changes)
    print(result)

    answer = 1568
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
