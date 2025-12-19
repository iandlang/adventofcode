from decorators.timer import timer
from functools import cache
from math import prod
from itertools import pairwise

Node = str
Network = dict[Node, list[Node]]

def load_data(file: str) -> Network:
    with open(file) as f:
        return {nodes[0][:-1]: nodes[1:] for nodes in [line.split(" ") for line in f.read().splitlines()]}

def solve(network: Network) -> int:

    @cache
    def path_count(node_from: Node, node_to: Node) -> int:
        if node_from == node_to:
            return 1
        if node_from not in network:
            return 0
        return sum(path_count(next_node, node_to) for next_node in network[node_from])

    paths = [
        ["svr", "fft", "dac", "out"],
        ["svr", "dac", "fft", "out"]
    ]
    return sum(prod(path_count(node_from, node_to) for node_from, node_to in pairwise(path)) for path in paths)

@timer
def main() -> None:
    filename =  "data.txt"
    data = load_data(filename)
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()