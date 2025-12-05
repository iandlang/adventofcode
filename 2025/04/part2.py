from decorators.timer import timer

def load_data(file: str) -> list[list[bool]]:
    with open(file) as f:
        # bools are faster to process
        return [[c == '@' for c in line] for line in f.read().splitlines()]

def pad_data(data: list[list[bool]]) -> list[list[bool]]:
    # Add border of False to eliminate boundary checking
    width = len(data[0]) + 2
    padded = [[False] * width]
    for row in data:
        padded.append([False] + row + [False])
    padded.append([False] * width)
    return padded

def is_accessible(data: list[list[bool]], row: int, col: int) -> bool:
    count = 0
    delta = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    for dx, dy in delta:
        count += data[row + dx][col + dy]
        if count == 4:
            return False

    data[row][col] = False
    return True

def solve(data: list[list[bool]]) -> int:
    data = pad_data(data)
    gridsize = len(data)
    result = 0
    while (
        c := sum(
            is_accessible(data, row, col)
            for row in range(1, gridsize - 1)
            for col in range(1, gridsize - 1)
            if data[row][col]
        )
    ) > 0:
        result += c
    return result

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()