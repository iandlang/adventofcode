import numpy as np
from decorators.timer import timer
from typing import List

def load_data(file:str) -> list[np.ndarray[str]]:

    with open(file) as f:
        return [np.array([list(row) for row in grid.splitlines()]) for grid in f.read().split("\n\n")]

def solve(data:List[np.ndarray[str]]) -> int:

    locks = [grid[1:].T for grid in data if np.all(grid[0] == "#")]
    keys = [grid[:-1].T for grid in data if np.all(grid[-1] == "#")]

    lock_pins = [[np.count_nonzero(col == "#") for col in lock] for lock in locks]
    key_pins = [[np.count_nonzero(col == "#") for col in key] for key in keys]

    result = sum(all(sum(t) <= 5 for t in zip(key, lock)) for lock in lock_pins for key in key_pins)

    return result
@timer
def main() -> None:

    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
