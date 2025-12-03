from decorators.timer import timer

def load_data(file: str) -> list[str]:
    with open(file) as f:
        return f.read().splitlines()

def get_max_value(line: str) -> int:
    mvi = line.index(mv := max(line[:-1]))
    return int(mv) * 10 + int(max(line[mvi+1:]))

def solve(data: list[str]) -> int:
    return sum(get_max_value(line) for line in data)

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()