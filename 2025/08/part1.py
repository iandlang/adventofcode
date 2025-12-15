from decorators.timer import timer
import networkx as nx
import math
from itertools import combinations


def load_data(file: str) -> tuple[tuple[int, ...]]:
    with open(file) as f:
        return tuple(tuple(map(int, line.split(","))) for line in f.read().splitlines())

def solve(data: tuple[tuple[int, ...]], max_edges: int) -> int:

    node_distances = sorted(
        [(p1, p2, math.dist(p1, p2)) for p1, p2 in combinations(data, 2)],
        key=lambda x: x[2]
    )
    node_list = [(p1, p2) for p1, p2, _ in node_distances]

    G = nx.Graph()
    G.add_edges_from(node_list[:max_edges])
    sizes = sorted((len(cc) for cc in nx.connected_components(G)), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

@timer
def main() -> None:
    import sys
    filename = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    max_edges = 10 if filename == "test.txt" else 1000
    data = load_data(filename)
    result = solve(data, max_edges)
    print(f"result: {result}")

if __name__ == "__main__":
    main()