from solution import findNode
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

# Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    # Write your code here.
    curr = head
    i=0
    while curr != None:
        if curr.data == n:
            return i
        else:
            curr = curr.next
            i+=1
    return -1
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head

# Main.
t = int(stdin.readline().rstrip())
while t > 0 : 
    head = takeInput()
    n = int(stdin.readline().rstrip())
    print(findNode(head, n))
    t -= 1
