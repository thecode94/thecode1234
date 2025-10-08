from itertools import permutations

def is_magic(square):
    return (
        sum(square[0:3]) == 15 and
        sum(square[3:6]) == 15 and
        sum(square[6:9]) == 15 and
        sum(square[0::3]) == 15 and
        sum(square[1::3]) == 15 and
        sum(square[2::3]) == 15 and
        sum(square[0::4]) == 15 and
        sum(square[2:8:2]) == 15
    )

def solve_magic_square():
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for square in permutations(digits):
        if is_magic(square):
            return square
    return None


solution = solve_magic_square()

if solution:
    print("Magic Square Solution:")
    for i in range(0, 9, 3):
        print(solution[i], solution[i+1], solution[i+2])
else:
    print("No solution found.")
