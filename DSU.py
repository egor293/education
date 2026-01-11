n = 5

parent = list(range(n))
rank = [1] * n

def find(x):
    if parent[x] == x:
        return x
    
    else:
        parent[x] = x 
        return find(parent[x])

    
def union(x, y):
    nx = find(x)
    ny = find(y)
    if ny == nx:
        return
    
    

    elif rank[nx] == rank[ny]:
        rank[nx] += rank[ny]
        rank[ny] = 1
        parent[ny] = parent[nx]

        return
    
    else:
        if rank[nx] > rank[ny]:
            rank[nx] += rank[ny]
            rank[ny] = 1
            parent[ny] = parent[nx]
        
        elif rank[nx] < rank[ny]:
            rank[ny] += rank[nx]
            rank[nx] = 1
            parent[nx] = parent[ny]

        return


union(0, 1)
print(parent, rank)

union(1, 2)
print(parent, rank)

union(3, 4)
print(parent, rank)

print(find(0) == find(2)) 
print(find(0) == find(4)) 


class DSU:
    def __init__(self, n):
        self.parent = list(range(n)) # Каждый элемент - сам себе родитель
        self.rank = [0] * n # Для оптимизации union by rank

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i]) # Сжатие пути
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by rank
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True # Успешно объединены
        return False # Уже в одном множестве




# сверхъёлка
