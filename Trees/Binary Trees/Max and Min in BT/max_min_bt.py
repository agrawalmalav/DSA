from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



#Representation of the Pair Class
class Pair :

    def __init__(self, minimum, maximum) :
        self.minimum = minimum
        self.maximum = maximum



def getMinAndMax(root) :
    #Your code goes here
    if root.left == None and root.right == None:
        return Pair(root.data, root.data)

    minans, maxans = root.data, root.data
    if root.left != None:
        leftpair = getMinAndMax(root.left)
        minans = min(minans, leftpair.minimum)
        maxans = max(maxans, leftpair.maximum)
    if root.right != None:
        rightpair= getMinAndMax(root.right)
        minans = min(minans, rightpair.minimum)
        maxans = max(maxans, rightpair.maximum)
    return Pair(minans, maxans)


#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

    
def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
       
        while not inputQ.empty():
       
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
       
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()

pair = getMinAndMax(root)
print(str(str(pair.minimum) + " " + str(pair.maximum)))
