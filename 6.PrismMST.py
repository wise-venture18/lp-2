#6.	  Implement Greedy search algorithm for Prim's Minimal Spanning Tree Algorithm 

import heapq

def prim_mst(graph):
    start = list(graph.keys())[0]   # start from any node
    visited = set([start])
    min_heap = []

    # add edges of starting node
    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))

    mst = []
    total_cost = 0

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_cost += weight

            # add new edges
            for neighbor, w in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, v, neighbor))

    return mst, total_cost


# Example graph
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

mst, cost = prim_mst(graph)

print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(u, "-", v, ":", w)

print("Total Cost:", cost)
