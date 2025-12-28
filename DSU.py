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



# сверхъёлка