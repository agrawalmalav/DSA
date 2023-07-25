from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def mergeTwoSortedLinkedLists(head1, head2):
    #approach 2
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    h1, h2 = head1, head2
    head, tail = None, None

    while h1 != None and h2 != None:
        if h1.data < h2.data:
            if head == None:
                head = h1
            else:
                tail.next = h1
            tail = h1
            h1 = h1.next
        else:
            if head == None:
                head = h2
            else:
                tail.next = h2
            tail = h2
            h2 = h2.next

        if h1 == None:
            tail.next = h2
            return head
        if h2 == None:
            tail.next = h1
            return head


def midPoint(head):
    # Write your code here
    if head == None or head.next == None:
        return head
    slow, fast = head, head

    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow


def mergeSort(head) :
    if head == None or head.next == None:
        return head

    mid = midPoint(head)
    head2 = mid.next
    mid.next = None

    head1 = mergeSort(head)
    head2 = mergeSort(head2)

    return mergeTwoSortedLinkedLists(head1,head2)




























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


def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1
