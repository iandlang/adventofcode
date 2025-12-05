import numpy as np
from decorators.timer import timer

def load_data(file:str) -> np.ndarray[str]:

    return np.genfromtxt(file, comments=None, converters={0:list})

def solve(data:np.ndarray[str]) -> int:

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
    return result
@timer
def main() -> None:

    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
