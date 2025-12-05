import networkx as nx
from decorators.timer import timer
from typing import List

def load_data(file:str) -> List[List[str]]:

     with open(file) as f:
         return [line.strip().split("-") for line in f]

def solve(edges:List[List[str]]) -> int:

    G = nx.Graph()
    G.add_edges_from(edges)
    result = sum(1 for cycle in nx.simple_cycles(G, 3) if any(node.startswith("t") for node in cycle))

    return result


@timer
def main() -> None:

    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
