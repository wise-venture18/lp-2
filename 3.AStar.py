#3.	Implement A star Algorithm for any game search problem.

import heapq   # for priority queue

# heuristic function (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    # priority queue (min-heap)
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}   # to reconstruct path
    g_cost = {start: 0}

    while open_list:
        current = heapq.heappop(open_list)[1]

        # if goal reached
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        x, y = current

        # possible moves (up, down, left, right)
        neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost

                    f_cost = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(open_list, (f_cost, (nx, ny)))

                    came_from[(nx, ny)] = current

    return None


# -------- Example Grid (Game Map) --------
# 0 = free path, 1 = obstacle
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

path = astar(grid, start, goal)

print("Path found:", path)
