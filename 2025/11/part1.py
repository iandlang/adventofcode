from decorators.timer import timer

def load_data(file: str):

    with open(file) as f:
        return {
            line[0][:-1]: line[1:]
            for line in [line.split(" ") for line in f.read().splitlines()]
        }

def solve(network: dict[str, list[str]]) -> int:

    def get_paths(node_from: str, node_to: str) -> list[list[str]]:
        if node_from == node_to:
            return [[node_from]]

        return [
            [node_from] + path
            for node in network[node_from]
            for path in get_paths(node, node_to)
        ]

    return len(get_paths("you", "out"))

@timer
def main() -> None:
    filename =  "data.txt"
    data = load_data(filename)
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()