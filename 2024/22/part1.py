from functools import reduce
from typing import List
from decorators.timer import timer

def load_data(file:str) -> List[int]:

    with open(file) as f:
        return [int(c) for c in f.readlines()]

def gen(n:int) -> int:

    n = (n * 64 ^ n) % 2**24
    n = (n // 32 ^ n) % 2**24
    n = (n * 2048 ^ n) % 2**24

    return n

def solve(data:List[int]) -> int:

    result = sum(reduce(lambda n,_: gen(n), range(2000), secret) for secret in data)

    return result
@timer
def main() -> None:

    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
