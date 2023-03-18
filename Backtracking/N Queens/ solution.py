def queenSafe(i, j, board, n):

    ci = i-1
    cj =j
    while ci>=0:
        if board[ci][cj] ==1:
            return False
        ci -=1

    ci = i-1
    cj =j-1
    while cj >=0 and ci >=0:
        if board[ci][cj] ==1:
            return False
        ci -=1
        cj -=1

        
    ci = i-1
    cj =j+1
    while ci >= 0 and cj <n:
        if board[ci][cj] == 1:
            return False
        ci -=1
        cj +=1
    return True

def printQueensHelper(i, n, board):
    if i ==n:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end = ' ')
        print()
        return

    for j in range(n):
        if queenSafe(i, j, board, n) is True:
            board[i][j] =1
            printQueensHelper(i+1, n, board)
            board[i][j] = 0
        
    return

def nQueen(n):
    #Implement Your Code Here
    board = [[0 for j in range(n) ] for i in range(n)]
    printQueensHelper(0, n, board)
    
n = int(input())
nQueen(n)

