import heapq
# Define the goal state and possible moves (up, down, left, right)
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
moves = {
    0: [(1, "Right"), (3, "Down")],
    1: [(0, "Left"), (2, "Right"), (4, "Down")],
    2: [(1, "Left"), (5, "Down")],
    3: [(0, "Up"), (4, "Right"), (6, "Down")],
    4: [(1, "Up"), (3, "Left"), (5, "Right"), (7, "Down")],
    5: [(2, "Up"), (4, "Left"), (8, "Down")],
    6: [(3, "Up"), (7, "Right")],
    7: [(4, "Up"), (6, "Left"), (8, "Right")],
    8: [(5, "Up"), (7, "Left")]
}
# Function to calculate the heuristic (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            x, y = divmod(i, 3)
            goal_x, goal_y = divmod(state[i] - 1, 3)
            distance += abs(x - goal_x) + abs(y - goal_y)
    return distance
# Function to generate the successors of a state
def generate_successors(state):
    zero_pos = state.index(0)
    successors = []
    for move, direction in moves[zero_pos]:
        new_state = state[:]
        new_state[zero_pos], new_state[move] = new_state[move], new_state[zero_pos]
        successors.append((new_state, state[move], direction))
    return successors
# A* search algorithm
def a_star_search(initial_state):
    open_list = []
    heapq.heappush(open_list, (heuristic(initial_state), 0, initial_state, [], []))
    closed_list = set()   
    while open_list:
        _, cost, current_state, path, moves_list = heapq.heappop(open_list)        
        if current_state == goal_state:
            return path + [current_state], moves_list, cost        
        closed_list.add(tuple(current_state))        
        for successor, moved_tile, move in generate_successors(current_state):
            if tuple(successor) not in closed_list:
                new_path = path + [current_state]
                new_moves = moves_list + [(moved_tile, move)]
                heapq.heappush(open_list, (cost + 1 + heuristic(successor), cost + 1, successor, new_path, new_moves))
    
    return None, None, None
# Function to print the state in 3x3 format
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()
# Input from the user
def get_user_input():
    print("Enter the puzzle configuration as 9 integers (0 for the blank space).")
    print("Example: 1 2 3 4 0 5 6 7 8")
    user_input = input("Enter your initial configuration: ").split()
    if len(user_input) != 9 or not all(num.isdigit() for num in user_input):
        print("Invalid input. Please enter exactly 9 numbers.")
        return get_user_input()
    return list(map(int, user_input))
# Example usage
initial_state = get_user_input()
solution, move_directions, path_cost = a_star_search(initial_state)
if solution:
    print("Solution found in", len(solution) - 1, "moves:")
    for i, state in enumerate(solution):
        print_state(state)
        if i < len(move_directions):
            moved_tile, move = move_directions[i]
            print(f"Move {moved_tile} {move}")
    print("Total Path Cost:", path_cost)
else:
    print("No solution found.")
