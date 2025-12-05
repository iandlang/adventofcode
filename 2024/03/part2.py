import re
from decorators.timer import timer


def load_data(file: str) -> list[str]:
    with open(file) as f:
        return [line.strip() for line in f]


def solve(data: list[str]) -> int:
    result = 0
    enabled = True
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|(don\'t\(\)|do\(\))", ''.join(data)):
        if match.groups()[2] == "don't()":
            enabled = False
        elif match.groups()[2] == "do()":
            enabled = True
        else:
            result += int(match.groups()[0]) * int(match.groups()[1]) * enabled
    return result


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
