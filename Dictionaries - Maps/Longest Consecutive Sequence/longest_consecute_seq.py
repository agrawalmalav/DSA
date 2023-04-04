from sys import stdin
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self, size = 100):
        self.bucketsize = size
        self.count = 0
        self.bucket = [None for i in range(self.bucketsize)]

    def size(self):
        return self.count
    
    def getIndex(self, key):
        code = hash(key)
        return (abs(code) % self.bucketsize)

    def search(self, key):
        index = self.getIndex(key)
        head = self.bucket[index]
        while head != None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def insert(self, key, value):
        index = self.getIndex(key)
        head = self.bucket[index]
        while head!= None:
            if head.key == key:
                head.value = value
            return
        head= self.bucket[index]
        node = Node(key, value)
        node.next = head
        self.bucket[index] = node
        self.count +=1
        loadFactor = self.count/self.bucketsize
        if loadFactor > 0.7:
            self.rehash()
        return

    def delete(self, key):
        index = self.getIndex(key)
        head = bucket[index]
        prev = None
        curr = head
        while curr != None:
            if curr.key == key:
                if prev == None:
                    bucket[index] = head.next
                    count -=1
                    return head.value
                else:
                    prev.next = curr.next
                    count -=1
                    return curr.value
            prev= curr
            curr = curr.next
        return None

    def rehash(self):
        temp = self.bucket
        self.bucket = [None for i in range(2*self.bucketsize)]
        self.bucketsize*=2

        for idx in temp:
            head = idx
            while head != None:
                self.insert(head.key, head.value)
        return
            

def longestConsecutiveSubsequence(arr,n): 
    # Write your code here
    hashmap = Map(int(n/0.7))
    for x in arr:
        hashmap.insert(x, True)

    start = None
    length = 0

    for el in arr:
        #print('el', el)
        if hashmap.search(el) == True:
            currlen = 1
            i = el+1
            while hashmap.search(i) != None:
                hashmap.insert(i, False)
                currlen +=1
                i+=1
            i = el -1
            while hashmap.search(i) != None:
                hashmap.insert(i, False)
                currlen +=1
                i-=1
            #print('currlen', currlen)
            #print('i', i)
            if currlen > length or (currlen == length and arr.index(i+1) < arr.index(start) ):
                length = currlen
                start = i+1
        #print('start:', start, 'len:', length )

    return [start, start +length -1]










def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

    
# Main 
arr,n=takeInput()
ans = longestConsecutiveSubsequence(arr,n) 
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(*ans)
