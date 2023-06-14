
import sys

def duplicateNumber(arr, n) :
    #Your code goes here
    # Brute force approach, O(n2)
    '''
    for i in range(n-1):
        if arr[i] in arr[i+1:]:
            return arr[i]
    '''
    # approach 2- Using maths O(n)
    return sum(arr) - ((n-2)*(n-1))//2




#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(duplicateNumber(arr, n))

    t -= 1
    
