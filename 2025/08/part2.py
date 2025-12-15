from decorators.timer import timer
import networkx as nx
import math
from itertools import combinations

def load_data(file: str) -> tuple[tuple[int, ...]]:
    with open(file) as f:
        return tuple(tuple(map(int, line.split(","))) for line in f.read().splitlines())

def solve(data: tuple[tuple[int, ...]]) -> int:

    node_distances = sorted(
        [(p1, p2, math.dist(p1, p2)) for p1, p2 in combinations(data, 2)],
        key=lambda x: x[2]
    )
    node_list = [(p1, p2) for p1, p2, _ in node_distances]

    G = nx.Graph()
    G.add_nodes_from(data)

    i = 0
    while (sz := nx.number_connected_components(G)) > 1:
        G.add_edges_from(node_list[i:i + sz - 1])
        i += sz - 1
    return node_list[i-1][0][0] * node_list[i-1][1][0]

@timer
def main() -> None:
    filename = "data.txt"
    data = load_data(filename)
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()