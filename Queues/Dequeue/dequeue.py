
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Dequeue:

    def __init__(self, max_size = 10):
        self.max_size = max_size
        self.front = None
        self.tail = None
        self.count = 0

    def insertFront(self, x):
        if self.count == self.max_size:
            print(-1)
            return
        
        if self.front == None:
            self.front = Node(x)
            self.tail = self.front
        else:
            node = Node(x)
            node.next = self.front
            self.front.prev = node
            self.front = node
        self.count += 1

    def insertRear(self, x):
        if self.count == self.max_size:
            print(-1)
            return

        if self.front == None:
            self.front = Node(x)
            self.tail = self.front
            self.count = 1
        else:
            node = Node(x)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.count +=1
        
    def deleteFront(self):
        if self.count == 0:
            print(-1)
            return
        
        if self.front == self.tail:
            self.front = None
            self.tail = None
            self.count = 0
        else:
            new = self.front.next
            new.prev = None
            self.front.next = None
            self.front = new
            self.count-=1

    def deleteRear(self):
        if self.count == 0:
            print(-1)
            return

        if self.front == self.tail:
            self.front = None
            self.tail = None
            self.count = 0
        else:
            new = self.tail.prev
            new.next = None
            self.tail.prev = None
            self.tail = new
            self.count -= 1

    def getFront(self):
        if self.count == 0:
            return -1
        return self.front.data

    def getRear(self):
        if self.count == 0:
            return -1
        return self.tail.data


dq = Dequeue()
task = [int(x) for x in input().split()]
i = 0
while task[i] != -1:
    if task[i] == -1:
        break
    elif task[i] == 1:
        dq.insertFront(task[i+1])
        i+=1
    elif task[i] == 2:
        dq.insertRear(task[i+1])
        i+=1
    elif task[i] == 3:
        dq.deleteFront()
    elif task[i] == 4:
        dq.deleteRear()
    elif task[i] == 5:
        print(dq.getFront())
    elif task[i] == 6:
        print(dq.getRear())
    i+=1
