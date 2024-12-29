import numpy as np
import sys
from decorators.timer import timer


def get_data(file:str) -> np.ndarray[str]:

    return np.genfromtxt(file, comments=None, converters={0:list})


def pause():
  """Reads a character from input. Exits the program if it's 'q',
  otherwise continues.
  """

  char = input("Enter a character ('q' to quit): ")
  if char.lower() == 'q':
    print("Exiting program.")
    sys.exit()  # or sys.exit() if you import sys


def compute(data:np.ndarray[str]) -> None:

    def solve(grid, loc, direction, score=0):

        r,c = loc

        if grid[r,c] == "E":
            scores.append(score)
            return

        if grid[r,c] in ("#","O"):
            return

        if grid[r,c] == ".":
            grid[r,c] = "O"

        at_intersection = sum([grid[r+1,c] == ".", grid[r-1,c] == ".", grid[r,c+1] == ".", grid[r,c-1] == "."]) > 1
        if (r,c) in visited and visited[(r,c)] < score and not at_intersection:
            grid[r,c] = "."
            return
        else:
            visited[(r,c)] = score

        if False:
            for _ in grid:
                print(''.join(_))
            pause()

        current_score = score
        solve(grid, [r-1,c], "N", score+1+1000*(direction != "N"))
        solve(grid, [r,c+1], "E", score+1+1000*(direction != "E"))
        solve(grid, [r+1,c], "S", score+1+1000*(direction != "S"))
        solve(grid, [r,c-1], "W", score+1+1000*(direction != "W"))

        at_dead_end = sum([grid[r+1,c] == "#", grid[r-1,c] == "#", grid[r,c+1] == "#", grid[r,c-1] == "#"]) == 3
        if at_dead_end:
            grid[r,c] = "#"
        else:
            grid[r,c] = "."
        score = current_score


    n = len(data)
    s = np.argwhere(data == 'S')[0]
    e = np.argwhere(data == 'E')[0]

    scores = []
    visited = dict()
    sr,sc = s
    solve(data,s,'E')

    result = min(scores)
    print(result)

    answer = (7036,11048,104516)
    if answer:
        assert(result in answer)


@timer
def main() -> None:

    sys.setrecursionlimit(10000)
    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
