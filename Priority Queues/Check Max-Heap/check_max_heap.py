def checkMaxHeap(lst):
    for i in range(len(lst)//2):
        l = 2*i+1
        r = 2*i+2

        if lst[i] < lst[l]:
            return False
        if r < len(lst) and lst[i] < lst[r]:
            return False
    return True


# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
