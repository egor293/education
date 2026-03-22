prices = [5,6,7,8,9,10,11,12,13,14,
15,16,17,18,19,20,21,22,23,24,
25,26,27,28,29,30,31,32,33,34]

sales = [205,192,180,170,158,149,141,133,122,115,
102,95,88,80,72,66,60,55,50,45,
40,37,33,30,27,24,22,20,18,16]

weight = -6
step = 0.025
bias = 235
step_bias = 2

def neural_network(price, weight, bias):
    return (price * weight) + bias

def errorFunc(pred, target):
    return (pred - target) ** 2


for i in range(1000):
    total_error = 0
    for j in range(0, -len(prices), -1):
        price = prices[j]
        target_pred = sales[j]

        pred = neural_network(price, weight, bias)

        gradient = (pred - target_pred) * step
        weight -= gradient

        predBias = neural_network(price, weight, bias)
        errorBias = errorFunc(predBias, target_pred)

        gradient_bias = (predBias - target_pred) * step_bias
        bias -= gradient_bias
        
        total_error += errorBias
        

    if i % 100 == 0:
        print(f"total_error: {round(total_error, 3)}",
              f"weight: {round(weight, 3)}",
              f"bias: {round(bias, 3)}", sep="||")

print(f"final weight: {round(weight, 3)}")

for i in range(len(prices)):
    pred1 = neural_network(prices[i], weight, bias)
    print(f"pred: {round(pred1, 3)}",
          f"target: {sales[i]}")