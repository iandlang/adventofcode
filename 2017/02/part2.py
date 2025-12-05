from itertools import combinations

def load_data(file: str) -> list[list[int]]:
    with open(file) as f:
        return [sorted([int(x) for x in line.split()]) for line in f]


def compute(data: list[list[int]]) -> int:
    return sum(
        b // a
        for line in data
        for a, b in combinations(line, 2)
        if b % a == 0
    )


if __name__ == "__main__":
    data = load_data("data.txt")
    result = compute(data)
    print(result)