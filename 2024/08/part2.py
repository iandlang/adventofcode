from itertools import count
import numpy as np
import string
from decorators.timer import timer


def load_data(file: str) -> np.ndarray:
    return np.genfromtxt(file, converters={0: list})


def solve(data: np.ndarray) -> int:
    rowcount, colcount = data.shape
    antinodes = np.zeros(data.shape, dtype=bool)

    for c in string.ascii_lowercase + string.ascii_uppercase + "0123456789":
        cells = np.argwhere(data == c)
        for c1 in cells:
            for c2 in cells:
                if not np.array_equal(c1, c2):
                    for i in count(0):
                        c = c1 + (c1 - c2) * i
                        if 0 <= c[0] < rowcount and 0 <= c[1] < colcount:
                            antinodes[c[0], c[1]] = True
                        else:
                            break

    return np.count_nonzero(antinodes)


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
