import numpy as np
import sys
from decorators.timer import timer

def load_data(file:str) -> np.ndarray[str]:

    return np.genfromtxt(file, comments=None, delimiter=",", dtype=int)

def pause():

  char = input("Enter a character ('q' to quit): ")
  if char.lower() == 'q':
    print("Exiting program.")
    sys.exit()

def solve(data:np.ndarray[str]) -> int:
    sys.setrecursionlimit(100000)

    def solve_helper(grid, loc, moves=0):

        r,c = loc

        if r < 0 or r >= n or c < 0 or c >= n:
            return

        if grid[r,c] in ("#","O"):
            return

        if (r,c) in visited and moves >= visited[(r,c)]:
            return
        else:
            visited[(r,c)] = moves

        if r == n-1 and c == n-1:
            scores.append(moves)
            return

        if grid[r,c] == ".":
            grid[r,c] = "O"

        if False:
            print()
            for _ in grid:
                print(''.join(_))
            print(f"{moves} moves")
            pause()

        solve_helper(grid, [r-1,c], moves+1)
        solve_helper(grid, [r,c+1], moves+1)
        solve_helper(grid, [r+1,c], moves+1)
        solve_helper(grid, [r,c-1], moves+1)

        grid[r,c] = "."

    if "data.txt" == "test.txt":
        n = 7
        b = 12
    else:
        n = 71
        b = 1024

    grid = np.full((n,n), ".")
    s = np.argwhere(grid == '.')[0]
    e = np.argwhere(grid == '.')[-1]

    for c,r in data[:b]:
        grid[r,c] = "#"

    scores = []
    visited = dict()
    sr,sc = s
    solve_helper(grid,s)

    result = min(scores)
    return result
@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
