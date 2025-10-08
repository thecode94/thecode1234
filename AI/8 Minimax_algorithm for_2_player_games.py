
tree = [
    [3, 5],
    [2, 9],
    [0, -1]
]

def minimax(tree):
    min_values = []

    for branch in tree:
        min_val = min(branch)
        min_values.append(min_val)

    return max(min_values)

best_value = minimax(tree)
print(f"Best value for MAX: {best_value}")
