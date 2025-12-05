def load_data(file: str) -> list[list[int]]:
    with open(file) as f:
        return [[int(x) for x in line.split()] for line in f]


def compute(data: list[list[int]]) -> int:
    return sum(max(line) - min(line) for line in data)

if __name__ == "__main__":
    data = load_data("data.txt")
    result = compute(data)
    print(result)