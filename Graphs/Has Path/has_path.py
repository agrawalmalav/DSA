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

    def checkPathHelper(self, v1, v2, visited):
        #visited[v1] = True
        if self.adjMat[v1][v2] >0:
            return True
        for i in range(self.nVertices):
            if self.adjMat[v1][i] >0 and visited[i] is False:
                visited[i] = True
                if self.checkPathHelper(i, v2, visited):
                    return True
        return False



    
    def checkPath(self, v1, v2):
        if v1 < self.nVertices and v2< self.nVertices:
            visited = [False for i in range(self.nVertices)]
            return self.checkPathHelper(v1, v2, visited)
        return False

    def bfs(self):
        if self.nVertices >0:
            visited = [False for i in range(self.nVertices)]
            q = queue.Queue()
            q.put(0)
            visited[0] = True
            while not q.empty():
                v= q.get()
                print(v, end= ' ')
                for i in range(self.nVertices):
                    if self.adjMat[v][i] >0 and visited[i] == False:
                        q.put(i)
                        visited[i] = True
            
            while False in visited:
                #print('elements left', visited)
                idx = visited.index(False)
                visited[idx] = True
                q.put(idx)
                while not q.empty():
                    v= q.get()
                    print(v, end= ' ')
                    for i in range(self.nVertices):
                        if self.adjMat[v][i] >0 and visited[i] == False:
                            q.put(i)
                            visited[i] = True


                
        return
        
    
    def __str__(self):
        return (str(self.adjMat))
        
        
# main
V, E = [int(i) for i  in input().split()]
g = Graph(V)
for l in range(E):
    v1, v2 = [int(i) for i in input().split()]
    g.addEdge(v1, v2)
v1, v2 = [int(i) for i in input().split()]
if g.checkPath(v1, v2):
    print('true')
else:
    print('false')

    
