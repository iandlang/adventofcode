from decorators.timer import timer

def load_data(file: str) -> list[tuple[str, int]]:
    with open(file) as f:
        return [(line[0], int(line[1:])) for line in map(str.strip, f)]

def solve(data: list[tuple[str, int]]) -> int:
    pos = 50
    zeros = 0
    delta = {"L": -1, "R": 1}
    for direction, clicks in data:
        newpos = (pos + clicks * delta[direction]) % 100
        if (pos != 0) and (newpos != 0):
            zeros += (newpos > pos) if direction == "L" else (newpos < pos)
        zeros += clicks // 100
        zeros += newpos == 0
        pos = newpos
    return zeros

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()