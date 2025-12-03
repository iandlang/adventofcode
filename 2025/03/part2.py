from decorators.timer import timer

def load_data(file: str) -> list[str]:
    with open(file) as f:
        return f.read().splitlines()

def get_max_value(line: str, depth: int, end: int) -> str:
    mv = max(line[:end])

    if depth == 12:
        return mv
    if end == 1:
        return line

    mvi = line.index(mv)
    return mv + get_max_value(line[mvi+1:], depth + 1, end - mvi)

def solve(data: list[str]) -> int:
    return sum(int(get_max_value(line, 1, len(line)-12 + 1)) for line in data)

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()