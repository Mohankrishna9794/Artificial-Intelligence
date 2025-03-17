def minimax(depth, node, is_max, scores, height):
    if depth == height:
        return scores[node]    
    next_nodes = [node * 2, node * 2 + 1]
    values = [minimax(depth + 1, n, not is_max, scores, height) for n in next_nodes]    
    return max(values) if is_max else min(values)
scores = [3, 5, 2, 9, 12, 5, 23, 23]  # Leaf node scores
height = len(scores).bit_length() - 1  # Calculate tree height
print("Optimal value:", minimax(0, 0, True, scores, height))
