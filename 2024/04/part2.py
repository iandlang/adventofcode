import numpy as np
import sys


def get_data(file:str) -> np.ndarray:

    with open(sys.argv[1]) as f:
        return np.array([list(line.strip()) for line in f])


def compute(data:np.ndarray) -> None:

    result = 0

    for r in range(1, data.shape[0]-1):
        for c in range(1, data.shape[1]-1):
            if data[r, c] == "A":
                d1 = ''.join([data[r-1, c-1], data[r+1, c+1]])
                d2 = ''.join([data[r+1, c-1], data[r-1, c+1]])
                result += d1 in ("MS","SM") and d2 in ("MS","SM")

    print(result)


def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
