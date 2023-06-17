
from sys import stdin


def binarySearch(arr, n, x) :
    #Your code goes here
    l = 0
    r = n-1
    while l<=r:
        m = (l+r)//2
        if arr[m] == x:
            return m
        if x > arr[m]:
            l = m+1
        else:
            r= m-1
    return -1
            

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0 :
    
    x = int(input().strip())    
    print(binarySearch(arr, n, x))

    t -= 1
