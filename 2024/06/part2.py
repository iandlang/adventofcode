import numpy as np
import sys
from timeit import default_timer
from functools import wraps

def timeme(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        result = func(*args, **kwargs)
        end_time = default_timer()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper

def get_data(file:str) -> np.ndarray[str]:

    with open(file) as f:
        return np.array([list(line.strip()) for line in f])


def solve(data:np.ndarray[str]) -> np.ndarray[str]:

    loc = np.where(data == "^")
    r,c = loc[0][0],loc[1][0]

    data[r,c] = 'X'

    try:

        while True:

            arr = data[:r,c]
            i = np.where(arr == '#')[0][-1]
            arr[i+1:] = "X"
            r = i + 1

            arr = data[r,c+1:]
            i = np.where(arr == '#')[0][0]
            arr[:i] = "X"
            c += i

            arr = data[r+1:,c]
            i = np.where(arr == '#')[0][0]
            arr[:i] = "X"
            r += i

            arr = data[r,:c]
            i = np.where(arr == '#')[0][-1]
            arr[i+1:] = "X"
            c = i + 1

    except IndexError:

        arr[:] = "X"
        data[loc[0][0],loc[1][0]] = "^"
        return data


def compute(data:np.ndarray[str]) -> None:

    loc = np.where(data == "^")
    gr,gc = loc[0][0], loc[1][0]

    prev_cell = None
    result = 0

    it = np.nditer(data, flags=['multi_index'])
    for x in it:

        r,c = gr,gc
        cell = it.multi_index

        if data[cell] != "X":
            continue

        if prev_cell:
            data[prev_cell] = "X"

        data[cell] = '#'

        visited = {}

        try:
            while True:

                arr = data[:r,c]
                i = np.where(arr == '#')[0][-1]
                r = i + 1

                if tuple((r,c)) in visited:
                    result += 1
                    break
                visited[tuple((r,c))] = True

                arr = data[r,c+1:]
                i = np.where(arr == '#')[0][0]
                c += i

                arr = data[r+1:,c]
                i = np.where(arr == '#')[0][0]
                r += i

                arr = data[r,:c]
                i = np.where(arr == '#')[0][-1]
                c = i + 1

        except IndexError:
            pass

        finally:
            prev_cell = cell

    print(result)


@timeme
def main() -> None:

    data = get_data(sys.argv[1])
    data = solve(data)
    compute(data)


if __name__ == "__main__":
    main()
