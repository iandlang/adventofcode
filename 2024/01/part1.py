import numpy as np
import sys


def get_data(file:str) -> np.ndarray:

    return np.loadtxt(file, dtype=int)


def compute(data:np.ndarray) -> None:

    print(sum(abs(t[0] - t[1]) for t in zip(sorted(data[:,0]), sorted(data[:,1]))))


def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
