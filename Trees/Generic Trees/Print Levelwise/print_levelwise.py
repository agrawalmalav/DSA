import sys
import queue


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


def printLevelWiseTree(tree):
    q = queue.Queue()
    q.put(tree)
    while not q.empty():
        count = q.qsize()
        while (count >0):
            root = q.get()
            print(root.data, end=':')
            childString = ''
            for child in root.children:
                childString = childString + str(child.data) + ','
                q.put(child)
            count -= 1
            print( childString[:-1] )


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root


# Main
sys.setrecursionlimit(10**6)
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)
