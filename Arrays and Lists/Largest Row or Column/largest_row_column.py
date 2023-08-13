'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin

def findLargest(arr, nRows, mCols):
    #Your code goes here
    if nRows <2 or mCols<2:
        print('row',0,-2**31)
        return
    rowidx, clmidx, maxrow, maxclm = -1,-1,0,0
    for i  in range(nRows):
        if (sum(arr[i]) > maxrow or (rowidx == -1 and maxrow ==0)):
            rowidx = i
            maxrow = sum(arr[i])
    
    for j in range(mCols):
        colsum =0
        for row in arr:
            colsum += row[j]
        if colsum > maxclm or (clmidx==-1 and maxclm == 0):
            maxclm=colsum
            clmidx = j

    if maxrow>=maxclm:
        print('row', rowidx, maxrow)
    else:
        print('column', clmidx, maxclm)


#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1
