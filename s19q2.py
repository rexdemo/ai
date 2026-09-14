import heapq


def heuristic(node):
    h = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'F': 0
    }
    return h[node]


def a_star_search(graph, start, goal):
    open_set = [(heuristic(start), start)]
    came_from = {}

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = [current]

            while current in came_from:
                current = came_from[current]
                path.append(current)

            path.reverse()
            return path, g_score[goal]

        for neighbor, cost in graph[current].items():
            new_cost = g_score[current] + cost

            if new_cost < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = new_cost

                f_score = new_cost + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, neighbor))

    return None, float('inf')


graph = {
    'A': {'B': 2, 'E': 3},
    'B': {'C': 1, 'F': 9},
    'C': {},
    'D': {'F': 1},
    'E': {'D': 6},
    'F': {}
}

start = 'A'
goal = 'F'

path, cost = a_star_search(graph, start, goal)

if path:
    print("Shortest path:", path)
    print("Total cost:", cost)
else:
    print("No path found.")
