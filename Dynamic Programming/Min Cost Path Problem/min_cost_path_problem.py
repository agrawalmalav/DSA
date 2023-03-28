
from sys import stdin
MAX_VALUE = 2147483647

def getMinPath(input, i, j, m, n, dp):
    if i == m-1 and j== n-1:
        return input[i][j]

    if j<n-1:
        if dp[i][j+1] != MAX_VALUE:
            costRight = dp[i][j+1]
        else:
            costRight = getMinPath(input, i, j+1, mRows, nCols, dp)
            dp[i][j+1] = costRight
    else:
        costRight = MAX_VALUE

    if i < m-1:
        if dp[i+1][j] != MAX_VALUE:
            costDown = dp[i+1][j]
        else:
            costDown = getMinPath(input, i+1, j, mRows, nCols, dp)
            dp[i+1][j] = costDown
    else:
        costDown = MAX_VALUE

    if i < m-1 and j < n-1:
        if dp[i+1][j+1] != MAX_VALUE:
            costDiag = dp[i+1][j+1]
        else:
            costDiag = getMinPath(input, i+1, j+1, mRows, nCols, dp)
            dp[i+1][j+1] = costDiag
    else:
        costDiag = MAX_VALUE

    return input[i][j] + min(costDiag, costDown, costRight)    



def minCostPath(input, mRows, nCols, dp) :
	#Your code goes here 
    return getMinPath(input, 0, 0, mRows, nCols, dp)



#taking input using fast I/O method
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])
    
    if mRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


#main
mat, mRows, nCols = take2DInput()
dp = [[MAX_VALUE for i in range(nCols)] for x in range(mRows)]
#print(dp)
print(minCostPath(mat, mRows, nCols, dp))
