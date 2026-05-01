#6.	  Implement Greedy search algorithm for Prim's Minimal Spanning Tree Algorithm 
import heapq

class Graph:
    def __init__(self):
        # hardcoded weighted undirected graph
        self.g = {
            0: [(1, 10), (2, 6), (3, 5)],
            1: [(0, 10), (3, 15)],
            2: [(0, 6), (3, 4)],
            3: [(0, 5), (1, 15), (2, 4)]
        }

    def prim(self):
        visited = []              # list to store visited nodes
        heap = [(0, 0)]           # (weight, node)
        total_cost = 0

        print("Edges in MST:")

        while heap:
            w, node = heapq.heappop(heap)

            # skip if already visited
            if node in visited:
                continue

            visited.append(node)
            total_cost += w

            print(node, "-> cost:", w)

            # check all neighbours
            for nbr, wt in self.g[node]:
                if nbr not in visited:
                    heapq.heappush(heap, (wt, nbr))

        print("Total cost of MST:", total_cost)


# main
g = Graph()
g.prim()
