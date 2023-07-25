
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def lengthofLL(head):
    curr = head
    i=0
    while curr != None:
        i+=1
        curr= curr.next
    return i



def appendLastNToFirst(head, n) :
    #Your code goes here
    if n<1:
        return head
    len = lengthofLL(head)
    #print(n, len)
    if n> len:
        #print('should return')
        return
    curr = head
    for i in range(len-n-1):
        curr = curr.next
    last = curr
    first = curr.next
    
    while curr.next != None:
        curr= curr.next
    curr.next = head
    head = first
    last.next = None
    return head




























#Taking Input Using Fast I/O
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


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1 
