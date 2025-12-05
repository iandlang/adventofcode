import networkx as nx
from pprint import pprint as pp
from decorators.timer import timer
from typing import List

def load_data(file:str) -> List[List[str]]:

    with open(file) as f:
        return [line.strip().split("-") for line in f]

def solve(data:List[List[str]]) -> str:

    G = nx.Graph()
    G.add_edges_from(data)
    cliques = sorted(nx.find_cliques(G), key = lambda x:len(x))
    result = ",".join(sorted(cliques[-1]))

    return result


@timer
def main() -> None:

    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
