#5.	 Implement Greedy search algorithm for Minimum Spanning Tree 

import heapq

class Graph:
    def __init__(self):
        # hardcoded graph (undirected with weights)
        self.graph = {
            0: [(1, 10), (2, 6), (3, 5)],
            1: [(0, 10), (3, 15)],
            2: [(0, 6), (3, 4)],
            3: [(0, 5), (1, 15), (2, 4)]
        }

    def prim_mst(self, start=0):
        visited = set()
        min_heap = [(0, start)]   # (weight, node)

        total_cost = 0

        print("Edges in MST:")

        while min_heap:
            weight, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            total_cost += weight

            print(f"Node {node} included with cost {weight}")

            for neighbor, w in self.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor))

        print("Total cost of MST:", total_cost)


# -------- main --------
g = Graph()
g.prim_mst(0)
