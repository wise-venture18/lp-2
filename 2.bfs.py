# 2.	Implement  Breadth First Search algorithm, Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure. 

from collections import deque   # used to create a queue

class Graph:
    def __init__(self, v):
        self.v = v              # total number of vertices
        self.graph = {}

        # create empty adjacency list for each vertex
        for i in range(v):
            self.graph[i] = []

    # function to add edge (undirected graph)
    def add_edge(self, a, b):
        self.graph[a].append(b)   # add b to a's list
        self.graph[b].append(a)   # add a to b's list

    # BFS traversal function
    def bfs(self, start):
        visited = [False] * self.v   # mark all nodes as not visited
        q = deque()                  # create an empty queue

        visited[start] = True        # mark starting node as visited
        q.append(start)              # add it to queue

        print("BFS Traversal:", end=" ")

        # loop until queue becomes empty
        while q:
            node = q.popleft()       # remove first element from queue
            print(node, end=" ")     # print the node

            # check all neighbours of current node
            for neighbour in self.graph[node]:
                if not visited[neighbour]:     # if not visited
                    visited[neighbour] = True  # mark as visited
                    q.append(neighbour)       # add to queue


# -------- main program --------
g = Graph(5)

# adding edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

# start BFS from node 0
g.bfs(0)
