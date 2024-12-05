import sys
from typing import List


def get_data(file:str) -> List[str]:

    with open(sys.argv[1]) as f:
        return list(f.readline().strip())


def compute(data:List[int]) -> None:

    xmap = {'^':0,'>':1,'v':0,'<':-1}
    ymap = {'^':1,'>':0,'v':-1,'<':0}

    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    d = {}
    house = (x1,y1)
    d[house] = 2

    for i in range(0,len(data),2):
        x1 += xmap[data[i]]
        y1 += ymap[data[i]]
        house = (x1,y1)
        if house in d:
            d[house] += 1
        else:
            d[house] = 1

    for i in range(1,len(data),2):
        x2 += xmap[data[i]]
        y2 += ymap[data[i]]
        house = (x2,y2)
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
