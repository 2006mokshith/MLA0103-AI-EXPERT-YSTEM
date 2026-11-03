
import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('F', 2)],
    'E': [('F', 1)],
    'F': []
}

h = {'A': 5, 'B': 4, 'C': 3,
     'D': 2, 'E': 1, 'F': 0}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {}

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node in best and best[node] <= cost:
            continue
        best[node] = cost

        if node == goal:
            return path, cost

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if (neighbor not in best or
                    new_cost < best[neighbor]):
                heapq.heappush(
                    pq,
                    (new_cost + h[neighbor],
                     new_cost, neighbor,
                     path + [neighbor])
                )

print("Path and Cost:", astar('A', 'F'))
