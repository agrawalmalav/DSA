from solution import *
import os
import sys
from sys import stdin
from copy import deepcopy

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None






def length(head) :
    #Your code goes here
    count = 0
    while head != None:
        count += 1
        head = head.next
    return count










        




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
    print(length(head))

    t -= 1
sys.setrecursionlimit(10**7)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Runner:
    def __init__(self):
        self.head = None
        self.tail = None

    def takeInput(self) :

        datas = list(map(int, input().split()))

        i = 0
        while (i < len(datas)) and (datas[i] != -1) :
            data = datas[i]
            newNode = Node(data)

            if self.head is None :
                self.head = newNode
                self.tail = newNode
            else :
                self.tail.next = newNode
                self.tail = newNode

            i += 1

    def executeAndPrintOutput(self):
        
        ans = length(self.head)

        print(ans)

runner = Runner()
runner.takeInput()
runner.executeAndPrintOutput()
