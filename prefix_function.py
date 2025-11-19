def prefix_sw(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        substring = s[:i+1]

        # Try lengths from largest to smallest
        for k in range(i, 0, -1):
            # prefix = s[:k], suffix = last k chars of substring
            if substring.startswith(s[:k]) and substring.endswith(s[:k]):
                p[i] = k
                break

    return p

print(prefix_sw('ABABAC'))
