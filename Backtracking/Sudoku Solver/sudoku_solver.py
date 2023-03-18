import sys
sys.setrecursionlimit(10**8)


def is_valid(board, r,c,k):
    if k in board[r] :
        return False
    for x in range(9):
        if k == board[x][c]:
            return False
    if k in [ [board[i][j] for i in range( (r - r%3), (r-r%3 +3) )] for j in range( (c- c%3), (c - c%3+3)) ]:
        return False
    return True
    

def solveSudoku(board, r, c):
    #Implement Your Code Here
    if r==8 and c== 9:
        for i in range(9):
            for j in range(9):
                print(board[i][j], end = ' ')
            print()
        return True
    if c==9:
        c=0
        r+=1
        #return solveSudoku(board, r+1, 0)

    if board[r][c] > 0:
        return solveSudoku(board, r, c+1)
    for k in range(1, 10, 1):
        if is_valid(board, r,c, k):
            board[r][c] = k
            if solveSudoku(board, r, c+1):
                return True
        board[r][c] = 0
    return False


            


    
    

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board, 0, 0)
if ans is True:
    print('SOlution Found!')
else:
    print('No Solution Exists')
