## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def nextNumber(head, carry):
    #Implement Your Code here
    if head.next == None:
        if head.data == 9:
            head.data = 0
            carry = 1
            return head, carry
        else:
            head.data += 1
            carry = 0
            return head, carry

    temphead, carry = nextNumber(head.next, 0)
    if carry == 1:
        head.data = 0
        node = Node(1)
        node.next = head
        node = head
    else:
        return head, 0


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printll(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next
    return


# Main
# Read the link list elements including -1
arr = [int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head, carry = nextNumber(l, 0)
if carry == 1:
    node = Node(1)
    node.next  = head
    head = node
printll(head)
