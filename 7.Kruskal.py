#7.	Implement Greedy search algorithm for Kruskal's Minimal Spanning Tree Algorithm 

# Kruskal's Algorithm (Simple Version)

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    parent[x] = y


def kruskal(vertices, edges):
    # Step 1: Sort edges by weight
    edges.sort()

    parent = [i for i in range(vertices)]

    mst = []
    total_cost = 0

    # Step 2: Pick edges one by one
    for w, u, v in edges:
        x = find(parent, u)
        y = find(parent, v)

        # Step 3: Check cycle
        if x != y:
            mst.append((u, v, w))
            total_cost += w
            union(parent, x, y)

    # Output
    print("Edges in MST:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)

    print("Total cost:", total_cost)


# Example Input
edges = [
    (10, 0, 1),
    (6, 0, 2),
    (5, 0, 3),
    (15, 1, 3),
    (4, 2, 3)
]

vertices = 4

kruskal(vertices, edges)
