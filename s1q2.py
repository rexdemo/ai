import sys


def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print("Visited node:", start)

    if start == goal:
        sys.exit()

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, goal, visited)


graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
    5: [8],
    6: [8],
    7: [8],
    8: []
}


dfs(graph, 1, 8)
