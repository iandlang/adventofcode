import numpy as np
from decorators.timer import timer


def load_data(file: str) -> np.ndarray:
    with open(file) as f:
        return np.array([list(line.strip()) for line in f])


def solve(data: np.ndarray) -> int:
    result = 0
    for r in range(1, data.shape[0] - 1):
        for c in range(1, data.shape[1] - 1):
            if data[r, c] == "A":
                d1 = ''.join([data[r - 1, c - 1], data[r + 1, c + 1]])
                d2 = ''.join([data[r + 1, c - 1], data[r - 1, c + 1]])
                result += d1 in ("MS", "SM") and d2 in ("MS", "SM")
    return result


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
