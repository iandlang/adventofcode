from decorators.timer import timer

def load_data(file: str) -> list[list[str]]:
    with open(file) as f:
        return [list(line) for line in f.read().splitlines()]

def solve(data: list[list[str]]) -> int:
    result = 0

    data[1][data[0].index("S")] = "|"
    for row in range(3, len(data), 2):
        for col in range(len(data[row])):
            if data[row - 2][col] == "|":
                if data[row - 1][col] == "^":
                    data[row][col - 1] = "|"
                    data[row][col + 1] = "|"
                    result += 1
                else:
                    data[row][col] = data[row - 2][col]

    return result

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()