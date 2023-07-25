from sys import stdin

def findUnique(arr, n) :
    #Your code goes here
    ''' 
    #approach 1
    unique = []
    for x in arr:
        if x not in unique:
            unique.append(x)
        else:
            unique.remove(x)
    return unique[0]
    '''
    #approach2
    arr = sorted(arr)
    #print(arr)
    i=0
    while i<n-1:
        if arr[i] == arr[i+1]:
            i+=2
        else:
            return arr[i]
    
    return arr[-1] 





























#taking input using fast I/O method
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
    print(findUnique(arr, n))

    t-= 1
