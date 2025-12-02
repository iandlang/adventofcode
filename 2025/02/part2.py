from decorators.timer import timer
from textwrap import wrap

def load_data(file: str) -> list[list[str]]:
    with open(file) as f:
        return [code.split("-") for line in f for code in line.strip().split(",")]

def solve(data: list[list[str]]) -> int:
    result = 0
    for (f,t) in data:
        for i in range(int(f), int(t) + 1):
            for x in range(1, len(str(i)) // 2 + 1)[::-1]:
                if len(set(wrap(str(i),x))) == 1:
                    result += i
                    break
    return result

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()