import numpy as np
from decorators.timer import timer


def load_data(file: str) -> np.ndarray:
    with open(file) as f:
        return np.array([list(line.strip()) for line in f])


def solve_part1(data: np.ndarray) -> np.ndarray:
    loc = np.where(data == "^")
    r, c = loc[0][0], loc[1][0]
    data[r, c] = 'X'
    try:
        while True:
            arr = data[:r, c]
            i = np.where(arr == '#')[0][-1]
            arr[i + 1:] = "X"
            r = i + 1

            arr = data[r, c + 1:]
            i = np.where(arr == '#')[0][0]
            arr[:i] = "X"
            c += i

            arr = data[r + 1:, c]
            i = np.where(arr == '#')[0][0]
            arr[:i] = "X"
            r += i

            arr = data[r, :c]
            i = np.where(arr == '#')[0][-1]
            arr[i + 1:] = "X"
            c = i + 1
    except IndexError:
        arr[:] = "X"
        data[loc[0][0], loc[1][0]] = "^"
        return data


def solve(data: np.ndarray) -> int:
    data = solve_part1(data)
    loc = np.where(data == "^")
    gr, gc = loc[0][0], loc[1][0]
    prev_cell = None
    result = 0

    it = np.nditer(data, flags=['multi_index'])
    for x in it:
        r, c = gr, gc
        cell = it.multi_index

        if data[cell] != "X":
            continue

        if prev_cell:
            data[prev_cell] = "X"

        data[cell] = '#'
        visited = {}

        try:
            while True:
                arr = data[:r, c]
                i = np.where(arr == '#')[0][-1]
                r = i + 1

                if tuple((r, c)) in visited:
                    result += 1
                    break
                visited[tuple((r, c))] = True

                arr = data[r, c + 1:]
                i = np.where(arr == '#')[0][0]
                c += i

                arr = data[r + 1:, c]
                i = np.where(arr == '#')[0][0]
                r += i

                arr = data[r, :c]
                i = np.where(arr == '#')[0][-1]
                c = i + 1
        except IndexError:
            pass
        finally:
            prev_cell = cell

    return result


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
