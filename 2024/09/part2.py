from decorators.timer import timer


def load_data(file: str) -> list[int]:
    with open(file) as f:
        return [int(c) for c in list(f.read().strip())]


def solve(data: list[int]) -> int:
    fs = []
    fn = 0
    while len(data) > 0:
        f, *data = data
        fs.append([fn, f])
        fn += 1

        if len(data) == 0:
            break

        f, *data = data
        fs.append([-1, f])

    for br in fs[::-1]:
        if br[0] == -1:
            continue
        for i, b in enumerate(fs):
            if b[0] == br[0]:
                break
            if b[0] == -1:
                if b[1] < br[1]:
                    continue
                if b[1] == br[1]:
                    b[0] = br[0]
                    br[0] = -1
                    break
                if b[1] > br[1]:
                    fs[i][1] -= br[1]
                    fs.insert(i, br.copy())
                    br[0] = -1
                    break

    result = 0
    p = 0

    for b in fs:
        if b[0] == -1:
            p += b[1]
        else:
            result += b[0] * (p + (p + b[1] - 1)) * b[1] // 2
            p += b[1]

    return result


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
