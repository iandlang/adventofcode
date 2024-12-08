import numpy as np
import string
import sys
from decorators.timer import timer


def get_data(file:str) -> np.ndarray[str]:

    return np.genfromtxt(file, converters={0:list})


def compute(data:np.ndarray[str]) -> None:

    rowcount, colcount = data.shape
    antinodes = np.zeros(data.shape, dtype=bool)

    for c in string.ascii_lowercase + string.ascii_uppercase + "0123456789":

        cells = np.argwhere(data == c)

        for c1 in cells:
            for c2 in cells:
                if not np.array_equal(c1,c2):
                    c = c1 + (c1 - c2)
                    if 0 <= c[0] < rowcount and 0 <= c[1] < colcount:
                        antinodes[c[0],c[1]] = True

    result = np.count_nonzero(antinodes)
    print(result)

    answer = 303
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
