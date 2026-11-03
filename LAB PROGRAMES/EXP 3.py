
import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('F', 2)],
    'E': [('F', 1)],
    'F': []
}

def ucs(start, goal):
    pq = [(0, start, [start])]
    best = {}

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in best and best[node] <= cost:
            continue
        best[node] = cost

        if node == goal:
            return path, cost

        for neighbor, weight in graph[node]:
            heapq.heappush(
                pq, (cost + weight, neighbor,
                     path + [neighbor])
            )

print("Path and Cost:", ucs('A', 'F'))
