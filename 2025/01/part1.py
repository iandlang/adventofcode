from decorators.timer import timer

def load_data(file: str) -> list[int]:
    with open(file) as f:
        return [int(line[1:]) * (1 if line[0] == "R" else -1) for line in f.read().splitlines()]

def solve(data: list[int]) -> int:
    pos = 50
    return sum((pos := (pos + clicks) % 100) == 0 for clicks in data)

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()