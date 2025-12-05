import numpy as np
import re
from decorators.timer import timer
from typing import List

def load_data(file:str) -> List[List[int]]:

    with open(file) as f:
        return [list(map(int,re.findall(r'-{0,1}\d+',line))) for line in f.readlines()]

def solve(arr:List[List[int]]) -> int:

    ROWS=103
    COLS=101

    grid = np.zeros(shape=(ROWS,COLS), dtype=int)

    for c,r,dc,dr in arr:
        r = (r + 100*dr) % ROWS
        c = (c + 100*dc) % COLS
        grid[r,c] += 1

    quad1 = grid[:ROWS//2,:COLS//2]
    quad2 = grid[:ROWS//2,COLS//2+1:]
    quad3 = grid[ROWS//2+1:,:COLS//2]
    quad4 = grid[ROWS//2+1:,COLS//2+1:]

    result = np.sum(quad1) * np.sum(quad2) * np.sum(quad3) * np.sum(quad4)

    return result
@timer
def main() -> None:

    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
