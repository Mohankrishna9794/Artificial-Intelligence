def alpha_beta(depth, node, is_max, scores, alpha, beta, height):
    if depth == height:
        return scores[node]    
    values = [alpha_beta(depth + 1, node * 2 + i, not is_max, scores, alpha, beta, height) for i in range(2)]
    best = max(values) if is_max else min(values)    
    if is_max:
        alpha = max(alpha, best)
    else:
        beta = min(beta, best)    
    return best if beta > alpha else best
scores = [3, 5, 6, 9, 1, 2, 0, -1]  # Example leaf node values
height = len(scores).bit_length() - 1  # Calculate tree height
print("Optimal value:", alpha_beta(0, 0, True, scores, float('-inf'), float('inf'), height))
