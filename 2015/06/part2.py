import numpy as np
import re
import sys
from typing import List


def get_data(file:str) -> List[str]:

    with open(file) as f:
        return [line.strip() for line in f.readlines()]


def compute(data:List[str]) -> None:

    grid = np.zeros((1000, 1000), dtype=int)

    pattern = r'(turn off|turn on|toggle) (\d+),(\d+) through (\d+),(\d+)'

    for line in data:
        for matches in re.finditer(pattern, line):
            match = list(matches.groups())
            action = match.pop(0)
            (r0,c0,r1,c1) = list(map(int, match))
            r1 += 1
            c1 += 1

            if action == 'turn on':
                grid[r0:r1,c0:c1] += 1
            elif action == 'turn off':
                grid[r0:r1,c0:c1][grid[r0:r1,c0:c1] > 0] -= 1
            elif action == 'toggle':
                grid[r0:r1,c0:c1] += 2

    print(np.sum(grid))


def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
