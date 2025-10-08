def is_safe(queen_positions,row,col):
    for r in range(row):
        c=queen_positions[r]
        if c==col or abs(c-col)==abs(r-row):
            return False
    return True
    
def solve_n_queens(n):
    solutions=[]
    queen_positions=[-1]*n

    def backtrack(row):
        if row==n:
            solutions.append(queen_positions[:])
            return

        for col in range(n):
            if is_safe(queen_positions,row,col):
                queen_positions[row]=col
                backtrack(row+1)
                queen_positions[row]=-1

    backtrack(0)
    return solutions

solutions=solve_n_queens(4)

def print_boards(solutions):
    for sol in solutions:
        print("Solutions:")
        for i in sol:
            row=['.']*len(sol)
            row[i]='Q'
            print("".join(row))
        print()
print_boards(solutions)
        
