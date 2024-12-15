import numpy as np
import sys
from decorators.timer import timer


def get_data(file:str) -> np.ndarray[str]:


    with open(file) as f:
        grid,moves = f.read().split("\n\n")

    grid = np.array([list(line) for line in grid.splitlines()])
    moves = ' '.join(moves.splitlines())

    return grid,moves


def compute(grid:np.ndarray[str], moves:str) -> None:

    ROWS,COLS = grid.shape

    r,c = np.argwhere(grid == "@")[0]

    d = {
        '>':(0,1),
        '<':(0,-1),
        '^':(-1,0),
        'v':(1,0)
    }

    for move in moves:

        if move not in list('><^v'):
            # should really strip these out, they come from newlines in the data
            continue

        rd = d[move][0]
        cd = d[move][1]

        nr = r + rd
        nc = c + cd

        if grid[nr,nc] == "#":
            continue

        if grid[nr,nc] == ".":
            pass

        elif move == ">":
            fs = np.argwhere(grid[r,c:] == ".")
            bl = np.argwhere(grid[r,c:] == "#")
            if len(fs) == 0 or fs[0][0] > bl[0][0]:
                continue
            grid[r,c+fs[0][0]] = "O"

        elif move == "<":
            fs = np.argwhere(grid[r,:c] == ".")
            bl = np.argwhere(grid[r,:c] == "#")
            if len(fs) == 0 or fs[-1][0] < bl[-1][0]:
                continue
            grid[r,fs[-1][0]] = "O"

        elif move == "^":
            fs = np.argwhere(grid[:r,c] == ".")
            bl = np.argwhere(grid[:r,c] == "#")
            if len(fs) == 0 or fs[-1][0] < bl[-1][0]:
                continue
            grid[fs[-1][0],c] = "O"

        elif move == "v":
            fs = np.argwhere(grid[r:,c] == ".")
            bl = np.argwhere(grid[r:,c] == "#")
            if len(fs) == 0 or fs[0][0] > bl[0][0]:
                continue
            grid[r+fs[0][0],c] = "O"

        grid[r,c] = "."
        grid[nr,nc] = "@"
        r += rd
        c += cd

    ri, ci = np.where(grid == "O")
    result = np.sum(100 * ri + ci)

    print(result)

    answer = 1415498
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    grid,moves = get_data(sys.argv[1])
    compute(grid,moves)


if __name__ == "__main__":
    main()
