from decorators.timer import timer
from functools import reduce
from typing import Iterator

def load_data(file: str) -> Iterator[tuple[str, ...]]:
    with open(file) as f:
        data = [line.split() for line in f.read().splitlines()]
    return zip(*data)

def calculate(line: tuple[str, ...]) -> int:
    *strs, op = line
    ints = map(int, strs)
    if op == "+":
        return sum(ints)
    return reduce(lambda x, y: x * y, ints)

def solve(data: Iterator[tuple[str, ...]]) -> int:
    return sum(calculate(line) for line in data)

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()