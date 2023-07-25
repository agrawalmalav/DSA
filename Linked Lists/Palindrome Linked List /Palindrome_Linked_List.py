
from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
def length(head):
    i=0
    while head != None:
        head= head.next
        i+=1
    return i 

def reverse(head):
    # Write your code here
    if head == None or head.next == None:
        return head
    next = None
    curr = head
    while curr != None:
        node = Node(curr.data)
        node.next = next
        next = node
        curr= curr.next
    return node

def midPoint(head) :
    # Write your code here
    if head == None or head.next == None:
        return head
    slow , fast = head, head

    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow

def isPalindrome(head) :
    #Your code goes here
    '''
    #approach 1: very bad

    curr = head
    lst = []    
    while curr != None:
        lst.append(curr.data)
    i=0
    j = len(lst)-1
    while i<j:
        if lst[i] != lst[j]:
            return False
        else:
            i+=1
            j-=1
    return True
    '''

    #approach 2
    if head == None or head.next == None:
        return True
    mid = midPoint(head)
    nexthead = mid.next
    revHead = reverse(nexthead)
    while revHead != None:
        if head.data != revHead.data:
            return False
        else:
            head = head.next
            revHead= revHead.next
    else: 
        return True
























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
    
    if isPalindrome(head) :
        print('true')
    else :
        print('false')
        
    t -= 1
