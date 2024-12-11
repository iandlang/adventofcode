from functools import cache
import numpy as np
import sys
from decorators.timer import timer


def get_data(file:str) -> np.ndarray[str]:

    with open(file) as f:
        return [int(c) for c in f.read().split()]


@cache
def split_stone(stone):

    stone = str(stone)
    mp = len(stone) // 2
    return int(stone[:mp]), int(stone[mp:])


def compute(data:np.ndarray[str]) -> None:

    data = {int(c):1 for c in data}

    for i in range(75):
        new_data = {}
        for stone, c in data.items():
            if stone == 0:
                new_stone = 1
                new_data[new_stone] = new_data.get(new_stone, 0) + c
            elif len(str(stone)) % 2 == 0:
                new_stone1, new_stone2 = split_stone(stone)
                new_data[new_stone1] = new_data.get(new_stone1, 0) + c
                new_data[new_stone2] = new_data.get(new_stone2, 0) + c
            else:
                new_stone = stone * 2024
                new_data[new_stone] = new_data.get(new_stone, 0) + c

        data = new_data

    result = sum(new_data.values())
    print(result)

    answer = 240954878211138
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
