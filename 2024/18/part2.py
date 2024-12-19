import numpy as np
import sys
from decorators.timer import timer


def get_data(file:str) -> np.ndarray[str]:

    return np.genfromtxt(file, comments=None, delimiter=",", dtype=int)


def pause():
  """Reads a character from input. Exits the program if it's 'q',
  otherwise continues.
  """

  char = input("Enter a character ('q' to quit): ")
  if char.lower() == 'q':
    print("Exiting program.")
    sys.exit()  # or sys.exit() if you import sys


def compute(data:np.ndarray[str]) -> None:

    def solve(grid, loc, moves=0):

        r,c = loc

        if r < 0 or r >= n or c < 0 or c >= n:
            return False

        if grid[r,c] in ("#","O"):
            return False

        if (r,c) in visited:
            return False
        else:
            visited[(r,c)] = moves

        if r == n-1 and c == n-1:
            scores.append(moves)
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

    if sys.argv[1] == "test.txt":
        n = 7
        b = 12
        answer = [6,1]
    else:
        n = 71
        b = 1024
        answer = [8,51]

    grid = np.full((n,n), ".")
    s = np.argwhere(grid == '.')[0]
    e = np.argwhere(grid == '.')[-1]

    for i, (nc,nr) in enumerate(data[b:]):

        if i > 1:
            if grid[nr,nc] == ".":
                continue

        grid = np.full((n,n), ".")
        for (c,r) in data[:b+i+1]:
            grid[r,c] = "#"

        scores = []
        visited = dict()
        sr,sc = s
        if solve(grid,s):
            continue
        else:
            break

    result = [int(nc),int(nr)]
    print(result)

    if answer:
        assert(result == answer)


@timer
def main() -> None:

    sys.setrecursionlimit(10000)

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
