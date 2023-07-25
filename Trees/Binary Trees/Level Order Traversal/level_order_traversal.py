from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    #Your code goes here
    if root == None:
        return
    q = queue.Queue()
    q.put(root)
    count = 0
    i = 1

    while not q.empty():
        while i > 0:
            node = q.get()
            print(node.data, end= ' ')

            if node.left != None:
                q.put(node.left)
                count +=1
            if node.right != None:
                q.put(node.right)
                count +=1
            i -= 1
        print()
        i = count
        count = 0
    
'''
    if root == None:
        return
    mainq = queue.Queue()
    mainq.put(root)
    q = queue.Queue()

    while not mainq.empty():
        while not mainq.empty():

            node = mainq.get()
            print(node.data, end= ' ')
            if node.left != None:
                q.put(node.left)
            if node.right!= None:
                q.put(node.right)
        print()
        mainq, q = q, mainq
        
'''

                

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


# Main
root = takeInput()
printLevelWise(root)
