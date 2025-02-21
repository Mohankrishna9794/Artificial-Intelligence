def map_coloring(nodes, colors, constraints, color_map={}):
    """Simple function to solve map coloring using backtracking."""
    if len(color_map) == len(nodes):
        return color_map    
    node = next(n for n in nodes if n not in color_map)
    for color in colors:
        if all(color_map.get(neigh) != color for neigh in constraints[node]):
            color_map[node] = color
            result = map_coloring(nodes, colors, constraints, color_map)
            if result:
                return result
            del color_map[node]  # Backtrack  
    return None
# Example usage
nodes = ["A", "B", "C", "D"]
colors = ["Red", "Green", "Blue"]
constraints = {
    "A": ["B", "C"], "B": ["A", "C", "D"],
    "C": ["A", "B", "D"], "D": ["B", "C"]
}
solution = map_coloring(nodes, colors, constraints)
print("Color assignment:", solution if solution else "No valid coloring found.")
