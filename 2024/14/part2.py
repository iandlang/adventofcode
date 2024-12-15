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

    grid = np.zeros((ROWS,COLS), dtype=int)

    d=[]
    stdmin = 99999999

    for moves in range (101*103):

        for c,r,dc,dr in arr:
            r = (r + moves*dr) % ROWS
            c = (c + moves*dc) % COLS
            grid[r,c] += 1

        std = np.std(grid)
        if std < stdmin:
            stdmin = std
            result = moves
            d.append(grid.copy())

        grid.fill(0)

    print(d[-1])
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
