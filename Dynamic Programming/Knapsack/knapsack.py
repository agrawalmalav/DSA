
from sys import stdin

def knapsack(weights, values, n, maxWeight, i=0) :
	#Your code goes here
    #print(values)
    if i == n:
        return 0
    
    if weights[i] > maxWeight:
        ans = knapsack(weights, values, n, maxWeight, i+1)
        return ans
    else:
        ans1 = knapsack(weights, values, n, maxWeight, i+1)
        ans2 = values[i] + knapsack(weights, values, n, maxWeight - weights[i],  i+1)
        return max(ans1, ans2)
    

def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), list(), n, 0

    weights = list(map(int, stdin.readline().rstrip().split(" ")))
    values = list(map(int, stdin.readline().rstrip().split(" ")))
    maxWeight = int(stdin.readline().rstrip())

    return weights, values, n, maxWeight


#main
weights, values, n, maxWeight = takeInput()

print(knapsack(weights, values, n, maxWeight))
