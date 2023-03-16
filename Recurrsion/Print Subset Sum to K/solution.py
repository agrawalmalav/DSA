
## Read input as specified in the question.
## Print output as specified in the question.
def subsets(arr, op, i, n, k):
    #print('condn', output == k)
    if i==n:
        if sum(op) == k:
        #for element in op:
            for x in op:
                print(x, end= ' ')
            print()
        return

    subsets(arr, op, i+1, n, k)
    op2 = op[:]
    op2.append(arr[i])
    subsets(arr, op2, i+1, n, k)

    return

# main
n = int(input())
arr = [int(i) for i in input().split()]
op = []
k = int(input())
subsets(arr, op, 0, n, k)
