goods = {
    1500: (1, 'Гитара'),
    3000: (4, 'Магнитофон'),
    2500: (3, 'Ноутбук'),
    2000: (1, 'Телефон'),
    2500: (2, 'Телевизор'),
    1000: (1, 'Наушники')
}

ingots = [
    ('gold', 10, 600),
    ('silver', 20, 1000),
    ('bronze', 30, 900)
]


def greedy_parted(ingots, capacity):
    backpack = []
    ingots = sorted(ingots, key=2)
    print(ingots)






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
    n = len(goods)
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    backpack = []
    
    for i in range(1, n + 1):
        weight = items[i - 1][0]
        value = values[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                dp_table[i][w] = max(dp_table[i - 1][w], dp_table[i - 1][w - weight] + value)                     
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    w = capacity
    print(dp_table)
    for i in range(n, 0, -1):
        if dp_table[i][w] != dp_table[i - 1][w]:
            backpack.append(items[i - 1][1])
            w -= items[i - 1][0]
    
    return dp_table[n][capacity], backpack


parted_res = greedy_parted(ingots, 25)
greedy_res = greedy(goods, 4)
dp_res = dp(list(goods.keys()), list(goods.values()), 4)
print(f'Greedy: {greedy_res}')
print(f'Dp: {dp_res}')
print(f'Parted: {parted_res}')


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