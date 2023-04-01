from sys import stdin

def lis(arr): 
    # Write your code here
    n = len(arr)
    dp = [1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] +1)
    return max(dp)









        

def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n
    

arr,n=takeInput()
print(lis(arr))
