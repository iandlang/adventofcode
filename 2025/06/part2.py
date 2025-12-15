from decorators.timer import timer
from functools import reduce
from typing import Iterator

def load_data(file: str) -> Iterator[tuple[str, ...]]:
    with open(file) as f:
        data = [line[:-1] for line in f]
    return zip(*data)

def calculate(data: tuple[str, ...]) -> int:
    result = 0
    for line in data:
        num = ("".join(line[:-1]).strip())

        if num != "" and line[-1] in ("+", "*"):
            # print("setting op")
            op = line[-1]
            calc = 0 if op == "+" else 1

        # print(f"line {line} nums {nums} op {op} calc {calc}")


        if num != "":
            if op == "*":
                calc *= int(num)
                # print(f"op {op} {calc} {nums}")
            if op == "+":
                calc += int(num)
                # print(f"op {op} {calc} {nums}")
        else:
            # print(f"calc: {calc}")
            result += calc
            # print(f"result: {result}")
            calc = 0
    result += calc
    return result

def solve(data: Iterator[tuple[str, ...]]) -> int:
    return calculate(data)

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()