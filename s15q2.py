def depth_limited_dfs(graph, node, goal, depth, path):
    path.append(node)

    if node == goal:
        return True

    if depth == 0:
        path.pop()
        return False

    for child in graph[node]:
        if depth_limited_dfs(graph, child, goal, depth - 1, path):
            return True

    path.pop()
    return False


def iterative_deepening_dfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        path = []

        if depth_limited_dfs(graph, start, goal, depth, path):
            return path

    return None


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H', 'I'],
        'E': [],
        'F': ['K'],
        'G': [],
        'H': [],
        'I': [],
        'K': []
    }

    start = 'A'
    goal = 'G'
    max_depth = 5

    result = iterative_deepening_dfs(
        graph, start, goal, max_depth
    )

    if result:
        print("Goal node found:", goal)
        print("Path:", " -> ".join(result))
    else:
        print("Goal node not found.")
