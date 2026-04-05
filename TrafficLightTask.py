import numpy as np
trafficLights = np.array([
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1],
    [1, 1, 1],
    [0, 1, 1],
    [1, 0, 0]
])

results = [0, 1, 0, 1, 1, 0]

weights = np.array([0.5, 0.5, 0.5])
step = 0.1

def errorFunc(pred, target):
    return (pred - target) ** 2



for j in range(1000):
    total_error = 0

    for i, light in enumerate(trafficLights):
        target_pred = results[i]

        for l in range(len(light)):
            pred = weights.dot(light)
            gradient = (pred - target_pred) * step
            weights[l] -= gradient

    if j % 100 == 0:
        print(total_error, [round(float(i), 3) for i in list(weights)])

print(round(np.array([0, 1, 0]).dot(weights)))


