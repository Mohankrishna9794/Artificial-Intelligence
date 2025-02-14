from itertools import permutations
def tsp(graph, start):
    cities = list(graph.keys())
    cities.remove(start)
    best_path, min_cost = [], float('inf')    
    for perm in permutations(cities):
        current_path = [start] + list(perm) + [start]
        current_cost = sum(graph[current_path[i]][current_path[i + 1]] for i in range(len(current_path) - 1))        
        if current_cost < min_cost:
            min_cost, best_path = current_cost, current_path    
    return best_path, min_cost
# Example distance graph
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
# Input start city
start_city = input("Enter the starting city (A/B/C/D): ").strip().upper()
# Run TSP solver
if start_city in graph:
    path, cost = tsp(graph, start_city)
    print("Optimal Path:", " -> ".join(path))
    print("Minimum Cost:", cost)
else:
    print("Invalid city. Please enter a valid city from the graph.")
