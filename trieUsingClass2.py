class Trie():
    trie = {}
    def insert_(self, word):
        subtrie = self.trie
        for ch in word:
            if ch not in subtrie.keys():
                subtrie[ch] = {}
            subtrie = subtrie[ch]
        subtrie['#'] = None            
                        
    def search_(self, word):
        answer = []
        subtrie = self.trie
        for ch in word:
            if ch in subtrie.keys():
                subtrie = subtrie[ch]
            else:
                return False
            
        if '#' in subtrie.keys():
            return True
        return False

    def prefix_search(self, prefix):

        def find_prefix_node(trie, prefix):
            subtrie = trie
            for ch in prefix:
                if ch in subtrie.keys():
                    subtrie = subtrie[ch]
                else:
                    return False
            return subtrie 
        
        def collect_words(node, prefix, result):
            if '#' in node:
                result.append(prefix)
            for i in node:
                if i == '#':
                    continue
                collect_words(node[i], prefix + i, result)
            return result

        node = find_prefix_node(self.trie, prefix)
        if not node:  
            return []
        collected_words = collect_words(node, prefix, [])
        return collected_words
    
    def remove_(self, word):
        current = self.trie
        stack = []
        for ch in word:
            if ch not in current:
                return
            stack.append((current, ch))
            current = current[ch]
        if '#' not in current:
            return
        # Remove the word marker
        del current['#']
        # Now, we traverse back up the trie
        while stack:
            parent, ch = stack.pop()
            # Current is the node we were at (which we just removed the '#' from, or the node we just cleaned up)
            # But note: in the first iteration of the while loop, `current` is the node at the end of the word (without the '#')
            # We check if `current` is empty
            if not current:   # if current is an empty dict
                # Then we remove the key `ch` from the parent
                del parent[ch]
            else:
                # If current is not empty, then we break because we don't want to remove nodes that are still in use
                break
            # Move current to the parent (because we are going up)
            current = parent
                 

trie_obj = Trie()
trie_obj.insert_('dog')
trie_obj.insert_('dogdfd')
print(trie_obj.trie)
print(trie_obj.search_('dog'))
print(trie_obj.search_('dogdf'))
print(trie_obj.prefix_search('do'))
print(trie_obj.prefix_search('dodfas')) 
    