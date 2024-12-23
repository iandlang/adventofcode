import networkx as nx
import sys
from decorators.timer import timer
from typing import List


def get_data(file:str) -> List[List[str]]:

     with open(file) as f:
         return [line.strip().split("-") for line in f]


def compute(edges:List[List[str]]) -> None:

    G = nx.Graph()
    G.add_edges_from(edges)
    result = sum(1 for cycle in nx.simple_cycles(G, 3) if any(node.startswith("t") for node in cycle))

    print(result)

    answer = 1098
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
