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

    def getComponentsHelper(self, v1, visited, path):
        path.append(v1)
        visited[v1] = True
        for i in range(self.nVertices):
            if self.adjMat[v1][i] != 0 and visited[i] == False:
                self.getComponentsHelper(i, visited, path)
        return

    def getComponents(self):
        ans = []
        visited = [False for i in range(self.nVertices)] 
        for j in range(self.nVertices):
            if visited[j] == False:
                path = []
                self.getComponentsHelper(j, visited, path)
                path.sort()
                ans.append(path)

        return ans
        
    
    def __str__(self):
        return (str(self.adjMat))
        
        
# main
V, E = [int(i) for i  in input().split()]
g = Graph(V)
for l in range(E):
    v1, v2 = [int(i) for i in input().split()]
    g.addEdge(v1, v2)
componentList = g.getComponents()
for component in componentList:
    for node in component:
        print(node, end= ' ')
    print()
