from sys import stdin

def pushZerosAtEnd(arr, n) :
    #Your code goes here
    '''
    # Insertion style code
    for i in range(1, n):
        curr = i
        for j in range(i-1, -1, -1):
            if arr[curr] !=0 and arr[j] ==0:
                arr[curr], arr[j] = arr[j], arr[curr]
                curr = j
            else: 
                break'''

    #buble sort style code
    '''
    for i in range(n-2):
        for j in range(0, n-1-i):
            if arr[j] == 0 and arr[j+1] !=0:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                '''
    # without sorting approach 1
    '''
    count = arr.count(0)
    for i in range(count):
        arr.remove(0)
        arr.append(0)
        '''
    # without sorting approach 2
    '''
    temp = []
    for x in arr:
        if x !=0:
            temp.append(x)
    temp.extend([0]*(n-len(temp)))
    print(temp, len(temp))
    arr = temp
    print(arr)
    '''

# approach 3
    i,k =0,0
    while i<n:
        if arr[i] !=0:
            arr[i] , arr[k] = arr[k], arr[i]
            i+=1
            k+=1
        elif arr[i] ==0:
            i+=1

    
        



























#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split()))
    return arr, n
  

#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()

    pushZerosAtEnd(arr, n)
    printList(arr, n)

    t -= 1
