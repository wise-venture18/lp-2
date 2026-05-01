#1.	Implement depth first search algorithm, Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure. 

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

    # recursive DFS function
    def dfs(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        for nbr in self.graph[node]:
            if not visited[nbr]:
                self.dfs(nbr, visited)

    # helper function
    def dfs_traversal(self, start):
        visited = [False] * self.v
        print("DFS Traversal:", end=" ")
        self.dfs(start, visited)


# main part
g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

g.dfs_traversal(0)
