import networkx as nx
from pprint import pprint as pp
import sys
from decorators.timer import timer
from typing import List


def get_data(file:str) -> List[List[str]]:

    with open(file) as f:
        return [line.strip().split("-") for line in f]


def compute(data:List[List[str]]) -> None:

    G = nx.Graph()
    G.add_edges_from(data)
    cliques = sorted(nx.find_cliques(G), key = lambda x:len(x))
    result = ",".join(sorted(cliques[-1]))

    print(result)

    answer = 'ar,ep,ih,ju,jx,le,ol,pk,pm,pp,xf,yu,zg'
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
