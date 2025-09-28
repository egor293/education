goods = {
    1500: (1, 'Гитара'),
    3000: (4, 'Магнитофон'),
    2500: (3, 'Ноутбук'),
    2000: (1, 'Телефон')
}

def greedy(values, capacity):
    backpack = []
    cost = sorted(goods.keys(), reverse=True)
    for i in cost:
        if goods[i][0] <= capacity:
            backpack.append(goods[i][1])
            capacity -= goods[i][0]
    return backpack

def dp(values, items, capacity):
    n = len(goods)
    # Создаем DP таблицу
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Создаем таблицу для отслеживания выбранных предметов
    selected = [[False for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        weight_i = items[i - 1][0]
        value_i = values[i - 1]
        
        for w in range(capacity + 1):
            if weight_i <= w:
                if dp_table[i - 1][w - weight_i] + value_i > dp_table[i - 1][w]:
                    dp_table[i][w] = dp_table[i - 1][w - weight_i] + value_i
                    selected[i][w] = True
                else:
                    dp_table[i][w] = dp_table[i - 1][w]
            else:
                dp_table[i][w] = dp_table[i - 1][w]
    
    # Восстанавливаем выбранные предметы
    backpack = []
    w = capacity
    for i in range(n, 0, -1):
        if selected[i][w]:
            backpack.append(items[i - 1][1])  # Добавляем название предмета
            w -= items[i - 1][0]  # Уменьшаем оставшуюся вместимость
    
    return dp_table[n][capacity], backpack, dp_table

# Альтернативная версия с более простым восстановлением предметов
def dp_simple(values, items, capacity):
    n = len(goods)
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        weight_i = items[i - 1][0]
        value_i = values[i - 1]
        
        for w in range(capacity + 1):
            if weight_i <= w:
                dp_table[i][w] = max(dp_table[i - 1][w], 
                                   dp_table[i - 1][w - weight_i] + value_i)
            else:
                dp_table[i][w] = dp_table[i - 1][w]
    
    # Восстанавливаем предметы
    backpack = []
    w = capacity
    for i in range(n, 0, -1):
        if dp_table[i][w] != dp_table[i - 1][w]:
            backpack.append(items[i - 1][1])
            w -= items[i - 1][0]
    
    return dp_table[n][capacity], backpack

greedy_res = greedy(goods, 4)
dp_value, dp_backpack = dp_simple(list(goods.keys()), list(goods.values()), 4)

print(f'Greedy: {greedy_res}')
print(f'DP: стоимость = {dp_value}, предметы = {dp_backpack}')