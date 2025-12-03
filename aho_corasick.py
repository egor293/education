def build_trie(patterns: list[str]):
    # edges[u][ch] = v — из узла u по символу ch переход в v
    edges = [{} ]  # edges[0] — корень
    # output[u] — список номеров шаблонов, которые заканчиваются в узле u
    output = [[]]
    
    node_cnt = 1  # следующий свободный номер узла
    
    for pat_id, pat in enumerate(patterns):
        u = 0  # начинаем с корня
        for ch in pat:
            if ch not in edges[u]:
                # создаём новый узел
                edges[u][ch] = node_cnt
                edges.append({})      # новый словарь переходов
                output.append([])     # новый список выводов
                node_cnt += 1
            u = edges[u][ch]  # переходим дальше
        # по окончании шаблона записываем его номер в output
        output[u].append(pat_id)
    
    return edges, output, node_cnt


# Тест
edges, output, total_nodes = build_trie(["ababac", "bababab", "ab", "bab"])
print("Всего узлов:", total_nodes)
print("edges:", [dict(e) for e in edges])  # для красивого вывода
print("output:", output)