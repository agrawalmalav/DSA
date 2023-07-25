from sys import stdin
'''
    Time Complexity : O(N*log(N))
    Space Complexity : O(1)
    
    Where N is the size of the array
'''

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def pairSum(arr, n, target):

    ans = 0
    arr.sort()

    # Take two pointers
    i = 0
    j = n - 1

    while (i < j):

        # If target is greater
        if (arr[i] + arr[j] < target):
            i += 1

        # If target is lesser
        elif (arr[i] + arr[j] > target):
            j -= 1

        # If target is equal
        else:

            # Find the frequency of arr[i]
            initialLeftElement = arr[i]
            initialLeftIndex = i

            while (i < j and arr[i] == initialLeftElement):
                i += 1

            # Find the frequency of arr[j]
            initialRightElement = arr[j]
            initialRightIndex = j

            while (j >= i and arr[j] == initialRightElement):
                j -= 1

            # If arr[i] and arr[j] are the same
            # then it gets counted twice so subtract 1
            if (initialLeftElement == initialRightElement):
                equalNumbers = (i - initialLeftIndex) + \
                    (initialRightIndex - j) - 1
                ans += (equalNumbers * (equalNumbers + 1)) // 2

            else:
                ans += ((i - initialLeftIndex) * (initialRightIndex - j))

    return ans




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
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))

    t -= 1
