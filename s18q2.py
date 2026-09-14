import heapq

ROOM_W = 10
ROOM_H = 10

objects = [
    (3, 2), (3, 2), (3, 2), (3, 2), (3, 2),
    (2, 2), (2, 2), (2, 2), (2, 2)
]


def can_place(placed, obj, x, y):
    w, h = obj

    if x + w > ROOM_W or y + h > ROOM_H:
        return False

    for px, py, pw, ph in placed:
        if not (x + w <= px or px + pw <= x or
                y + h <= py or py + ph <= y):
            return False

    return True


def heuristic(placed):
    if not placed:
        return 0

    max_x = max(x + w for x, y, w, h in placed)
    max_y = max(y + h for x, y, w, h in placed)

    return max_x * max_y


def a_star(objects):
    start = (0, 0, [])
    pq = [(0, 0, start)]
    visited = set()

    while pq:
        f, g, (_, _, placed) = heapq.heappop(pq)

        if len(placed) == len(objects):
            return placed

        state = tuple(placed)

        if state in visited:
            continue

        visited.add(state)

        obj = objects[len(placed)]
        w, h = obj

        # Only try a few meaningful positions
        positions = [(0, 0)]

        for x, y, pw, ph in placed:
            positions.extend([
                (x + pw, y),
                (x, y + ph)
            ])

        for x, y in positions:
            if can_place(placed, obj, x, y):

                new_placed = placed + [(x, y, w, h)]

                new_g = g + w * h
                new_h = heuristic(new_placed)
                new_f = new_g + new_h

                heapq.heappush(
                    pq,
                    (new_f, new_g, (0, 0, new_placed))
                )

    return None


solution = a_star(objects)

if solution:
    print("Optimal arrangement:")

    for i, (x, y, w, h) in enumerate(solution, 1):
        print(
            f"Object {i}: Position=({x}, {y}), "
            f"Size=({w}, {h})"
        )

    used_area = sum(w * h for x, y, w, h in solution)
    room_area = ROOM_W * ROOM_H
    unused_area = room_area - used_area

    print("\nRoom area:", room_area)
    print("Used area:", used_area)
    print("Unused area:", unused_area)

else:
    print("No solution found.")
