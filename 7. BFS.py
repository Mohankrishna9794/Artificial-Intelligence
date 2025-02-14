from collections import deque
def bfs(graph, start):
    """
    Simple BFS implementation. :param graph: Adjacency list:param start: Starting node """
    visited = set()
    queue = deque([start])
    result = []    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph.get(node, []))    
    return result
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
# Run BFS
start_node = input("Enter start node: ").strip()
if start_node in graph:
    print("BFS Order:", " -> ".join(bfs(graph, start_node)))
else:
    print("Invalid node.")
