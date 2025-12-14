# import heapq
from collections import deque

def prim_mst(graph, n):
    graph.sort(key=lambda x: min([i[1] for i in x]))
    min_ = 0
    queue = deque((0, graph[0]))
    subgraph = {}
    visited = set()
    visited.add(0)

    while len(visited) != n:
        for node in deque:
            node1 = node[1]
            child = node1[0][0]
            length = node1[0][1]

            if child not in visited:
                subgraph[node[0]]
                deque[0].pop(0)
                deque.append((child, graph[child]))
                visited.add(child)
            else:
                continue
    return subgraph            
    

n = 4
graph = [
    [(1, 10), (2, 6)],      # вершина 0
    [(0, 10), (2, 5), (3, 15)],  # вершина 1
    [(0, 6), (1, 5), (3, 4)],    # вершина 2
    [(1, 15), (2, 4)]     # вершина 3
]
    
print(prim_mst(graph, n))    
# parent, key = prim_mst(graph, n)
# print("Parent:", parent)  # [0, 2, 0, 2]
# print("Key:", key)        # [0, 5, 6, 4]
# print("Общий вес MST:", sum(k for k in key if k != float('inf')))
