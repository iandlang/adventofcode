import numpy as np
import re
import sys
from decorators.timer import timer
from typing import List

def get_data(file:str) -> List[List[int]]:

    with open(file) as f:
        return [list(map(int,re.findall(r'-{0,1}\d+',line))) for line in f.readlines()]


def compute(arr:List[List[int]]) -> None:

    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(linewidth=np.inf)

    ROWS=103
    COLS=101

    # assume there will be a bock of robots in the final picture, as we are not told anything else
    # increment this manually from 2 until we get a hit on the final grid
    sp= 3
    search_pattern = np.full((sp,sp), '#')

    grid = np.full((ROWS,COLS), ".")

    moves = 0
    solved = False

    while not solved:
        moves += 1
        for c,r,dc,dr in arr:
            r = (r + moves*dr) % ROWS
            c = (c + moves*dc) % COLS
            grid[r,c] = '#'

        for i in range(ROWS*COLS):
            r = i // ROWS
            c = i % COLS

            if grid[r,c] == ".":
                continue

            if r > ROWS - sp or c > COLS - sp:
                continue

            if np.all(search_pattern == grid[r:r+sp,c:c+sp]):
                solved = True
                for line in grid:
                    print(''.join(line))
                break
        grid.fill('.')

    result = moves
    print(result)

    answer = 6577
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
