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

    regionID, region_size = np.unique(regions, return_counts=True)

    perimeters = {r:0 for r in range(0,region+1)}

    for region in regionID:
        for r in range(n):
            for c in range(n):

                if regions[r,c] != region:
                    continue

                cell  = grid[r,c]
                m = n - 1

                ncell = grid[r-1,c] if r > 0 else -1
                scell = grid[r+1,c] if r < m else -1
                ecell = grid[r,c+1] if c < m else -1
                wcell = grid[r,c-1] if c > 0 else -1

                necell = grid[r-1,c+1] if r > 0 and c < m else -1
                nwcell = grid[r-1,c-1] if r > 0 and c > 0 else -1
                secell = grid[r+1,c+1] if r < m and c < m else -1
                swcell = grid[r+1,c-1] if r < m and c > 0 else -1

                perimeters[regions[r,c]] += cell != ncell and cell != ecell
                perimeters[regions[r,c]] += cell != ncell and cell != wcell
                perimeters[regions[r,c]] += cell != scell and cell != ecell
                perimeters[regions[r,c]] += cell != scell and cell != wcell

                perimeters[regions[r,c]] += cell == ncell and cell == ecell and cell != necell
                perimeters[regions[r,c]] += cell == ncell and cell == wcell and cell != nwcell
                perimeters[regions[r,c]] += cell == scell and cell == ecell and cell != secell
                perimeters[regions[r,c]] += cell == scell and cell == wcell and cell != swcell

    result = sum(size * perimeters[i+1] for i, size in enumerate(region_size))

    return result
@timer
def main() -> None:

    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
