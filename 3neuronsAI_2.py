weights = [
    [ 1.4,  1.8,  0.9],   # вероятность победы
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
    KDA = sum(input[k] * weights[0][k] for k in range(3))
    WR = sum(input[k] * weights[1][k] for k in range(3))
    GPM = sum(input[k] * weights[2][k] for k in range(3))
    return [KDA, WR, GPM]


step_amount = 0.01

for i in range(3):
    KDA, WR, GPM, WIN = data[i]
    input = [KDA/5, WR, GPM/600]
    goal_prediction = 2.5 if WIN else 1.5

    for _ in range(100):
        pred = neural_network(input, weights)
        error = (pred[0] - goal_prediction) ** 2

        weights[0][i] += step_amount
        up_prediction = neural_network(input, weights)[0]
        up_error = (up_prediction - goal_prediction) ** 2

        weights[0][i] -= 2 * step_amount  
        down_prediction = neural_network(input, weights)[0]
        down_error = (down_prediction - goal_prediction) ** 2

        weights[0][i] += step_amount

        if up_error > down_error:
            weights[0][i] -= step_amount
        if up_error < down_error:
            weights[0][i] += step_amount


for row in data:
    KDA, WR, GPM, WIN = row
    input = [KDA/5, WR, GPM/600]
    pred = neural_network(input, weights)
    goal = 2.5 if WIN else 1.5
    # print([round(i, 3) for i in pred])
    print(f"Предсказание: {pred[0]:.3f} (цель: {goal})")
    print("Факт:", WIN,
          "Предсказание:", "WIN" if pred[0] > 2.5 else "LOSE")