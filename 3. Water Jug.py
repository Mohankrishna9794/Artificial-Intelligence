from collections import deque
def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    # BFS queue: stores (jug1 state, jug2 state, path taken)
    queue = deque([(0, 0, [])])
    visited = set()
    while queue:
        jug1, jug2, path = queue.popleft()
        if (jug1, jug2) in visited:
            continue        
        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]        
        # If we reach the target, return the path
        if jug1 == target or jug2 == target:
            path.append((0, jug2))  # Ensure Jug1 is emptied at the end
            return path        
        # Possible next states
        next_states = set([
            (jug1_capacity, jug2),  # Fill Jug1
            (jug1, jug2_capacity),  # Fill Jug2
            (0, jug2),              # Empty Jug1
            (jug1, 0),              # Empty Jug2
            # Pour Jug1 -> Jug2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
            # Pour Jug2 -> Jug1
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))
        ])        
        for state in next_states:
            queue.append((*state, path))    
    return None  # No solution found
# Example usage
jug1_capacity = int(input("Enter capacity of Jug 1: "))
jug2_capacity = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount of water: "))
solution = water_jug_bfs(jug1_capacity, jug2_capacity, target)
if solution:
    print("Solution steps:")
    for step, state in enumerate(solution):
        print(f"Step {step}: Jug1 = {state[0]}, Jug2 = {state[1]}")
else:
    print("No solution found.")
