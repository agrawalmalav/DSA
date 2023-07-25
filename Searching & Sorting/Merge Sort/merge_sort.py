def mergeSort(arr, start, end):
    # Please add your code here
    if len(arr) == 0 or len(arr) ==1:
        return
    
    mid = (start+end)//2
    arr1 = arr[:mid]
    arr2 = arr[mid:]

    mergeSort(arr1, 0 , len(arr1))
    mergeSort(arr2, 0, len(arr2))

    i, j, k = 0, 0,0

    while i< len(arr1) and j< len(arr2):
        if arr1[i] > arr2[j]:
            arr[k] = arr2[j]
            k+=1
            j+=1
        else:
            arr[k]=arr1[i]
            k += 1
            i += 1
    while i< len(arr1):
        arr[k] = arr1[i]
        k+=1
        i+=1

    while j < len(arr2):
        arr[k]=arr2[j]
        k += 1
        j += 1






# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)
