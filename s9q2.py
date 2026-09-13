from collections import deque


def get_next_states(state):
    x, y = state
    next_states = []

    if x < 5:
        next_states.append((5, y))

    if y < 7:
        next_states.append((x, 7))

    if x > 0:
        next_states.append((0, y))

    if y > 0:
        next_states.append((x, 0))

    if x > 0 and y < 7:
        pour = min(x, 7 - y)
        next_states.append((x - pour, y + pour))

    if y > 0 and x < 5:
        pour = min(y, 5 - x)
        next_states.append((x + pour, y - pour))

    return next_states


def bfs():
    start_state = (0, 0)
    target = 4

    queue = deque([(start_state, [])])
    visited = {start_state}

    while queue:
        (x, y), path = queue.popleft()

        if y == target:
            return path + [(x, y)]

        for next_state in get_next_states((x, y)):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(x, y)]))

    return None


def print_solution(path):
    if path:
        print("Steps to achieve 4 gallons in the 7-gallon jug:")

        for step in path:
            print(
                f"5-gallon jug: {step[0]} gallons, "
                f"7-gallon jug: {step[1]} gallons"
            )
    else:
        print("No solution found.")


solution = bfs()
print_solution(solution)
