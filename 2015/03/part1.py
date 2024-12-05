import sys
from typing import List


def get_data(file:str) -> List[str]:

    with open(sys.argv[1]) as f:
        return list(f.readline().strip())


def compute(data:List[int]) -> None:

    xmap = {'^':0,'>':1,'v':0,'<':-1}
    ymap = {'^':1,'>':0,'v':-1,'<':0}

    x = 0
    y = 0
    d = {}
    house = (x,y)
    d[house] = 1

    for move in data:
        x += xmap[move]
        y += ymap[move]
        house = (x,y)
        if house in d:
            d[house] += 1
        else:
            d[house] = 1

    print(len(d.keys()))


def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
