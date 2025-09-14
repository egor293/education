goods = {
    3000: (4,'Магнитофон'),
    2500: (3, 'Ноутбук'),
    1500: (1, 'Гитара'),
    2000 : (1, 'Телефон')
}

def greedy(goods, capacity):
    backpack = []
    cost = sorted(goods.keys(),reverse=True)
    for i in cost:
        if goods[i][0] <= capacity:
            backpack.append(goods[i][1])
            capacity -= goods[i][0]
            del i
    return backpack
        

def dp(goods, capacity):
    backpack = []
    cost = sorted(goods.keys(), reverse=True)
    for i in cost:
        for new_capacity in range(1, capacity + 1):
            if goods[i][0] <= new_capacity:
                if goods[cost[new_capacity-1]][0] + goods[i][0] <= new_capacity:
                    print(goods[i])
                    if goods[i][0] <= capacity:
                        backpack.append(goods[i][1]) 
                        capacity -= goods[i][0]

    return backpack

greedy_res = greedy(goods, 4)
dp_res = dp(goods, 4)
print(f'Greedy: {greedy_res}')
print(f'Dp: {dp_res}')
