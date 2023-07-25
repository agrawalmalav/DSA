from sys import stdin

def arrayEquilibriumIndex(arr, n) :
    #Your code goes here

    lsum, rsum = 0, sum(arr)
    for i in range(-1, n-1,1):
        if(lsum ==rsum):
            return i
        else:
            lsum += arr[i]
            rsum -= arr[i+1]
    else:
        return(-1)































#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t-= 1
