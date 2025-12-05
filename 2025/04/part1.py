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
    delta = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    return sum(data[row + dx][col + dy] for dx, dy in delta) < 4

def solve(data: list[list[bool]]) -> int:
    data = pad_data(data)
    gridsize = len(data)
    return sum(
        is_accessible(data, row, col)
        for row in range(1, gridsize - 1)
        for col in range(1, gridsize - 1)
        if data[row][col]
    )

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()