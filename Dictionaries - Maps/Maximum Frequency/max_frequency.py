# Read input as sepcified in the question
# Print output as specified in the question
n = int(input())
lst = [int(x) for x in input().split()]
count = {}
for x in lst:
    count[x] = count.get(x,0) +1
#print(count)
max = 0
for x in count:
    if count[x] > max or (count[x] == max and lst.index(x) < lst.index(num)):
        max=count[x]
        num = x

print(num)
