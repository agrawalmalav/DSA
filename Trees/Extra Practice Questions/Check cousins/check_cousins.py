## Read input as specified in the question.
## Print output as specified in the question.
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
def isSibling(root, p, q):
    if root == None:
        return False
    #if (root.left == p and root.right == q) or (root.right ==p and root.left == q):
    #    return True
    #else:
    return (root.left == p and root.right == q) or (root.right == p and root.left == q) or isSibling(root.left, p, q) or isSibling(root.right, p, q)

def getLevel(root, data, level = 1):
    if root == None:
        return 0
    if root.data == data:
        return level
    leftLevel = getLevel(root.left, data)
    if leftLevel != 0:
        return 1+ leftLevel
    rightLevel = getLevel(root.right, data)
    if rightLevel != 0:
        return 1+ rightLevel
    return 0

def checkCousins(root,p,q):
    #Implement Your Code Here
    levelp = getLevel(root, p)
    levelq = getLevel(root, q)
    #print(levelq, levelp)

    if levelp != levelq:
        return False
    else:
        return not isSibling(root, p, q)
'''
def getParentAndLevel(root, val, parent = None, level = 1 ):
    if root == None:
        return 
    if root.data == val:
        return parent, level

    childparent, childlevel = getParentAndLevel(root.left, val, root, level)
    if childlevel != 0:
        childlevel += 1
        return childparent, childlevel
    else:
        childparent, childlevel = getParentAndLevel(root.right, val, root, level)
        if childlevel != 0:
            childlevel += 1
            return childparent, childlevel
    return parent, level

def checkCousins(root, p, q):
    parentp, levelp = getParentAndLevel(root, p)
    parentq, levelq = getParentAndLevel(root, q)
    print('p', parentp.data)
    print('q', parentq.data)
    if levelp == levelq and parentq != parentp:
        return True
    else:
        return False


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
p = int(input())
q = int(input())
ans = checkCousins(root,p,q)
if ans is True:
    print('true')
else:
    print('false')
