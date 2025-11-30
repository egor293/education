def build_trie(tmplts: list[str]):
    edges = [{} for i in range(sum(map(len, tmplts)))]
    output = []
    i = 1
    for k, tmp in enumerate(tmplts):
        for j, ch in enumerate(tmp):
            if ch not in edges[j]:    
                edges[j][ch] = i
            
            else:
                continue
            i += 1 
            output.append([])

        else:
            edges.append({})
            output.insert(j, k)
        
        
    return edges, output

print(build_trie(["ababac", "bababab", "ab", "bab"]))

