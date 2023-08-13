from sys import stdin

def selectionSort(arr, n) :
    #Your code goes here  
    if n==1 or n==0:
        return 
    min_idx = 0
    min_val = arr[min_idx]
    for i in range(n-1):
        #print('step ', i)
        min_val = min(arr[i+1:])
        #print('min_val ', min_val)
        min_idx = arr[i+1:].index(min_val) +i +1
        #print("min_idx ", min_idx)
        if arr[i] > min_val:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
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
    selectionSort(arr, n)
    printList(arr, n)

    t-= 1
