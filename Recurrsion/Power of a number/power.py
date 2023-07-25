## Write your code here
## To take space separated input for two variables, we use the following syntax (3 lines)
x, n = input().split()
x = int(x)
n = int(n)

def power(x,n):
    if n==0:
        return 1
    return power(x, n-1)*x

print(power(x,n))
