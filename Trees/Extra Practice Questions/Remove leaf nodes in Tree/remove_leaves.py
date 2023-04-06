## Read input as specified in the question.
## Print output as specified in the question.
import queue 
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def removeLeafNodes(root):
    #Implement Your Code Here
    #print(len(root.children), root.data)
    if root == None:
        return None
    if len(root.children) == 0:
        root = None
        return root

    for child in reversed(root.children):
        if removeLeafNodes(child) == None:
            root.children.remove(child)
            child = None
    return root

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

def printLevelWiseTree(root):
    q = queue.Queue()
    q.put(root)
    q.put(None)
    
    while q.empty() is False:
        front = q.get()
        if front is None:
            if q.empty():
                return
            else:
                print()
                q.put(None)
        else:
            print(front.data,end= ' ')
            for child in front.children:
                q.put(child)
            
        
    
    
# Main
arr = list(int(x) for x in input().strip().split(' '))
root = createLevelWiseTree(arr)
removeLeafNodes(root)
printLevelWiseTree(root)
