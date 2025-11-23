def pr(word):
    p = [0] * len(word)
    for i in range(1, len(word)):
        substring = word[:i + 1]
        for j in range(i, 0, -1):
            if substring.startswith(word[:j]) and substring.endswith(word[:j]):
                p[i] = j
                break
    return p

def kmp_search(word, tmp):
    n = len(word)
    m = len(tmp)

    if m == 0:
        return 0
    
    i = 0
    j = 0
    prefix_res = pr(tmp)
    print(prefix_res)

    while i < n:

        if tmp[j] == word[i]:
            j += 1
            i += 1

            if j == len(tmp):
                return i - len(tmp)
            
        elif j > 0:
            j = prefix_res[j - 1]
            
        else:
            i += 1

    return -1

print(kmp_search("ABABABABAC", "ABABABAC"))