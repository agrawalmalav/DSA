

## Read input as specified in the question.
## Print output as specified in the question.
def subsets(arr, output, i, n):
    if i==n:
        for element in output:
            print(element, end= ' ')
        print()
        return

    subsets(arr, output, i+1, n)
    output2 = output[:]
    output2.append(arr[i])
    subsets(arr, output2, i+1, n)

    return

# main
n = int(input())
arr = [int(i) for i in input().split()]
output = []
subsets(arr, output, 0, n)
