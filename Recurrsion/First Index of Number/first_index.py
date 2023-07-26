def firstIndex(arr, x, idx = 0):
    # Please add your code here
    #By passing the array :
    '''
    if len(arr) == 0:
        return -1

    if arr[0] == x:
        return 0
    else: 
        temp = firstIndex(arr[1:], x)
        if temp ==-1:
            return -1
        else:
            return 1+temp
    '''
    #by index 
    if idx == len(arr):
        return -1
    if arr[idx] ==x:
        return idx
    else:
        return firstIndex(arr,x,idx+1)


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))
