import numpy as np
import sys
from decorators.timer import timer


def get_data(file:str) -> np.ndarray[str]:

    return np.genfromtxt(file, comments=None, converters={0:list})


def compute(data:np.ndarray[str]) -> None:

    def solve(grid, loc):

        r,c = loc
        height = int(grid[r,c])

        if height == 9:
            paths[thr,thc] += 1
            return

        if r > 0 and int(grid[r-1,c]) == height + 1:
                solve(grid, [r-1,c])

        if c < n-1 and int(grid[r,c+1]) == height + 1:
                solve(grid, [r,c+1])

        if r < n-1 and int(grid[r+1,c]) == height + 1:
                solve(grid, [r+1,c])

        if c > 0 and int(grid[r,c-1]) == height + 1:
                solve(grid, [r,c-1])

    n = len(data)
    trailheads = np.argwhere(data == '0')
    paths=np.zeros(shape=data.shape, dtype=int)

    for th in trailheads:
        thr,thc = th
        solve(data,th)

    result = np.sum(paths)
    print(result)

    answer = 1801
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
