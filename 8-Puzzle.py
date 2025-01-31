import heapq
# Define the goal state and possible moves (up, down, left, right)
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
moves = {
    0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
    3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
    6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
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
    for move in moves[zero_pos]:
        new_state = state[:]
        new_state[zero_pos], new_state[move] = new_state[move], new_state[zero_pos]
        successors.append(new_state)
    return successors
# A* search algorithm
def a_star_search(initial_state):
    open_list = []
    heapq.heappush(open_list, (heuristic(initial_state), 0, initial_state, []))
    closed_list = set()
    while open_list:
        _, cost, current_state, path = heapq.heappop(open_list)
        if current_state == goal_state:
            return path + [current_state]
        closed_list.add(tuple(current_state))
        for successor in generate_successors(current_state):
            if tuple(successor) not in closed_list:
                new_path = path + [current_state]
                heapq.heappush(open_list, (cost + 1 + heuristic(successor), cost + 1, successor, new_path))
    return None
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
solution = a_star_search(initial_state)
if solution:
    print("Solution found in", len(solution) - 1, "moves:")
    for state in solution:
        print_state(state)
else:
    print("No solution found.")
