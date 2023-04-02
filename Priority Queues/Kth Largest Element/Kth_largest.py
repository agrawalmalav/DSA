import heapq
def kthLargest(lst, k):
    heap = lst[:k]
    heapq.heapify(heap)
    for i in range(k, len(lst)):
        heapq.heappush(heap, lst[i])
        heapq.heappop(heap)
    return heap[0]

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)
