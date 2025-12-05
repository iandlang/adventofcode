import re
from decorators.timer import timer


def load_data(file: str) -> list[str]:
    with open(file) as f:
        return [line.strip() for line in f]


def solve(data: list[str]) -> int:
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", ''.join(data))
    return sum(int(x) * int(y) for x, y in matches)


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
