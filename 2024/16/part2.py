import numpy as np
import sys
from decorators.timer import timer

min_score = 999999

def get_data(file:str) -> np.ndarray[str]:

    return np.genfromtxt(file, comments=None, converters={0:list})


def compute(data:np.ndarray[str]) -> None:


    def solve(grid, loc, direction, score=0):

        global min_score

        if False:
            for _ in grid:
                print(''.join(_))

            pause()

        r,c = loc

        if (r,c) in visited and visited[(r,c)] < score and sum([grid[r+1,c] == ".", grid[r-1,c] == ".", grid[r,c+1] == ".", grid[r,c-1] == "."]) == 1:
            return

        visited[(r,c)] = score

        ROWS,COLS=data.shape

        if grid[r,c] == "E":
            if score < min_score:
                paths[:] = 0
            if score <= min_score:
                min_score = score
                for i in range(ROWS):
                    for j in range(COLS):
                        if grid[i,j] in ["S","E","O"]:
                            paths[i,j] = 1
            return

        if grid[r,c] == ".":
            grid[r,c] = "O"

        current_score = score
        if r > 0 and grid[r-1,c] in (".","E"):
            solve(grid, [r-1,c], "N", score+1+1000*(direction != "N"))

        if c < n-1 and grid[r,c+1] in (".","E"):
            solve(grid, [r,c+1], "E", score+1+1000*(direction != "E"))

        if r < n-1 and grid[r+1,c] in (".","E"):
            solve(grid, [r+1,c], "S", score+1+1000*(direction != "S"))

        if c > 0 and grid[r,c-1] in (".","E"):
            solve(grid, [r,c-1], "W", score+1+1000*(direction != "W"))

        grid[r,c] = "."
        score = current_score


    n = len(data)
    s = np.argwhere(data == 'S')[0]
    e = np.argwhere(data == 'E')[0]
    paths=np.zeros(shape=data.shape, dtype=int)

    scores = []
    visited = dict()
    sr,sc = s
    min_score = 99999999
    solve(data,s,'E')

    visited=np.zeros(data.shape, dtype=int)
    ROWS,COLS = visited.shape

    result = np.count_nonzero(paths)

    print(result)

    answer = (45,64,545)
    if answer:
        assert(result in answer)


@timer
def main() -> None:

    sys.setrecursionlimit(10000)
    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
