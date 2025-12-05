import numpy as np
import re
from decorators.timer import timer


def load_data(file: str) -> np.ndarray:
    with open(file) as f:
        return np.array([list(line.strip()) for line in f])


def solve(data: np.ndarray) -> int:
    count_xmas = lambda line: len(re.findall('XMAS', ''.join(line)))
    result = 0
    for _ in range(4):
        data = np.rot90(data)
        result += sum(count_xmas(row) for row in data)
        result += sum(count_xmas(np.diagonal(data, i)) for i in range(-data.shape[0] + 1, data.shape[1]))
    return result


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
