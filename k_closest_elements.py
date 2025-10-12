from math import sqrt
data = [
    [170, 65, 'Ж'],
    [180, 80, 'Ж'],
    [160, 50, 'Ж'],
    [155, 45, 'Ж']
]
new_data = [167, 55]

def KNN(data, new_data):
    distances = []
    closest = []
    for i in data:
        distances.append((sqrt((i[0] - new_data[0])**2 + (i[1] - new_data[1])**2), i[2]))
    distances.sort()

    for i in range(len(distances)- 1):
        closest.append(distances[i][1])

    if closest.count('М') >= 2:
        return 'М', distances
    return 'Ж', distances

print(KNN(data, new_data))






















# def recursion_numbers(n):
#     if n <= 0:
#         return
#     recursion_numbers(n - 1)
#     print(n)


# print(recursion_numbers(5))