import numpy as np
import sys
from decorators.timer import timer


def get_data(file:str) -> np.ndarray[str]:

    with open(file) as f:
         grid = f.read()

    grid = np.array([list(line) for line in grid.splitlines()])

    return grid


def compute(grid:np.ndarray[str]) -> None:

    def solve(grid, loc, moves=0):

        r,c = loc

        if r < 0 or r >= n or c < 0 or c >= n:
            return False

        if grid[r,c] in ("#","O"):
            return False

        if visited[(r,c)] > 0:
            return False
        else:
            visited[(r,c)] = moves

        if grid[r,c] == "E":
            return True

        if grid[r,c] == ".":
            grid[r,c] = "O"

        if False:
            print()
            for _ in grid:
                print(''.join(_))
            print(f"{moves} moves")
            pause()

        if solve(grid, [r-1,c], moves+1):
            return True
        elif solve(grid, [r,c+1], moves+1):
            return True
        elif solve(grid, [r+1,c], moves+1):
            return True
        elif solve(grid, [r,c-1], moves+1):
            return True

        grid[r,c] = "."

        return False


    n = grid.shape[0]
    s = np.argwhere(grid == 'S')[0]
    e = np.argwhere(grid == 'E')[0]
    visited = np.zeros(grid.shape, dtype=int)

    solve(grid,s)

    def find_cheats(r,c):

        d = [(-1,0),(0,1),(1,0),(0,-1)]
        cheats = 0

        for dr,dc in d:
            r1=r+dr;c1=c+dc
            r2=r1+dr;c2=c1+dc
            if 0 <= r2 < n and 0 <= c2 < n:
                if visited[r1,c1] == 0 and visited[r2,c2] > 0 and visited[r2,c2] - visited[r,c] >= 100 + 2:
                    #print(f"shortcut from {r},{c} with value {visited[r,c]} to {r2},{c2} with value {visited[r2,c2]} saving {visited[r2,c2] - visited[r,c]}")
                    cheats += 1
        return cheats


    result = sum(find_cheats(r,c) for r in range(n) for c in range(n) if visited[r,c] > 0)
    print(result)

    answer = 1384
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    sys.setrecursionlimit(10000)
    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
