import sys
import queue


#main
sys.setrecursionlimit(10**6)
## Read input as specified in the question.
## Print output as specified in the question.
def heightOfTree(root):
    if root == None:
        return 0
    childHeight = 0
    for child in root.children:
        childHeight = max(childHeight, heightOfTree(child))
    return 1+ childHeight

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

task = [ int(x) for x in input().split()]
i = 0
root = TreeNode(task[i])
i+=1
q = queue.Queue()
q.put(root)
while not q.empty():
    curr = q.get()
    numNodes = task[i]
    i+=1
    for x in range(numNodes):
        node = TreeNode(task[i])
        q.put(node)
        curr.children.append(node)
        i+=1

print(heightOfTree(root))
