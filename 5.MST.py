#5.	 Implement Greedy search algorithm for Minimum Spanning Tree 

import heapq

class Graph:
    def __init__(self):
        # graph stored as adjacency list (node: [(neighbor, weight)])
        self.g = {
            0: [(1, 10), (2, 6), (3, 5)],
            1: [(0, 10), (3, 15)],
            2: [(0, 6), (3, 4)],
            3: [(0, 5), (1, 15), (2, 4)]
        }

    def prim(self):
        visited = []
        heap = [(0, 0)]   # (weight, node)
        cost = 0

        print("MST:")

        while heap:
            w, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.append(node)
            cost += w

            print(node, "-> cost:", w)

            for nbr, wt in self.g[node]:
                if nbr not in visited:
                    heapq.heappush(heap, (wt, nbr))

        print("Total cost:", cost)


# main
g = Graph()
g.prim()
