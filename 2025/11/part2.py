from decorators.timer import timer
from functools import lru_cache, reduce
from operator import mul
from itertools import pairwise

def load_data(file: str):

    with open(file) as f:
        return {
            line[0][:-1]: line[1:]
            for line in [line.split(" ") for line in f.read().splitlines()]
        }

def solve(network: dict[str, list[str]]) -> int:

    @lru_cache
    def path_count(node_from: str, node_to: str) -> int:
        if node_from == node_to:
            pass
            return 1

        if node_from not in network:
            pass
            return 0

        next_nodes = network[node_from]
        return sum(path_count(next_node, node_to) for next_node in next_nodes)

    return sum([
        reduce(mul,(path_count(f,t) for f,t in pairwise(["svr", "fft", "dac", "out"]))),
        reduce(mul,(path_count(f,t) for f,t in pairwise(["svr", "dac", "fft", "out"])))
    ])

@timer
def main() -> None:
    filename =  "data.txt"
    data = load_data(filename)
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()