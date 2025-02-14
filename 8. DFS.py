def dfs(graph, start, visited=set()):
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}
# Run DFS
start_node = input("Enter start node: ").strip()
if start_node in graph:
    print("DFS Traversal Order:", end=' ')
    dfs(graph, start_node)
else:
    print("Invalid node.")
