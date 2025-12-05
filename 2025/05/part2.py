from decorators.timer import timer

def load_data(file: str) -> list[list[int]]:
    with open(file) as f:
        return sorted(
            [int(x) for x in line.split("-")]
            for line in f.read().splitlines()
            if "-" in line
        )

def combine_ranges(fresh: list[list[int]]) -> list[list[int]]:
    if len(fresh) == 1:
        return fresh
    if fresh[0][1] >= fresh[1][0] - 1:
        return combine_ranges([[fresh[0][0], max(fresh[0][1], fresh[1][1])]] + fresh[2:])
    else:
        return [fresh[0]] + combine_ranges(fresh[1:])

def solve(data: list[list[int]]) -> int:
    return sum(t - f + 1 for f, t in combine_ranges(data))

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()