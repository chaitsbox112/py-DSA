# ADJACENCY MATRIX IN DIRECTED, UNDIRECTED, WEIGHTED, UNWEIGHTED
# Test cases for undirected graph
'''
7 9
A B
A C
A F
C E
C F
C D
D E
D G
G F
'''
# Test cases for weighted graph
'''
6 7
A B 4
A C 2
B C 5
B D 10
C E 3
D F 11
E D 4
'''
def printmatrix(matrix):
    r,c = len(matrix),len(matrix[0])
    print(r,c)
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end = " ")
        print()

def undigraph():
    v,e = map(int,input().split())
    matrix = [[0]*v for i in range(v)] # This would generate matrix of v^2
    for i in range(e):
        u,v = map(str,input().split())
        u = ord(u) - ord("A")
        v = ord(v) - ord("A")
        matrix[u][v] = 1 # True or False in case of edge
        matrix[v][u] = 1
    return matrix

def weightedgraph():
    v,e = map(int,input().split())
    matrix = [[0]*v for i in range(v)]
    for i in range(e):
        u,v,w = map(str,input().split())
        u = ord(u)-ord("A")
        v = ord(v)-ord("A")
        w = int(w)
        matrix[u][v] = w # cost or weight in case of edges
    return matrix
#undimatrix = undigraph()
#printmatrix(undimatrix)
weightmatrix = weightedgraph()
printmatrix(weightmatrix)