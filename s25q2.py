#explanation
'''Start state:

1 2 3
4 0 6
7 5 8

Moves:

down → 0 neeche jaata hai
right → 0 right jaata hai

Final:

1 2 3
4 5 6
7 8 0

Ye goal state hai, aur total 2 moves lage.

import heapq

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}'''


import heapq

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


def find_position(puzzle, value):
    for i, row in enumerate(puzzle):
        if value in row:
            return i, row.index(value)


def move_tile(puzzle, pos0, move):
    new_puzzle = [row[:] for row in puzzle]
    i, j = pos0
    di, dj = move
    ni, nj = i + di, j + dj

    if 0 <= ni < 3 and 0 <= nj < 3:
        new_puzzle[i][j], new_puzzle[ni][nj] = \
            new_puzzle[ni][nj], new_puzzle[i][j]
        return new_puzzle

    return None


def heuristic(puzzle):
    distance = 0

    for i in range(3):
        for j in range(3):
            value = puzzle[i][j]

            if value != 0:
                target_i, target_j = divmod(value - 1, 3)
                distance += abs(i - target_i) + abs(j - target_j)

    return distance


def a_star(start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, []))
    visited = {tuple(map(tuple, start))}

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)

        if current == goal_state:
            return path

        pos0 = find_position(current, 0)

        for move_name, move_delta in moves.items():
            new_state = move_tile(current, pos0, move_delta)

            if new_state:
                state = tuple(map(tuple, new_state))

                if state not in visited:
                    new_path = path + [move_name]
                    new_cost = len(new_path) + heuristic(new_state)

                    heapq.heappush(
                        priority_queue,
                        (new_cost, new_state, new_path)
                    )
                    visited.add(state)

    return None


def solve_puzzle(start_state):
    solution = a_star(start_state)

    if solution:
        print("Solution found! Moves to solve the puzzle:")

        for move in solution:
            print(move)

        print(f"Total moves: {len(solution)}")
    else:
        print("No solution found.")


start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]


if __name__ == "__main__":
    solve_puzzle(start_state)
