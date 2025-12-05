import numpy as np
import sys
from decorators.timer import timer

def load_data(file:str) -> np.ndarray[str]:

    with open(file) as f:
        return np.array([list(line) for line in f.read().splitlines()])

def solve(grid:np.ndarray[str]) -> int:
    sys.setrecursionlimit(100000)

    def solve_helper(grid, loc, moves=1):

        r,c = loc

        if r < 0 or r >= n or c < 0 or c >= n:
            return False

        if grid[r,c] in ("#","O"):
            return False

        if track[(r,c)] > 0:
            return False
        else:
            track[(r,c)] = moves

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

        if solve_helper(grid, [r-1,c], moves+1):
            return True
        elif solve_helper(grid, [r,c+1], moves+1):
            return True
        elif solve_helper(grid, [r+1,c], moves+1):
            return True
        elif solve_helper(grid, [r,c-1], moves+1):
            return True

        grid[r,c] = "."

        return False

    def find_cheats(sr,sc,r,c,m):

        if 0 < r < n and 0 < c < n:
            pass
        else:
            return

        if m == 21:
            return;

        if visited[(r,c)] == 0:
            visited[(r,c)] = m
        else:
            if visited[(r,c)] <= m:
                return
            else:
                visited[(r,c)] = m

        if track[r,c] > 0:
            saved = track[r,c] - track[sr,sc] - m
            if saved >= 100:
                cheats[(sr,sc),(r,c)] = int(saved)

        find_cheats(sr,sc,r-1,c,m+1)
        find_cheats(sr,sc,r,c+1,m+1)
        find_cheats(sr,sc,r+1,c,m+1)
        find_cheats(sr,sc,r,c-1,m+1)

    n = grid.shape[0]
    s = np.argwhere(grid == 'S')[0]
    e = np.argwhere(grid == 'E')[0]
    track = np.zeros(grid.shape, dtype=int)

    solve_helper(grid,s)

    cheats = {}
    for r in range(n):
        for c in range(n):
            if track[r,c] > 0:
                visited = np.zeros(grid.shape, dtype=int)
                find_cheats(r,c,r,c,0)

    result = len(cheats)
    return result
@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
