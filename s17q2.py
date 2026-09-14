import heapq


def a_star(graph, heuristic, start, goal):
    open_set = [(heuristic[start], 0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        f, cost, current = heapq.heappop(open_set)

        if current == goal:
            path = [current]

            while current in came_from:
                current = came_from[current]
                path.append(current)

            path.reverse()
            return path, g_score[goal]

        for neighbor, edge_cost in graph[current].items():
            new_cost = g_score[current] + edge_cost

            if new_cost < g_score[neighbor]:
                g_score[neighbor] = new_cost
                came_from[neighbor] = current

                f_score = new_cost + heuristic[neighbor]

                heapq.heappush(
                    open_set,
                    (f_score, new_cost, neighbor)
                )

    return None, float('inf')


graph = {
    'A': {'B': 9, 'C': 4, 'D': 7},
    'B': {'A': 9, 'E': 11},
    'C': {'A': 4, 'E': 17, 'F': 12},
    'D': {'A': 7, 'F': 14},
    'E': {'B': 11, 'C': 17, 'G': 5},
    'F': {'C': 12, 'D': 14, 'G': 9},
    'G': {'E': 5, 'F': 9}
}


heuristic = {
    'A': 21,
    'B': 14,
    'C': 18,
    'D': 18,
    'E': 5,
    'F': 8,
    'G': 0
}


start = 'A'
goal = 'G'

path, cost = a_star(graph, heuristic, start, goal)

if path:
    print("Shortest path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found.")
