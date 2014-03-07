def lcp(s, t):
    n = min(len(s), len(t))
    for i in range(n):
        if s[i] != t[i]:
            return s[:i]
    return s

def lrs(s):
    N = len(s)
    suffixes = []
    for i in range(N):
        suffixes.append(s[i:])

    suffixes.sort()

    lrstr = ""

    for i in range(N - 1):
        x = lcp(suffixes[i], suffixes[i + 1])
        if len(x) > len(lrstr):
            lrstr = x

    return lrstr

s = "my string"
print lrs(s)
