## Read input as specified in the question.
## Print output as specified in the question.
class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt
        
def getParent(src, parent):
    i = src
    while parent[i] != i:
        i = parent[i]
    return i

def kruskal(edges, n):
    parent = [i for i in range(n)]
    edges = sorted(edges, key = lambda edge: edge.wt)
    count = 0
    output = []
    i = 0
    while count < n-1 and i < len(edges):
        currEdge = edges[i]
        srcPar = getParent(currEdge.src, parent)
        destPar = getParent(currEdge.dest, parent)
        if srcPar != destPar:
            output.append(currEdge)
            parent[srcPar] = destPar
            count +=1
        i+=1
    return output
        
            
        
    
# main
V, E = [int(i) for i in input().split()]
edges= []
for i in range(E):
    src, dest, wt = [int(j) for j in input().split()]
    edge = Edge(src, dest, wt)
    edges.append(edge)
output = kruskal(edges, V)
for e in output:
    if e.src < e.dest:
        print(e.src, e.dest, e.wt, sep = " ")
    else:
        print(e.dest, e.src, e.wt, sep = " ")
    
