from sys import stdin

def merge(arr1, n, arr2, m) : 
    #Your code goes here
    arr= []
    i = 0
    j= 0
    while i<n and j<m:
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i +=1
        elif arr1[i] >= arr2[j]:
            arr.append(arr2[j])
            j +=1
    #print('i = ', i, 'and j = ', j)

    if i ==n:
        arr.extend(arr2[j:])
    elif j ==m:
        arr.extend(arr1[i:])
    return arr  



#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1
