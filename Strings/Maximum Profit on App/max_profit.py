
def maximumProfit(arr):
	#Implement Your Function here
	arr = sorted(arr)
	curr_max = 0
	for i in range(len(arr)):
		if ( len(arr) -i)*arr[i] > curr_max:
			curr_max = (len(arr) - i)*arr[i]
	return curr_max

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)
