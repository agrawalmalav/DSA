import sys
from sys import stdin
def mcm(p,n, i, j, dp):
	# Write your code here
    cost = sys.maxsize
    if i==j:
        return 0

    for k in range(i, j):
        if dp[i][k] == -1:
            cost1 = mcm(p, n, i, k, dp)
            dp[i][k] = cost1
        else:
            cost1 = dp[i][k]
        
        if dp[k+1][j] ==-1:
            cost2 = mcm(p, n, k+1, j, dp)
            dp[k+1][j] = cost2
        else:
            cost2 = dp[k+1][j]

        currCost = cost1 + cost2 +  p[i-1]*p[k]*p[j]
        if cost > currCost:
            cost = currCost
    return cost

    





n=int(stdin.readline().strip())
p=[int(i) for i in stdin.readline().strip().split()]
dp = [[-1 for j in range(n+1)] for i in range(n+1)]
print(mcm(p,n, 1, n, dp))
