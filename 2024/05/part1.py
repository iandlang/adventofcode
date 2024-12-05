import sys
from typing import List, Dict, Tuple

def get_data(file:str) -> Tuple[Dict[str, List[str]], Dict[str, List[str]], List[List[str]]]:

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


def compute(epm:Dict[str, List[str]], lpm:Dict[str, List[str]], updates:List[List[str]]) -> None:

    good_updates = []

    for update in updates:
        results = []
        for i, page in enumerate(update):
            results.extend([False for lp in update[i+1:] if lp in epm[page]] if page in epm else [])
            results.extend([False for ep in update[0:i] if ep in lpm[page]] if page in lpm else [])

        if all(results):
            good_updates.append(update)

    print(sum(([int(update[len(update)//2]) for update in good_updates])))


def main() -> None:

    epm, lpm, updates = get_data(sys.argv[1])
    compute(epm, lpm, updates)


if __name__ == "__main__":
    main()
