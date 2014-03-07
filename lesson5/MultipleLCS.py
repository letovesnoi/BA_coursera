__author__ = 'lenk'

back = {}

def GA(v, w, u):
    global back
    s = {}
    for i in range(len(v)):
        for j in range(len(w)):
            for k in range(len(u)):
                s[i, j, k] = 0
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            for k in range(1, len(u)):
                if v[i] == w[j] and v[i] == u[k]:
                    s[i, j, k] = max(s[i - 1, j, k], s[i, j - 1, k], s[i, j, k - 1], s[i - 1, j - 1, k], s[i - 1, j, k - 1], s[i, j - 1, k - 1], s[i - 1, j - 1, k - 1] + 1)
                else:
                    s[i, j, k] = max(s[i - 1, j, k], s[i, j - 1, k], s[i, j, k - 1], s[i - 1, j - 1, k], s[i - 1, j, k - 1], s[i, j - 1, k - 1], s[i - 1, j - 1, k - 1])
                if s[i, j, k] == s[i - 1, j, k]:
                    back[i, j, k] = i - 1, j, k
                elif s[i, j, k] == s[i, j - 1, k]:
                    back[i, j, k] = i, j - 1, k
                elif s[i, j, k] == s[i, j, k - 1]:
                    back[i, j, k] = i, j, k - 1
                elif s[i, j, k] == s[i - 1, j - 1, k]:
                    back[i, j, k] = i - 1, j - 1, k
                elif s[i, j, k] == s[i - 1, j, k - 1]:
                    back[i, j, k] = i - 1, j, k - 1
                elif s[i, j, k] == s[i, j - 1, k - 1]:
                    back[i, j, k] = i, j - 1, k - 1
                elif s[i, j, k] == s[i - 1, j - 1, k - 1]:
                    back[i, j, k] = i - 1, j - 1, k - 1
                elif s[i, j, k] == s[i - 1, j - 1, k - 1] + 1:
                    back[i, j, k] = i - 1, j - 1, k - 1

    return s[len(v) - 1, len(w) - 1, len(u) - 1]

def OUTPUTLCS(v, w, u, i, j, k):
    global back
    global str1
    global str2
    global str3

    if i == 0 and j != 0 and k != 0:
        while j != 0 or k != 0:
            str1 += '-'
            str2 += w[j]
            str3 += u[k]
            j -= 1
            k -= 1
    if i != 0 and j == 0 and k != 0:
        while i != 0 or k != 0:
            str1 += v[i]
            str2 += '-'
            str3 += u[k]
            i -= 1
            k -= 1
    if i != 0 and j != 0 and k == 0:
        while i != 0 or j != 0:
            str1 += v[i]
            str2 += w[j]
            str3 += '-'
            i -= 1
            j -= 1
    if i == 0 or j == 0 or k == 0:
        while i != 0:
            str1 += v[i]
            str2 += '-'
            str3 += '-'
            i -= 1
        while j != 0:
            str1 += '-'
            str2 += w[j]
            str3 += '-'
            j -= 1
        while k != 0:
            str1 += '-'
            str2 += '-'
            str3 += u[k]
            k -= 1

    if i == 0 and j == 0 and k == 0:
        return 0

    if back[i, j, k] == (i - 1, j, k):
        OUTPUTLCS(v, w, u, i - 1, j, k)
        str1 += v[i]
        str2 += '-'
        str3 += '-'
    elif back[i, j, k] == (i, j - 1, k):
        OUTPUTLCS(v, w, u, i, j - 1, k)
        str1 += '-'
        str2 += w[j]
        str3 += '-'
    elif back[i, j, k] == (i, j, k - 1):
        OUTPUTLCS(v, w, u, i, j, k - 1)
        str1 += '-'
        str2 += '-'
        str3 += u[k]
    elif back[i, j, k] == (i - 1, j - 1, k):
        OUTPUTLCS(v, w, u, i - 1, j - 1, k)
        str1 += v[i]
        str2 += w[j]
        str3 += '-'
    elif back[i, j, k] == (i - 1, j, k - 1):
        OUTPUTLCS(v, w, u, i - 1, j, k - 1)
        str1 += v[i]
        str2 += '-'
        str3 += u[k]
    elif back[i, j, k] == (i, j - 1, k - 1):
        OUTPUTLCS(v, w, u, i, j - 1, k - 1)
        str1 += '-'
        str2 += w[j]
        str3 += u[k]
    elif back[i, j, k] == (i - 1, j - 1, k - 1):
        OUTPUTLCS(v, w, u, i - 1, j - 1, k - 1)
        str1 += v[i]
        str2 += w[j]
        str3 += u[k]

def main():
    global str1
    global str2
    global str3
    str1 = ''
    str2 = ''
    str3 = ''
    with open('inputMLCS.txt', 'r') as fin:
        v = fin.readline()[:-1]
        w = fin.readline()[:-1]
        u = fin.readline()[:-1]

    s = GA(v, w, u)
    OUTPUTLCS(v, w, u, len(v) - 1, len(w) - 1, len(u) - 1)

    with open('outputMLCS.txt', 'w') as fout:
        fout.write(str(s) + '\r\n')
        fout.write(str1 + '\r\n')
        fout.write(str2 + '\r\n')
        fout.write(str3)

main()