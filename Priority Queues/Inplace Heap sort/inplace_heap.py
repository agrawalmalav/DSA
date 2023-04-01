
def percolate_down(arr, i, n):
    p = i
    l = 2*p+1
    r = 2*p+2


    while l < n:
        minIdx = p
        if arr[l] < arr[minIdx]:
            minIdx = l
        if r < n and arr[r] < arr[minIdx]:
            minIdx = r
        if minIdx == p:
            return
        arr[p], arr[minIdx] = arr[minIdx], arr[p]
        p = minIdx
        l = 2*p+1
        r = 2*p+2
    return

def heapSort(arr):
    n= len(arr)
    for i in range(n, -1, -1):
        percolate_down(arr, i, n)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        percolate_down(arr, 0, i)
    return

n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr:
    print(ele,end=' ')
