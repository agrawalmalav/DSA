def sortByPivot(arr, start, end):
    #print('arr initial', arr)
    c = 0
    el = arr[start]
    for x in arr[start:end+1]:
        if x < el:
            c +=1
    #print(c)
    pvt_idx = start+c
    arr[start], arr[pvt_idx] = arr[pvt_idx], arr[start]
    #print(arr)
    

    i= start
    j= end
    while i<pvt_idx and j> pvt_idx:
        if arr[i] < el:
            i+=1
        elif arr[j] >=el:
            j -=1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            j -=1
            i+=1
    #print(arr)
    return pvt_idx


def quickSort(arr, start, end):
    # Please add your code here
    if start > end:
        return
    pvt_idx = sortByPivot(arr, start, end)
    quickSort(arr, start, pvt_idx-1)
    quickSort(arr, pvt_idx+1, end)
    return


n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)
