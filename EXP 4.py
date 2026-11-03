
import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

h = {'A': 5, 'B': 4, 'C': 2,
     'D': 3, 'E': 1, 'F': 0}

def best_first(start, goal):
    pq = [(h[start], start, [start])]
    visited = set()

    while pq:
        _, node, path = heapq.heappop(pq)

        if node == goal:
            return path

        if node in visited:
            continue
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    pq, (h[neighbor], neighbor,
                         path + [neighbor])
                )

print("Path:", best_first('A', 'F'))
