import numpy as np
import sys
from decorators.timer import timer
from typing import List


def get_data(file:str) -> List[int]:

    with open(file) as f:
        return [ int(c) for c in list(f.read().strip())]


def compute(data:List[int]) -> None:

    fs = []
    fn = 0
    while len(data) > 0:
        f, *data = data
        fs.append([fn,f])
        fn += 1

        if len(data) == 0:
            break

        f, *data = data
        fs.append([-1,f])

    for br in fs[::-1]:
        if br[0] == -1:
            continue
        for i,b in enumerate(fs):
            if b[0] == br[0]:
                break
            if b[0] == -1:
                if b[1] < br[1]:
                    b[0] = br[0]
                    br[1] -= b[1]
                    continue
                if b[1] == br[1]:
                    b[0] = br[0]
                    br[0] = -1
                    break
                if b[1] > br[1]:
                    fs[i][1] -= br[1]
                    fs.insert(i,br.copy())
                    br[0] = -1
                    break

    result = 0
    p = 0

    for b in fs:
        if b[0] == -1:
            p += b[1]
        else:
            result += b[0] * (p + (p + b[1] - 1)) * b[1] // 2
            p += b[1]

    print(result)

    answer = 6386640365805
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
