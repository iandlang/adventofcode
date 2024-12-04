import numpy as np
import re
import sys


def get_data(file:str) -> np.ndarray:

    with open(sys.argv[1]) as f:
        return np.array([list(line.strip()) for line in f])


def compute(data:np.ndarray) -> None:

    count_xmas = lambda line: len(re.findall('XMAS',''.join(line)))

    result = 0

    for _ in range(4):
        data = np.rot90(data)
        result += sum(count_xmas(row) for row in data)
        result += sum(count_xmas(np.diagonal(data, i)) for i in range(-data.shape[0] + 1, data.shape[1]))

    print(result)


def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
