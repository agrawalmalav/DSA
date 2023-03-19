import queue
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
        
    def __bfsHelper(self, visited, sv, q):
        
            q.put(sv)
            visited[sv] = True
            while not q.empty():
                v= q.get()
                print(v, end= ' ')
                for i in range(self.nVertices):
                    if self.adjMat[v][i] >0 and visited[i] == False:
                        q.put(i)
                        visited[i] = True

    def bfs(self):
        if self.nVertices >0:
            visited = [False for i in range(self.nVertices)]
            q = queue.Queue()
            for i in range(self.nVertices):
                if visited[i] is False:
                    self.__bfsHelper(visited, i, q)

                
        return
        
    
    def __str__(self):
        return (str(self.adjMat))
        
        
# main
V, E = [int(i) for i  in input().split()]
g = Graph(V)
for l in range(E):
    v1, v2 = [int(i) for i in input().split()]
    g.addEdge(v1, v2)
g.bfs()

    
