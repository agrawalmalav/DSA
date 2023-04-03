class PQNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        #Implement the isEmpty() function here
        return len(self.pq) == 0

    def getSize(self):
        #Implement the getSize() function here
        return len(self.pq)

    def getMax(self):
        #Implement the getMax() function here
        return self.pq[0].value

    def __percolateUp(self):
        childIdx = self.getSize()-1
        while childIdx > 0:
            parent = (childIdx-1)//2
            if self.pq[childIdx].priority > self.pq[parent].priority:
                self.pq[childIdx], self.pq[parent] = self.pq[parent], self.pq[childIdx]
                childIdx = parent
            else:
                break

    def insert(self, value, priority):
        #Implement the insert() function here
        node = PQNode(value, priority)
        self.pq.append(node)
        self.__percolateUp()
        #print('after insert', [x.value for x in self.pq])
        return

    def __percolateDown(self):
        curr = 0
        left = 2*curr + 1
        right = 2*curr+2

        while left < self.getSize():
            maxIdx = curr
            if self.pq[left].priority > self.pq[maxIdx].priority:
                maxIdx = left
            if right < self.getSize() and self.pq[right].priority > self.pq[maxIdx].priority:
                maxIdx = right

            if maxIdx == curr:
                break
            else:
                self.pq[maxIdx], self.pq[curr] = self.pq[curr], self.pq[maxIdx]
                curr = maxIdx
                left = curr*2+1
                right = curr*2+2

    def removeMax(self):
        #Implement the removeMax() function here
        ans = self.pq[0].value
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()

        self.__percolateDown()
        #print('after remove', [x.value for x in self.pq])
        return ans


myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1
