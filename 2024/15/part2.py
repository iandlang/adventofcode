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

    def add2move(r,c,d):

        if grid[r,c] == "#":
            return False
        elif grid[r,c] == ".":
            return True
        elif [r,c] not in cells2move:
            cells2move.append([r,c])
            if grid[r,c] == '[':
                return add2move(r,c+1,d) and add2move(r+d,c,d)
            elif grid[r,c] == ']':
                return add2move(r,c-1,d) and add2move(r+d,c,d)
        else:
            return True

    ROWS,COLS = grid.shape

    grid2=np.empty((ROWS,COLS*2), dtype=str)

    for r in range(ROWS):
        for c in range(COLS):
            cell = grid[r,c]
            if cell == "#":
                grid2[r,2*c] = "#"
                grid2[r,2*c+1] = "#"
            elif cell == ".":
                grid2[r,2*c] = "."
                grid2[r,2*c+1] = "."
            elif cell == "O":
                grid2[r,2*c] = "["
                grid2[r,2*c+1] = "]"
            elif cell == "@":
                grid2[r,2*c] = "@"
                grid2[r,2*c+1] = "."

    grid = grid2.copy()

    r,c = np.argwhere(grid == "@")[0]

    d = {
       '>':(0,1),
       '<':(0,-1),
       '^':(-1,0),
       'v':(1,0)
     }

    for m, move in enumerate(moves):

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
            i = fs[0][0]
            grid[r,c+2:c+i+1] = grid[r,c+1:c+i].copy()

        elif move == "<":
            fs = np.argwhere(grid[r,:c] == ".")
            bl = np.argwhere(grid[r,:c] == "#")
            if len(fs) == 0 or fs[-1][0] < bl[-1][0]:
                continue
            i = fs[-1][0]
            grid[r,i:c-1] = grid[r,i+1:c].copy()

        elif move == "^":
            cells2move = [[r,c]]
            can_move = add2move(r-1,c,-1)

            if can_move:
                for cell in sorted(cells2move):
                    rm,cm = cell
                    grid[rm-1,cm] = grid[rm,cm].copy()
                    if grid[rm,cm] not in cells2move:
                        grid[rm,cm] = "."
            else:
                continue

        elif move == "v":
            cells2move = [[r,c]]
            can_move = add2move(r+1,c,1)

            if can_move:
                for cell in sorted(cells2move)[::-1]:
                    rm,cm = cell
                    grid[rm+1,cm] = grid[rm,cm].copy()
                    if grid[rm,cm] not in cells2move:
                        grid[rm,cm] = "."
            else:
                continue

        grid[r,c] = "."
        grid[nr,nc] = "@"
        r += rd
        c += cd

    ri, ci = np.where(grid == "[")
    result = np.sum(100 * ri + ci)

    print(result)

    answer = 1432898
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    grid,moves = get_data(sys.argv[1])
    compute(grid,moves)


if __name__ == "__main__":
    main()
