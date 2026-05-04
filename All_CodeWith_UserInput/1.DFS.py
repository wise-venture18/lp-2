1.	Implement depth first search algorithm, Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure. 

class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = {i: [] for i in range(v)}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)  # undirected

    def dfs(self, node, visited):
        visited[node] = True
        print(node, end=" ")
        for nbr in self.graph[node]:
            if not visited[nbr]:
                self.dfs(nbr, visited)

    def dfs_full(self):
        visited = [False] * self.v
        print("DFS Traversal:", end=" ")
        for i in range(self.v):   # ensures all vertices are covered
            if not visited[i]:
                self.dfs(i, visited)


# -------- User Input --------
v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

g = Graph(v)

print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    g.add_edge(u, v)

# Run DFS
g.dfs_full()
