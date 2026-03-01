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
    KDA = sum([input[0] * i for i in weights[0]])
    WR = sum([input[1] * i for i in weights[1]])
    GPM = sum([input[2] * i for i in weights[2]])
    return [KDA, WR, GPM]


step_amount = 0.01

for i in range(len(weights)):
    input, WR, GPM, WIN = data[i]
    goal_prediction = 3 if WIN else 2 

    for _ in range(100):
        weight = weights[0][i]
        prediction = weight * input
        error = (prediction - goal_prediction) ** 2

        up_prediction = input * (weight + step_amount)
        up_error = (goal_prediction - up_prediction) ** 2

        down_prediction = input * (weight - step_amount)
        down_error = (goal_prediction - down_prediction) ** 2

        if up_error > down_error:
            weights[0][i] = weight - step_amount
        else:
            weights[0][i] = weight + step_amount


for row in data:
    KDA, WR, GPM, WIN = row
    input = [KDA/5, WR, GPM/600]
    pred = neural_network(input, weights)
    goal = 3 if WIN else 2
    # print([round(i, 3) for i in pred])
    print(f"Предсказание: {pred[0]:.3f} (цель: {goal})")
    print("Факт:", WIN,
          "Предсказание:", "WIN" if pred[0] > 2.5 else "LOSE")