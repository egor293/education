def build_trie(patterns: list[str]):
    edges = [{}]  
    output = [[]]
    nodes = 1 
    
    for ptI, pt in enumerate(patterns):
        i = 0  
        for ch in pt:
            if ch not in edges[i]:
                edges[i][ch] = nodes
                edges.append({})      
                output.append([])     
                nodes += 1
            i = edges[i][ch]  
        output[i].append(ptI)
    
    return edges, output


edges, output = build_trie(["ababac", "bababab", "ab", "bab"])
print("edges:", edges)  
print("output:", output)
