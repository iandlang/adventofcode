from decorators.timer import timer


def load_data(file: str) -> list[list[int]]:
    with open(file) as f:
        return [[int(x) for x in line.strip().split(" ")] for line in f]


def solve(data: list[list[int]]) -> int:
    result = 0
    for orig_line in data:
        for i in range(len(orig_line)):
            line = orig_line.copy()
            line.pop(i)
            tuples = list(zip(line, line[1:]))
            diffs = [abs(b - a) for a, b in tuples]
            signs = [b > a for a, b in tuples]
            if min(diffs) > 0 and max(diffs) < 4 and len(set(signs)) == 1:
                result += 1
                break
    return result


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
