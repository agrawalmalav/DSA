## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
arr = [int(x) for x in input().split()]
curr_max = arr[-1]
ans = []
for i in range(n-1, -1, -1):
    #print(curr_max, arr[i])
    if arr[i] >= curr_max:
        curr_max = arr[i]
        ans.append(curr_max)
    #print(curr_max, arr[i])
for x in ans[::-1]:
    print(x, end= ' ')
