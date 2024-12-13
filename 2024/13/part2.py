import numpy as np
import re
import sys
from decorators.timer import timer
from typing import List

def get_data(file:str) -> List[List[int]]:

    with open(file) as f:
        return [list(map(int,re.findall(r'\d+',line))) for line in f.read().split("\n\n")]


def compute(machines:List[List[int]]) -> None:

    result = 0

    for ax,ay,bx,by,px,py in machines:

        px += 10000000000000
        py += 10000000000000

        '''
        a(ax) + b(bx) = px
        a(ay) + b(by) = py

        solve for a and b, and check both are integers
        '''

        a = (px*by-py*bx)/(ax*by-bx*ay)
        b = (px*ay-py*ax)/(bx*ay-ax*by)

        if a.is_integer() and b.is_integer():
            result += int(3*a + b)

    print(result)

    answer = 92827349540204
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
