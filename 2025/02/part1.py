from decorators.timer import timer

def load_data(file: str) -> list[tuple[int, int]]:
    with open(file) as f:
        return [tuple(map(int, code.split("-"))) for line in f for code in line.strip().split(",")]

def solve(data: list[tuple[int, int]]) -> int:
    result = 0
    for f,t in data:
        i = f
        while i <= t:
            s = str(i)
            n = len(s)
            if n % 2 == 1:
                i = 10 ** n
                continue
            mp = n // 2
            smp1, smp2 = s[:mp], s[mp:]
            if smp1 < smp2:
                i = (int(smp1) + 1) * 10 ** mp + 1
                continue
            elif smp1 == smp2:
                result += i
                i = (int(smp1) + 1) * 10 ** mp + 1
                continue
            elif smp1 > smp2:
                i = int(smp1 * 2)
                continue
    return result

@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()