# DFS - STACK/RECURSION ==> PREORDER POSTORDER INORDER
# BFS - QUEUE/ITERATION ==> LEVEL ORDER TRAVERSAL
# Trees are also graphs that are acyclic and udirected

'''
V E
v = 7
E = 9
for every Edge
U V
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
from collections import deque
from collections import defaultdict

def bfs(graph,start,visited,path):
    queue = deque()
    queue.append(start)
    path.append(start)
    visited[start] = True
    while len(queue) != 0:
        tempnode = queue.popleft()
        for neighbour in graph[tempnode]:
            if visited[neighbour] == False:
                path.append(neighbour)
                queue.append(neighbour)
                visited[neighbour] = True
    return path          


v,e = map(int,input().split())
graph = defaultdict(list)
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)

start = "A"
path = []
visited = defaultdict(bool)
traversedpath = bfs(graph,start,visited,path)
print(traversedpath)
