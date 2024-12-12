import numpy as np
import sys
from decorators.timer import timer


def get_data(file:str) -> np.ndarray[str]:

    return np.genfromtxt(file, comments=None, converters={0:list})


def solve(grid,r,c,regions,region,n):

    if regions[r,c] > 0:
        return

    regions[r,c] = region

    for nr,nc in ([r-1,c],[r,c+1],[r,c-1],[r+1,c]):
        if 0 <= nr <= n-1 and 0 <= nc <= n-1:
            if grid[nr,nc] == grid[r,c]:
                solve(grid,nr,nc,regions,region,n)


def compute(grid:np.ndarray[str]) -> None:

    n = len(grid)

    regions = np.zeros(grid.shape,dtype=int)

    region = 0
    for r in range(n):
        for c in range(n):
            if regions[r,c] == 0:
                region += 1
                solve(grid,r,c,regions,region,n)

    _, region_size = np.unique(regions, return_counts=True)

    perimeters = {r:0 for r in range(0,region+1)}

    for r in range(n):
        for c in range(n):
            region = regions[r,c]
            m = n - 1
            perimeters[region] += r == 0 or grid[r,c] != grid[r-1,c]
            perimeters[region] += r == m or grid[r,c] != grid[r+1,c]
            perimeters[region] += c == 0 or grid[r,c] != grid[r,c-1]
            perimeters[region] += c == m or grid[r,c] != grid[r,c+1]

    result = sum(size * perimeters[i+1] for i, size in enumerate(region_size))

    print(result)

    answer = 1477762
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
