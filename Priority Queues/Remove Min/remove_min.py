class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
        
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
        
    def __percolateDown(self):
        currIdx = 0
        while currIdx < self.getSize():
            childLeft = 2*currIdx + 1
            childRight = 2*currIdx + 2

            if childLeft < self.getSize() and childRight < self.getSize():
                leftPrior = self.pq[childLeft].priority
                rightPrior = self.pq[childRight].priority
                currPrior = self.pq[currIdx].priority

                if currPrior > leftPrior and leftPrior < rightPrior:
                    self.pq[currIdx], self.pq[childLeft] = self.pq[childLeft], self.pq[currIdx]
                    currIdx = childLeft
                elif currPrior > rightPrior and rightPrior < leftPrior:
                    self.pq[currIdx], self.pq[childRight] = self.pq[childRight], self.pq[currIdx]
                    currIdx = childRight
                else:
                    break

            elif childLeft < self.getSize() and childRight >= self.getSize():
                if self.pq[currIdx].priority > self.pq[childLeft].priority:
                    self.pq[currIdx], self.pq[childLeft] = self.pq[childLeft], self.pq[currIdx]
                    currIdx = childLeft
                else:
                    break
            else:
                break


    def removeMin(self):
        ans = self.pq[0].ele
        self.pq[0] = self.pq[-1]
        self.pq.pop()
        self.__percolateDown()
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
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
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
        
    
