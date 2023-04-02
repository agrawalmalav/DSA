import heapq
def kSmallest(lst, k):
    ######################
    #PLEASE ADD CODE HERE#
    ######################
    heap = lst[:k]
    heapq._heapify_max(heap)
    for i in range(k, len(lst)):
        heap.append(lst[i])
        heapq._heapify_max(heap)
        heapq._heappop_max(heap)
    return heap



# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')
