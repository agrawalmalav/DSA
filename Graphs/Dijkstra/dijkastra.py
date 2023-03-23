import sys
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMat = [[0 for i in range(nVertices)] for j in range(nVertices)]
    def addEdge(self, v1, v2, wt):
        self.adjMat[v1][v2] = wt
        self.adjMat[v2][v1] = wt
        return
    
    def checkEdge(self, v1, v2):
        return True if self.adjMat[v1][v2] != 0 else False
        
    def delEdge(self, v1, v2):
        if self.checkEdge( v1, v2):
            self.adjMat[v1][v2] = 0
            self.adjMat[v2][v1] = 0
        return
    
    def getMinVertex(self,weight, visited):
        minV =-1
        for i in range(self.nVertices):
            if (visited[i] == False and (minV == -1 or weight[minV] > weight[i])):
                 minV = i
        return minV
        
        
    def dijkstra(self):
        visited = [False for i in range(self.nVertices)]
        #parent = [-1 for i in range(self.nVertices)]
        dist = [sys.maxsize for i in range(self.nVertices)]
        dist[0] = 0
        
        for i in range(self.nVertices-1):
            min_V = self.getMinVertex(dist, visited)
            visited[min_V] = True
            for j in range(self.nVertices):
                if self.adjMat[min_V][j] >0 and visited[j] == False:
                    if dist[j] > dist[min_V] + self.adjMat[min_V][j]:
                        dist[j] = self.adjMat[min_V][j] + dist[min_V]
                        #parent[j] = min_V
        
        for i in range(self.nVertices):
            print(i, dist[i], sep= ' ')
            
                
    
    def __str__(self):
        return (str(self.adjMat))

V, E = [int(i) for i in input().split()]
g = Graph(V)
for i in range(E):
    src, dest, wt = [int(j) for j in input().split()]
    g.addEdge(src, dest, wt)
g.dijkstra()
    
