import sys

def findUnique(arr, n) :
    #Your code goes here
    #approach 1- Brute force O(n^2)
    '''
    if n ==1:
        return arr[0]
    for i in arr:
        if (arr.count(i) == 1):
            return i
    '''
    # approach 2- using XOR O(n)
    ans = arr[0]
    for i in range(1, n):
        ans = ans^arr[i]
    return ans



#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1
