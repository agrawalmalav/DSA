from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def skipMdeleteN(head, M, N) :
	#Your code goes here
    if M == 0:
        return None
    if N==0:
        return head
    curr = head
    while True:
        
        for i in range(1,M):
            if curr == None:
                return head
            else:
                curr= curr.next
        if curr == None:
            return head
        delstart = curr.next
        for i in range(1,N):
            if delstart == None:
                curr.next = None
                return head
            else:
                delstart = delstart.next
        if delstart == None:
            curr.next = None
            return head
        curr.next = delstart.next
        curr= curr.next


























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
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1
