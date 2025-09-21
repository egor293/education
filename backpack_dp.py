goods = {
    1500: (1, 'Гитара'),
    3000: (4, 'Магнитофон'),
    2500: (3, 'Ноутбук'),
    2000: (1, 'Телефон')
}

def greedy(values, capacity):
    backpack = []
    cost = sorted(goods.keys(),reverse=True)
    for i in cost:
        if goods[i][0] <= capacity:
            backpack.append(goods[i][1])
            capacity -= goods[i][0]
            del i
    return backpack
        

def dp(values, items, capacity):
    print(values, items)
    n = len(goods)
    dp = [[0 for _ in range(capacity + 1)]for _ in range(n + 1)]
    print(dp)
    backpack = []
    for i in range(1, n + 1):
        for w in range(capacity):
            if items[i - 1][0] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][items[i - 1][0]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    for j in range(1, n):
        if dp[j][w] == values[j - 1]:
            backpack.append(goods[values[j - 1]][1])
            print(backpack)
        else:
            backpack.append(goods[dp[j][w] - values[j - 1]][1])
    return dp[i][w], dp, backpack


greedy_res = greedy(goods, 4)
dp_res = dp(list(goods.keys()), list(goods.values()), 4)
print(f'Greedy: {greedy_res}')
print(f'Dp: {dp_res}')
# def dp(values, items, capacity):
#     print(values, items)
#     n = len(goods)
#     dp = [[0 for _ in range(capacity + 1)]for _ in range(n + 1)]
#     print(dp)
#     backpack = []
#     for i in range(1, n + 1):
#         for w in range(capacity):
#             if items[i - 1][0] <= w:
#                 if dp[i - 1][w] > dp[i - 1][items[i - 1][0]] + (values[i - 1]):
#                     dp[i][w] = dp[i - 1][w]

#                 dp[i][w] = max(dp[i - 1][w], dp[i - 1][items[i - 1][0]] + (values[i - 1]))
#             else:
#                 dp[i][w] = dp[i - 1][w]
    
#     return dp[i][w], dp, backpack