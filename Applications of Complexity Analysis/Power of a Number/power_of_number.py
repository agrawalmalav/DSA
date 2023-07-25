def power(x, n):
    # Please add your code here
    if n==0:
        return 1
    elif n==1:
        return x
    
    return power(x, n//2)*power(x, n-n//2)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
