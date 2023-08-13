# Take Minimum value as MIN_VALUE = -2147483648
from sys import stdin


def secondLargestElement(arr, n):
    #Your code goes here
    m1, m2 = -2**31, -2**31

    for x in arr:
        if x> m1:
            m2= m1
            m1 = x
        elif x > m2 and m1 != x:
            m2 =x
    return m2



#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0



#main
t = int(stdin.readline().rstrip())

while t > 0 : 
    
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1
