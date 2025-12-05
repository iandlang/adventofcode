from decorators.timer import timer


def load_data(file: str) -> tuple[dict[str, list[str]], dict[str, list[str]], list[list[str]]]:
    epm = {}
    lpm = {}
    updates = []
    with open(file) as f:
        for line in [line.strip() for line in f]:
            if "|" in line:
                ep, lp = line.split("|")
                epm[lp] = epm.get(lp, []) + [ep]
                lpm[ep] = lpm.get(ep, []) + [lp]
            if "," in line:
                updates.append(line.split(","))
    return epm, lpm, updates


def solve(data: tuple[dict[str, list[str]], dict[str, list[str]], list[list[str]]]) -> int:
    epm, lpm, updates = data
    good_updates = []
    for update in updates:
        results = []
        for i, page in enumerate(update):
            results.extend([False for lp in update[i + 1:] if lp in epm[page]] if page in epm else [])
            results.extend([False for ep in update[0:i] if ep in lpm[page]] if page in lpm else [])
        if all(results):
            good_updates.append(update)
    return sum([int(update[len(update) // 2]) for update in good_updates])


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
