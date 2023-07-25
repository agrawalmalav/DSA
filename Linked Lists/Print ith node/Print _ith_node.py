
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None




def printIthNode(head, i):
    #Your code goes here
    '''
    if head== None:
        return
    else:
        for x in range(i):
            if head.next == None:
                return
            else:
                head= head.next
        print(head.data)
        return
    '''
    n=0
    while n<i and head != None:
        head = head.next
        n+=1
    if n==i and head != None:
        print(head.data)
    

























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
    i = int(stdin.readline().rstrip())
    printIthNode(head, i)

    t -= 1
