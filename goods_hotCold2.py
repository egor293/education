prices = [5,6,7,8,9,10,11,12,13,14,
15,16,17,18,19,20,21,22,23,24,
25,26,27,28,29,30,31,32,33,34]

sales = [205,192,180,170,158,149,141,133,122,115,
102,95,88,80,72,66,60,55,50,45,
40,37,33,30,27,24,22,20,18,16]

weight = -1 
step = 0.015
bias = 235.0
step_bias = 1.2

def neural_network(price, weight, bias):
    return price * weight + bias

def errorFunc(pred, target):
    return (pred - target) ** 2


for i in range(4000):
    total_error = 0
    for p, t in zip(prices, sales):
        total_error += (p * weight + bias - t) ** 2


        err_up   = sum((p * (weight + step)   + bias - t)**2 for p,t in zip(prices,sales))
        err_down = sum((p * (weight - step)   + bias - t)**2 for p,t in zip(prices,sales))

        if err_down < total_error and err_down < err_up:
            weight -= step
        elif err_up < total_error:
            weight += step


        err_up_b   = sum((p * weight + (bias + step_bias)   - t)**2 for p,t in zip(prices,sales))
        err_down_b = sum((p * weight + (bias - step_bias)   - t)**2 for p,t in zip(prices,sales))

        if err_down_b < total_error and err_down_b < err_up_b:
            bias -= step_bias
        elif err_up_b < total_error:
            bias += step_bias


        if i % 400 == 0:
            print(f"{i:4d} | err {total_error:9.1f} | w {weight:7.4f} | b {bias:7.1f}")

print(f"final weight: {round(weight, 3)}")

for i in range(len(prices)):
    pred1 = neural_network(prices[i], weight, bias)
    print(f"pred: {round(pred1, 3)}",
          f"target: {sales[i]}")