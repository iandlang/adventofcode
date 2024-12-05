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

    bad_updates = []

    for update in updates:
        results = []

        for i, page in enumerate(update):
             results.extend([False for lp in update[i+1:] if lp in epm[page]] if page in epm else [])
             results.extend([False for ep in update[0:i] if ep in lpm[page]] if page in lpm else [])

        if not all(results):
            bad_updates.append(update)

    good_updates = []

    for update in bad_updates:
        good_update = []
        for page in update:
            inserted = False
            for i, good_page in enumerate(good_update):

                if page in epm and good_page in epm[page]:
                    continue

                if page in lpm and good_page in lpm[page]:
                    good_update.insert(i,page)
                    inserted = True
                    break

            if not inserted:
                good_update.append(page)

        good_updates.append(good_update)

    print(sum(([int(update[len(update)//2]) for update in good_updates])))


def main() -> None:

    epm, lpm, updates = get_data(sys.argv[1])
    compute(epm, lpm, updates)


if __name__ == "__main__":
    main()
