class TrieNode:
    def __init__(self):
        self.children = {}
        self.pattern_index = -1 # Индекс шаблона, если узел - конец шаблона
        self.suffix_link = None # Суффиксная ссылка
        self.output_link = None # Выходная ссылка

def build_trie(patterns):
    root = TrieNode()
    for i, pattern in enumerate(patterns):
        node = root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.pattern_index = i # Помечаем конец шаблона
    return root
