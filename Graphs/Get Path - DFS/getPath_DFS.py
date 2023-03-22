# Write your code here
import queue
import sys
sys.setrecursionlimit(10**8)

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMat = [[0 for i in range(nVertices)] for j in range(nVertices)]
    def addEdge(self, v1, v2):
        self.adjMat[v1][v2] = 1
        self.adjMat[v2][v1] = 1
        return
    
    def checkEdge(self, v1, v2):
        return True if self.adjMat[v1][v2] != 0 else False
        
    def delEdge(self, v1, v2):
        if self.checkEdge( v1, v2):
            self.adjMat[v1][v2] = 0
            self.adjMat[v2][v1] = 0
        return

    def getPathDFS(self, v1, v2, visited):
        visited[v1] = True
        if v1 == v2:
            return [v2]

        for i in range(self.nVertices):
            if self.adjMat[v1][i] >0 and visited[i] == False:
                currPath = self.getPathDFS(i, v2, visited)
                if len(currPath) > 0:
                    currPath.append(v1)
                    return currPath
        return []

        
    
    def __str__(self):
        return (str(self.adjMat))
        
        
# main
V, E = [int(i) for i  in input().split()]
g = Graph(V)
for l in range(E):
    v1, v2 = [int(i) for i in input().split()]
    g.addEdge(v1, v2)
v1, v2 = [int(i) for i in input().split()]
visited = [False for i in range(V)]
path = g.getPathDFS(v1, v2, visited)
for x in path:
    print(x, end=' ')
