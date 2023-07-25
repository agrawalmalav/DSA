from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(curr) :
    #Your code goes here
    if head == None or head.next == None:
        return head
    oh, ot, eh, et = None, None, None, None
    #curr = head

    while curr != None:
        if curr.data %2 == 1:
            if oh == None:
                oh = curr
                #ot= curr
            else:
                ot.next = curr
            ot = curr
            #curr= curr.next
        else:
            if eh == None:
                eh = curr
                #et= curr
            else:
                et.next = curr
            et = curr
        curr= curr.next
    #ot.next , et.next = None, None
    if et != None:
        et.next = None
    if oh == None:
        return eh
    else:
        ot.next = eh
        return oh




            

    
























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
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1
