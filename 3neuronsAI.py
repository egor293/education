weights = [
    [ 1.2,  1.8,  0.9],   # вероятность победы
    [-0.6, -0.4, -0.2],  # tilt
    [ 0.3,  1.5,  0.4]   # мораль
]


data = [
    [2.1, 0.48, 420, 0],
    [3.4, 0.61, 510, 1],
    [1.8, 0.42, 380, 0],
    [4.2, 0.73, 560, 1]
]

def neural_network(input, weights):
    kda = sum([input[0] * i for i in weights[0]])
    wr = sum([input[1] * i for i in weights[1]])
    gpm = sum([input[2] * i for i in weights[2]])
    return [kda, wr, gpm]

for row in data:
    KDA, WR, GPM, WIN = row
    input = [KDA/5, WR, GPM/600]
    pred = neural_network(input, weights)
    print([round(i, 3) for i in pred])
    print("Факт:", WIN,
          "Предсказание:", "WIN" if pred[0] > 2.5 else "LOSE")