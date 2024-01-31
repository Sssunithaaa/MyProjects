def find_next_empty(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] == -1:
                return i,j
    return None,None

def isValid(puzzle,guess,row,col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if guess == puzzle[r][c]:
                return False
    return True


def solve_sudoku(puzzle):
    row,col = find_next_empty(puzzle)
    if row is None:
        return True
    for guess in range(1,10):
        if isValid(puzzle,guess,row,col):
            puzzle[row][col]= guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col]=-1
    return False


puzzle=[[5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, 9, 8, -1, -1, -1, -1, 6, -1],
    [8, -1, -1, -1, 6, -1, -1, -1, 3],
    [4, -1, -1, 8, -1, 3, -1, -1, 1],
    [7, -1, -1, -1, 2, -1, -1, -1, 6],
    [-1, 6, -1, -1, -1, -1, 2, 8, -1],
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, 8, -1, -1, 7, 9]]
print(puzzle)
solve_sudoku(puzzle)
print(puzzle)

[[5, 3, 4, 6, 7, 8, 9, 1, 2], 
 [6, 7, 2, 1, 9, 5, 3, 4, 8], 
 [1, 9, 8, 3, 4, 2, 5, 6, 7], 
 [8, 5, 9, 7, 6, 1, 4, 2, 3], 
 [4, 2, 6, 8, 5, 3, 7, 9, 1], 
 [7, 1, 3, 9, 2, 4, 8, 5, 6], 
 [9, 6, 1, 5, 3, 7, 2, 8, 4], 
 [2, 8, 7, 4, 1, 9, 6, 3, 5], 
 [3, 4, 5, 2, 8, 6, 1, 7, 9]] 