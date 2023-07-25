''' 
    Following is the node structure

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

'''

def deleteAlternateNodes(head):
    # Write your code here
    curr = head

    if curr == None or curr.next == None:
        return curr

    curr.next = curr.next.next
    curr = curr.next
    head.next = deleteAlternateNodes(curr)
    return head
from copy import deepcopy
from solution import deleteAlternateNodes
import os
import sys
sys.setrecursionlimit(10**7)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, input().rstrip().split(" ")))

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

head = takeInput()

deleteAlternateNodes(head)
printLinkedList(head) 
