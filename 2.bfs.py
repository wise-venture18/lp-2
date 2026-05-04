# 2.	Implement  Breadth First Search algorithm, Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure. 

from collections import deque

class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = {}

        # create adjacency list
        for i in range(v):
            self.graph[i] = []

    # add edge (undirected)
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # recursive BFS function
    def bfs_recursive(self, queue, visited):
        if not queue:
            return

        node = queue.popleft()
        print(node, end=" ")

        # visit neighbours
        for nbr in self.graph[node]:
            if not visited[nbr]:
                visited[nbr] = True
                queue.append(nbr)

        # recursive call
        self.bfs_recursive(queue, visited)

    # wrapper function
    def bfs(self, start):
        visited = [False] * self.v
        queue = deque()

        visited[start] = True
        queue.append(start)

        print("BFS Traversal:", end=" ")
        self.bfs_recursive(queue, visited)


# -------- main --------
g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

g.bfs(0)
