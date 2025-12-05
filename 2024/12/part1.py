import numpy as np
from decorators.timer import timer

def load_data(file:str) -> np.ndarray[str]:

    return np.genfromtxt(file, comments=None, converters={0:list})

def flood_fill(grid,r,c,regions,region,n):

    if regions[r,c] > 0:
        return

    regions[r,c] = region

    for nr,nc in ([r-1,c],[r,c+1],[r,c-1],[r+1,c]):
        if 0 <= nr <= n-1 and 0 <= nc <= n-1:
            if grid[nr,nc] == grid[r,c]:
                flood_fill(grid,nr,nc,regions,region,n)

def solve(grid:np.ndarray[str]) -> int:

    n = len(grid)

    regions = np.zeros(grid.shape,dtype=int)

    region = 0
    for r in range(n):
        for c in range(n):
            if regions[r,c] == 0:
                region += 1
                flood_fill(grid,r,c,regions,region,n)

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

    return result
@timer
def main() -> None:

    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
