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

    def find_continuation(self, prefix):

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
        collected_words = collect_words(node, prefix, [])
        return collected_words
                
                    
            
                
            

trie_obj = Trie()
trie_obj.insert_('dog')
trie_obj.insert_('dogdfd')
print(trie_obj.trie)
print(trie_obj.search_('dog'))
print(trie_obj.search_('dogdf'))
# print(trie_obj.find_continuation('dodfas')) ! gives an error
    