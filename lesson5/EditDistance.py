__author__ = 'lenk'

back = {}

def GA(v, w):
    global back
    s = {}
    s[0, 0] = 0
    for i in range(1, len(v)):
        s[i, 0] = s[i - 1, 0] - 1
    for j in range(1, len(w)):
        s[0, j] = s[0, j - 1] - 1
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            s[i, j] = max(s[i - 1, j] - 1, s[i, j - 1] - 1)
            if v[i] == w[j]:
                s[i, j] = max(s[i, j], s[i - 1, j - 1])
            else:
                s[i, j] = max(s[i, j], s[i - 1, j - 1] - 1)
            if s[i, j] == s[i, j - 1] - 1:
                back[i, j] = 0
            elif s[i, j] == s[i - 1, j] - 1:
                back[i, j] = 1
            elif s[i, j] == s[i - 1, j - 1] and v[i] == w[j]:
                back[i, j] = 2
            elif s[i, j] == s[i - 1, j - 1] - 1 and v[i] != w[j]:
                back[i, j] = 3
    return s[len(v) - 1, len(w) - 1]

def main():
    global str1
    global str2
    str1 = ''
    str2 = ''
    with open('inputED.txt', 'r') as fin:
        v = fin.readline()[:-1]
        w = fin.readline()[:-1]
    s = GA(v, w)
    print -1 * s

main()