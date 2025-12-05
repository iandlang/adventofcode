from decorators.timer import timer

BATTERY_COUNT = 12

def load_data(file: str) -> list[str]:
    with open(file) as f: return f.read().splitlines()

def get_max_value(line: str, window: int, depth: int = 1) -> str:
    if window == 1: return line

    mvi = line.index(mv := max(line[:window]))
    return mv if depth == BATTERY_COUNT else mv + get_max_value(line[mvi+1:], window - mvi, depth + 1)

def solve(data: list[str]) -> int:
    return sum(int(get_max_value(line, window = len(line) - BATTERY_COUNT + 1)) for line in data)

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()