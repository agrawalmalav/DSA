from sys import stdin

def spiralPrint(mat, n, m):
    #Your code goes here
    start = [0,0]
    end = [0, m-1]

    hr = True
    hrcnt, vrcnt = 0,0

    for itr in range(m+n-1):
        if hr == True:
            if hrcnt%2 == 0:
                for j in range(start[1], end[1] +1):
                    print(mat[start[0]][j], end= ' ')
                start[0], start[1] = end[0] +1, end[1]
                end[0] = n -1 -hrcnt//2
                hrcnt += 1
                hr = False

            else:
                for j in range(start[1], end[1]-1, -1):
                    print(mat[start[0]][j], end=" ")
                start[0], start[1] = end[0] -1, end[1]
                end[0] = (hrcnt +1)//2
                hrcnt += 1
                hr = False

        else:
            if vrcnt%2 == 0:
                for i in range(start[0], end[0] +1):
                    print(mat[i][start[1]], end= ' ')
                start[0], start[1] = end[0], end[1]-1
                end[1] = vrcnt//2
                vrcnt += 1
                hr = True

            else:
                for i in range(start[0], end[0]-1, -1):
                    print(mat[i][start[1]], end=" ")
                start[0], start[1] = end[0] , end[1]+1
                end[1] = m -1- hrcnt//2 
                vrcnt += 1
                hr = True

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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
