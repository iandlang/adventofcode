import numpy as np
from decorators.timer import timer


def load_data(file: str) -> np.ndarray:
    return np.loadtxt(file, dtype=int)


def solve(data: np.ndarray) -> int:
    return sum(i * np.sum(data[:, 1] == i) for i in data[:, 0])


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
