import numpy as np
from tabulate import tabulate

users = ["Анна", "Борис", "Виктор", "Дарья"]
movies = ["Матрица", "Пираты", "Начало", "Интерстеллар", "Форсаж"]
ratings = [
    np.array([5, 3, 4, 5, 2]),  # Анна
    np.array([4, 4, 5, 3, 5]),  # Борис
    np.array([2, 5, 3, 4, 4]),  # Виктор
    np.array([3, 2, 5, 5, 3]),  # Дарья
]

def dist(p1, p2):
    return int(p1.dot(p2))

matrix = [[] for i in range(len(ratings))]
for i, ratingI in enumerate(ratings):
    person = []

    for j, ratingJ in enumerate(ratings):
        person.append(f"{users[i]}: {dist(ratingI, ratingJ)}")

    else:
        person[i] = ""
        matrix[i] = person

print(tabulate(matrix, headers=users, tablefmt="grid", ))
print(matrix)

print("|||||||||||||")

person_ = np.array([0, 5, 5, 0, 0])

def recommend(person_):
    stats = [(dist(person_, rating), i) for i, rating in enumerate(ratings)]
    closest = max(stats, key=lambda x: x[0])[1]
    
    res = (0, 0)
    for i, rt in enumerate(ratings[closest]):
        if person_[i] == 0 and rt > res[0]:
            res = (rt, i)
    
    return movies[res[1]]

print(recommend(person_))
    