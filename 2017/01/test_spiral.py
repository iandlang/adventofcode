def spiral_coords(n: int) -> tuple[int, int]:
    if n == 1:
        return (0, 0)

    x, y = 0, 0
    current = 1
    steps = 1

    # Directions: right, up, left, down
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    direction = 0

    while current < n:
        for _ in range(2):  # Two directions per step size
            for _ in range(steps):
                if current >= n:
                    return (x, y)
                x += dx[direction]
                y += dy[direction]
                current += 1
            direction = (direction + 1) % 4
        steps += 1

    return (x, y)

# Test with some known values from the spiral
test_cases = [
    (1, (0, 0)),
    (2, (1, 0)),
    (3, (1, 1)),
    (12, (2, 1)),
    (23, (0, -2)),
]

print("Testing known values:")
for n, expected in test_cases:
    coords = spiral_coords(n)
    print(f"n={n}: {coords}, expected {expected}, {'✓' if coords == expected else '✗'}")

print("\nTesting n=1024:")
coords = spiral_coords(1024)
manhattan = abs(coords[0]) + abs(coords[1])
print(f"1024 is at {coords}, Manhattan distance: {manhattan}")
print(f"Expected Manhattan distance: 31, {'✓' if manhattan == 31 else '✗'}")
