from __future__ import annotations

def load_data(file: str) -> tuple[int, ...]:
    with open(file) as f:
        return tuple(int(digit) for digit in f.read().strip())

def compute(data: tuple[int, ...]) -> int:
    offset = 1
    return sum(a for i, a in enumerate(data) if a == data[(i + offset) % len(data)])

if __name__ == "__main__":
    data = load_data("data.txt")
    result = compute(data)
    print(result)