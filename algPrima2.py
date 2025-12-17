import heapq

def prim_mst(graph, n):
    # graph — список смежности: graph[u] = [(v, weight), ...]
    
    visited = [False] * n
    parent = [-1] * n   # родитель в MST
    key = [float('inf')] * n  # минимальный вес ребра до вершины
    key[0] = 0
    
    # min-heap: (вес, вершина)
    pq = [(0, 0)]  # (key, vertex)
    
    while pq:
        weight, u = heapq.heappop(pq)
        
        if visited[u]:
            continue  # пропускаем устаревшие записи
        
        visited[u] = True
        
        # перебираем всех соседей u
        for v, w in graph[u]:
            if not visited[v] and w < key[v]:
                key[v] = w
                parent[v] = u
                heapq.heappush(pq, (w, v))
    
    # Общий вес MST
    total_weight = sum(key)
    
    return parent, key, total_weight

# Твой граф
n = 4
graph = [
    [(1, 10), (2, 6)],          # 0
    [(0, 10), (2, 5), (3, 15)], # 1
    [(0, 6), (1, 5), (3, 4)],   # 2
    [(1, 15), (2, 4)]           # 3
]

parent, key, total_weight = prim_mst(graph, n)

print("Parent:", parent)      # например: [-1, 2, 0, 2]
print("Key:    ", key)        # [0, 5, 6, 4]
print("Общий вес MST:", total_weight)  # 15
