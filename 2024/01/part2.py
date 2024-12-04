import numpy as np
import sys


def get_data(file:str) -> np.ndarray:

    return np.loadtxt(file, dtype=int)


def compute(data:np.ndarray) -> None:

    print(sum([i * np.sum(data[:,1] == i) for i in data[:,0] ]))


def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
