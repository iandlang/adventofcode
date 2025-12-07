from decorators.timer import timer
from typing import Any

def load_data(file: str) -> list[list[str]]:
    with open(file) as f:
        return [list(line) for line in f.read().splitlines()]

def solve(data: list[list[Any]]) -> int:

    for row in range(1, len(data), 2):
        data[row] = [0] * len(data[row])
    data[1][data[0].index("S")] = 1

    for row in range(3, len(data), 2):
        for col in range(len(data[row])):
            if data[row - 1][col] == "^":
                data[row][col - 1] += data[row - 2][col]
                data[row][col + 1] += data[row - 2][col]
            else:
                data[row][col] += data[row - 2][col]

    return sum(data[-1])

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()