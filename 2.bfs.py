# 2.	Implement  Breadth First Search algorithm, Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure. 

from collections import deque

class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = {}

        # create empty list for each vertex
        for i in range(v):
            self.graph[i] = []

    # add edge (undirected)
    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    # bfs traversal
    def bfs(self, start):
        visited = [False] * self.v
        q = deque()

        visited[start] = True
        q.append(start)

        print("BFS Traversal:", end=" ")

        while q:
            node = q.popleft()
            print(node, end=" ")

            for neighbour in self.graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    q.append(neighbour)


# main part
g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

g.bfs(0)
