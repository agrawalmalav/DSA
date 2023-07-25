from copy import deepcopy
from solution import Queue
import os
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

class Queue:
    # Stacks to be used in the operations.
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    # Enqueues 'X' into the queue. Returns true after enqueuing.
    def enqueue(self, X):
        # Write your code here
        for i in range(len(self.stk1)):
            self.stk2.append(self.stk1.pop())
        self.stk1.append(X)
        for i in range(len(self.stk2)):
            self.stk1.append(self.stk2.pop())
        return True

    """
      Dequeues top element from queue. Returns -1 if the queue is empty, 
      otherwise returns the popped element.
    """
    def dequeue(self):
        # Write your code here
        if len(self.stk1) == 0:
            return -1
        else:
            return self.stk1.pop()

class Runner:
    def __init__(self):
        self.arr = []
        self.t = 0

    def takeInput(self):
        self.t = int(input())
        for i in range(self.t):
            temp = list(map(int, stdin.readline().strip().split(" ")))
            self.arr.append(temp)

    def getCopy(self):
        arrCopy = deepcopy(self.arr)
        return arrCopy

    def execute(self):
        arrCopy = self.getCopy()
        que = Queue()
        for i in range(self.t):
            if(arrCopy[i][0]==1):
                ans = que.enqueue(arrCopy[i][1])
            else:
                ans = que.dequeue()

    def executeAndPrintOutput(self):
        que = Queue()
        for i in range(self.t):
            if(self.arr[i][0]==1):
                ans = que.enqueue(self.arr[i][1])
            else:
                ans = que.dequeue()
            print(ans)



runner = Runner()
runner.takeInput()
runner.executeAndPrintOutput()
