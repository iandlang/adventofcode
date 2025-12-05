import numpy as np
import sys
from decorators.timer import timer

def load_data(file:str) -> np.ndarray[str]:

    return np.genfromtxt(file, comments=None, converters={0:list})

def pause():
  """Reads a character from input. Exits the program if it's 'q',
  otherwise continues.
  """

  char = input("Enter a character ('q' to quit): ")
  if char.lower() == 'q':
    print("Exiting program.")
    sys.exit()  # or sys.exit() if you import sys

def solve(data:np.ndarray[str]) -> int:
    sys.setrecursionlimit(100000)

    def solve_helper(grid, loc, direction, score=0):

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
        solve_helper(grid, [r-1,c], "N", score+1+1000*(direction != "N"))
        solve_helper(grid, [r,c+1], "E", score+1+1000*(direction != "E"))
        solve_helper(grid, [r+1,c], "S", score+1+1000*(direction != "S"))
        solve_helper(grid, [r,c-1], "W", score+1+1000*(direction != "W"))

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
    solve_helper(data,s,'E')

    result = min(scores)
    return result
@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
