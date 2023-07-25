from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def swapNodes(head, i, j) :
	#Your code goes here
    idx = 0
    curr = head
    ni, nip, nj, njp = None, None, None, None 
    #print('start')
    while curr!= None:
        if idx == i-1:
            #print('ip')
            nip = curr
        elif idx == i:
            #print('i')
            ni = curr
        if idx ==j-1:
            #print('jp')
            njp = curr
        elif idx == j:
            #print('j')
            nj = curr
        idx +=1
        curr= curr.next
        #print('idx', idx)

    if nip== None:
        head = nj
    else:
        nip.next = nj
    if i+1==j:
        temp = nj.next
        nj.next = ni
        ni.next = temp
    else:
        nj.next, ni.next = ni.next, nj.next
        njp.next = ni
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




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1
