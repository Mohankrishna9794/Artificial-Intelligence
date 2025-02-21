import heapq
def a_star(graph, start, goal, heuristic):
    """ A* Algorithm for shortest path."""
    open_list = [(heuristic[start], 0, start, [])]
    closed_set = set()   
    while open_list:
        _, cost, current, path = heapq.heappop(open_list)
        if current in closed_set:
            continue
        path.append(current)
        if current == goal:
            return path, cost
        closed_set.add(current)
        for neighbor, move_cost in graph[current].items():
            if neighbor not in closed_set:
                heapq.heappush(open_list, (cost + move_cost + heuristic[neighbor], cost + move_cost, neighbor, path[:]))
    return None, float('inf')
# Example graph with heuristic values
graph = {
    'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'D': 2, 'E': 5}, 'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'G': 2}, 'E': {'B': 5, 'H': 3}, 'F': {'C': 3, 'H': 2},
    'G': {'D': 2, 'H': 1}, 'H': {'E': 3, 'F': 2, 'G': 1}
}
heuristic = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3, 'F': 2, 'G': 1, 'H': 0}
# User input
start, goal = input("Start node: ").strip().upper(), input("Goal node: ").strip().upper()
if start in graph and goal in graph:
    path, cost = a_star(graph, start, goal, heuristic)
    print(f"Path: {' -> '.join(path) if path else 'No path found'}")
    print(f"Cost: {cost if path else 'N/A'}")
else:
    print("Invalid input.")
