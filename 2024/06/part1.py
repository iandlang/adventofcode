import numpy as np
from decorators.timer import timer


def load_data(file: str) -> np.ndarray:
    with open(file) as f:
        return np.array([list(line.strip()) for line in f])


def solve(data: np.ndarray) -> int:
    loc = np.where(data == "^")
    r, c = loc[0][0], loc[1][0]
    data[r, c] = 'X'
    try:
        while True:
            arr = data[:r, c]
            i = np.where(arr == '#')[0][-1]
            arr[i + 1:] = "X"
            r = i + 1

            arr = data[r, c + 1:]
            i = np.where(arr == '#')[0][0]
            arr[:i] = "X"
            c += i

            arr = data[r + 1:, c]
            i = np.where(arr == '#')[0][0]
            arr[:i] = "X"
            r += i

            arr = data[r, :c]
            i = np.where(arr == '#')[0][-1]
            arr[i + 1:] = "X"
            c = i + 1
    except IndexError:
        arr[:] = "X"
        return np.count_nonzero(data == 'X')


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
