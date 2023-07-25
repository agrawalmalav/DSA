from sys import stdin

# Following is the Node class already written for the Linked List.
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def deleteNode(head, pos) :
    # Write your code here.
    if head== None:
        return
    if pos ==0:
        head = head.next
        return head

    i = 1
    curr= head
    while i<pos:
        if curr.next != None:
            curr= curr.next
            i+=1
        else:
            return head
    if curr.next == None:
        return head
    curr.next = curr.next.next
    return head









# Taking Input Using Fast I/O.
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



# To print the linked list.
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


# Main.
t = int(stdin.readline().strip())

while t > 0 :
    
    head = takeInput()
    pos = int(stdin.readline().rstrip())
    
    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
