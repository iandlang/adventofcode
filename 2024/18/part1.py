import numpy as np
import sys
from decorators.timer import timer


def get_data(file:str) -> np.ndarray[str]:

    return np.genfromtxt(file, comments=None, delimiter=",", dtype=int)


def pause():

  char = input("Enter a character ('q' to quit): ")
  if char.lower() == 'q':
    print("Exiting program.")
    sys.exit()


def compute(data:np.ndarray[str]) -> None:

    def solve(grid, loc, moves=0):

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

        solve(grid, [r-1,c], moves+1)
        solve(grid, [r,c+1], moves+1)
        solve(grid, [r+1,c], moves+1)
        solve(grid, [r,c-1], moves+1)

        grid[r,c] = "."


    if sys.argv[1] == "test.txt":
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
    solve(grid,s)

    result = min(scores)
    print(result)

    answer = None
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    sys.setrecursionlimit(10000)
    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
