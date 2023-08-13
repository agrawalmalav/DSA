from sys import stdin

def sumOfTwoArrays(arr1, n, arr2, m, output) :
    #Your code goes here
    sum1, sum2 =0,0
    for i in range(n):
        sum1 = sum1*10 + arr1[i]
    for i in range(m):
        sum2 = sum2*10 + arr2[i]
    #print(sum1, sum2)
    total = sum1 + sum2
    i = max(n,m)
    while total >0:
        output[i] = total %10
        total //=10
        i-=1


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


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
    
    outputSize = (1 + max(n, m))
    output = outputSize * [0]
    
    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)
    
    t -= 1
