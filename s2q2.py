# Graph represented as an adjacency list
graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [5, 6],
    5: [7],
    6: [7],
    7: []
}


# Function to perform DFS
def depth_first_search(graph, start, goal):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node == goal:
            print(f"Goal node {goal} found!")
            return True

        if node not in visited:
            print(f"Visiting node {node}")
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    print("Goal node not found.")
    return False


# Run DFS
initial_node = 1
goal_node = 7

depth_first_search(graph, initial_node, goal_node)
