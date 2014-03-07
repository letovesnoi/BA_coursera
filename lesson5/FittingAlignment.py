__author__ = 'lenk'

back = {}

def GA(v, w):
    global back
    s = {}
    s[0, 0] = 0
    for i in range(1, len(v)):
        s[i, 0] = s[i - 1, 0]
    for j in range(1, len(w)):
        s[0, j] = s[0, j - 1] - 1
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            s[i, j] = max(s[i - 1, j] - 1, s[i, j - 1] - 1)
            if v[i] == w[j]:
                s[i, j] = max(s[i, j], s[i - 1, j - 1] + 1)
            else:
                s[i, j] = max(s[i, j], s[i - 1, j - 1] - 1)

            if s[i, j] == s[i, j - 1] - 1:
                back[i, j] = (i, j - 1)
            elif s[i, j] == s[i - 1, j] - 1:
                back[i, j] = (i - 1, j)
            elif s[i, j] == s[i - 1, j - 1] + 1 or s[i, j] == s[i - 1, j - 1] - 1:
                back[i, j] = (i - 1, j - 1)

    maxS = s[0, len(w) - 1]
    maxi = 0
    for i in range(1, len(v)):
        if s[i, len(w) - 1] > maxS:
            maxS = s[i, len(w) - 1]
            maxi = i
    ans = {}
    ans['score'] = s[maxi, len(w) - 1]
    ans['index'] = maxi
    return ans

def OUTPUTLCS(v, w, i, j):
    global back
    str1 = ''
    str2 = ''
    while j != 0:
        if back[i, j] == (i, j - 1):
            str1 += '-'
            str2 += w[j]
            j -= 1
        elif back[i, j] == (i - 1, j):
            str1 += v[i]
            str2 += '-'
            i -= 1
        elif back[i, j] == (i - 1, j - 1):
            str1 += v[i]
            str2 += w[j]
            i -= 1
            j -= 1

    newStr1 = ''
    newStr2 = ''
    for i in range(len(str1)):
        newStr1 += str1[len(str1) - i - 1]
        newStr2 += str2[len(str2) - i - 1]
    ans = {}
    ans['str1'] = newStr1
    ans['str2'] = newStr2
    return ans

def main():
    with open('inputFA.txt', 'r') as fin:
        v = '0' + fin.readline()[:-1]
        w = '9' + fin.readline()[:-1]
    g = GA(v, w)
    score = g['score']
    ind = g['index']
    outstr = OUTPUTLCS(v, w, ind, len(w) - 1)
    str1 = outstr['str1']
    str2 = outstr['str2']
    with open('outputFA.txt', 'w') as fout:
        fout.write(str(score) + '\r\n' + str1 + '\r\n' + str2)

main()