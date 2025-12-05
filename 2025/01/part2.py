from decorators.timer import timer

def load_data(file: str) -> list[tuple[str, int]]:
    with open(file) as f:
        return [(line[0], int(line[1:])) for line in f.readlines()]

def solve(data: list[tuple[str, int]]) -> int:
    pos = 50
    zeros = 0
    delta = {"L": -1, "R": 1}
    for direction, clicks in data:
        zeros += clicks // 100
        for _ in range(clicks % 100):
            pos = (pos + delta[direction]) % 100
            zeros += pos == 0
    return zeros

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
