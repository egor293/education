from collections import deque
def build_bor(words):
    bor = {}
    for word in words:
        cur_dict = bor
        for ch in word: 
            if ch not in cur_dict.keys():
                cur_dict[ch] = {}
            cur_dict = cur_dict[ch]

        bor['#'] = True
    return bor


def find_prefix_node(root, prefix):
    if prefix[0] not in root.keys():
        return {}
    else:
        node = root
        for i in prefix:
            if i not in node.keys():
                return {}
            else:
                node = node[i]
    return node

        

def collect_words(node, prefix, result):
    if '#' in node:
        result.append(prefix)

    for i in node:
        if i == '#':
            continue
        collect_words(node[i], prefix + i, result)

    return result

def autocomplete(root, prefix):
    result = []
    node = find_prefix_node(root, prefix)
    return collect_words(root, prefix, result)


words = ["cat", "car", "cartoon", "carbon", "dog", "door"]
bor = build_bor(words)
print(bor)
print(autocomplete(bor, "ca"))   # ['cat', 'car', 'cartoon', 'carbon']
print(autocomplete(bor, "do"))   # ['dog', 'door']
print(autocomplete(bor, "z"))    # []