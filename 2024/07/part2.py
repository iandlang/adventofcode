from decorators.timer import timer


def load_data(file: str) -> list[dict[int, list[int]]]:
    data = []
    with open(file) as f:
        for line in f:
            parts = line.strip().split(":")
            data.append({int(parts[0]): [int(x) for x in parts[1].split()]})
    return data


def solve(data: list[dict[int, list[int]]]) -> int:
    def solve_equation(current: int, target: int, arr: list[int], ops: list[str]) -> bool:
        if current > target:
            return False
        elif arr == []:
            if current == target:
                return True
            else:
                return False
        else:
            if solve_equation(current * arr[0], target, arr[1:], ops + ['*', str(arr[0])]):
                return True
            elif solve_equation(current + arr[0], target, arr[1:], ops + ['+', str(arr[0])]):
                return True
            elif solve_equation(int(str(current) + str(arr[0])), target, arr[1:], ops + ['||', str(arr[0])]):
                return True
            else:
                return False

    result = 0
    for d in data:
        for target, arr in d.items():
            result += target * solve_equation(current=arr[0], target=target, arr=arr[1:], ops=[str(arr[0])])
    return result


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
