import heapq


class PuzzleNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.cost = 0 if parent is None else parent.cost + 1

    def __lt__(self, other):
        return self.cost + self.heuristic() < other.cost + other.heuristic()

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(map(tuple, self.state)))

    def heuristic(self):
        h = 0

        for i in range(3):
            for j in range(3):
                value = self.state[i][j]

                if value != 0:
                    goal_i, goal_j = divmod(value - 1, 3)
                    h += abs(i - goal_i) + abs(j - goal_j)

        return h

    def get_possible_moves(self):
        moves = []

        i, j = next(
            (i, j)
            for i, row in enumerate(self.state)
            for j, value in enumerate(row)
            if value == 0
        )

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = i + di, j + dj

            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row.copy() for row in self.state]

                new_state[i][j], new_state[new_i][new_j] = \
                    new_state[new_i][new_j], new_state[i][j]

                moves.append(PuzzleNode(new_state, self))

        return moves


def a_star(initial_state):
    initial_node = PuzzleNode(initial_state)

    if initial_node.heuristic() == 0:
        return [initial_node.state]

    priority_queue = [initial_node]
    visited = set()

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node.heuristic() == 0:
            path = []

            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent

            return path[::-1]

        for neighbor in current_node.get_possible_moves():
            if neighbor not in visited:
                heapq.heappush(priority_queue, neighbor)

    return None


def print_solution(solution):
    for step, state in enumerate(solution, 1):
        print(f"Step {step}:")

        for row in state:
            print(row)

        print()


if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]
    ]

    solution = a_star(initial_state)

    if solution:
        print_solution(solution)
    else:
        print("No solution found.")
