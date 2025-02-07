from itertools import permutations
def solve_crypt_arithmetic(words, result):
    unique_chars = set("".join(words) + result)
    if len(unique_chars) > 10:
        print("Too many unique characters. Cannot assign unique digits.")
        return None    
    char_list = list(unique_chars)
    for perm in permutations(range(10), len(char_list)):
        char_map = dict(zip(char_list, perm))        
        if any(char_map[word[0]] == 0 for word in words + [result]):
            continue        
        word_values = [sum(char_map[c] * (10 ** i) for i, c in enumerate(word[::-1])) for word in words]
        result_value = sum(char_map[c] * (10 ** i) for i, c in enumerate(result[::-1]))        
        if sum(word_values) == result_value:
            return char_map
    return None
# Example usage
words = ["SEND", "MORE"]
result = "MONEY"
solution = solve_crypt_arithmetic(words, result)
if solution:
    print("Solution found:")
    for char, digit in solution.items():
        print(f"{char} = {digit}")
else:
    print("No solution found.")
