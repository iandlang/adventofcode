from decorators.timer import timer

def load_data(file: str) -> list[str]:
    with open(file) as f:
        return [line for line in f.read().splitlines() if line]

def parse_data(data: list[str]) -> tuple[list[list[int]], list[int]]:
    fresh = [list(map(int,line.split("-"))) for line in data if "-" in line]
    ids = [int(line) for line in data if "-" not in line]
    return fresh, ids

def is_fresh(id: int, fresh: list[list[int]]) -> bool:
    return any(id in range(f,t+1) for f,t in fresh)

def solve(data: list[str]) -> int:
    fresh, ids = parse_data(data)
    return sum(is_fresh(id, fresh) for id in ids)

@timer
def main() -> None:
    data = load_data("test.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()