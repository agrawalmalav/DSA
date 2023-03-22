import sys
sys.setrecursionlimit(10**6)

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
    
    def dfsHelper(self, sv, visited):
        #print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if (self.adjMat[sv][i] >0 and visited[i] == False):
                self.dfsHelper(i, visited)
        
                
        
    def checkConnected(self):
        visited = [False for i in range(self.nVertices)]
        self.dfsHelper(0, visited)
        #print(visited)
        return not False in visited
        
    
    def __str__(self):
        return (str(self.adjMat))

# main
V, E = [int(i) for i in input().split()]
if V >0:
    g = Graph(V)
    for i in range(E):
        v1, v2 = [int(i) for i in input().split()]
        g.addEdge(v1, v2)
    if g.checkConnected():
        print('true')
    else:
        print('false')
else:
    print('true')

