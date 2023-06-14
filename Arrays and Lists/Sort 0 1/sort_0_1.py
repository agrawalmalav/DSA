from sys import stdin

def sortZeroesAndOne(arr, n) :
    #Your code goes here 
    left = 0
    right = n-1
    '''while left < right:
        if arr[left] == 0:
            left +=1
        if arr[right] == 1:
            right -=1
        if arr[left] == 1 and arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]'''

    for i in range(n):
        if arr[i]==1:
            while arr[right] != 0 and right > i:
                right -=1
            arr[right], arr[i] = arr[i], arr[right]




#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1
