__author__ = 'lenk'

back = {}

def GA(score, v, w):
    global back
    s = {}
    s[0, 0] = 0
    for i in range(1, len(v)):
        s[i, 0] = s[i - 1, 0] - 5
    for j in range(1, len(w)):
        s[0, j] = s[0, j - 1] - 5
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            s[i, j] = max(s[i - 1, j] - 5, s[i, j - 1] - 5)
            s[i, j] = max(s[i, j], s[i - 1, j - 1] + int(score[v[i], w[j]]))
            if s[i, j] == s[i, j - 1] - 5:
                back[i, j] = 0
            elif s[i, j] == s[i - 1, j] - 5:
                back[i, j] = 1
            elif s[i, j] == s[i - 1, j - 1] + int(score[v[i], w[j]]) and v[i] == w[j]:
                back[i, j] = 2
            elif s[i, j] == s[i - 1, j - 1] + int(score[v[i], w[j]]) and v[i] != w[j]:
                back[i, j] = 3
    return s[len(v) - 1, len(w) - 1]

def OUTPUTLCS(v, w, i, j):
    global back
    global str1
    global str2
    if i == 0 or j == 0:
        if i == 0:
            while j > 0:
                str1 += '-'
                str2 += w[j]
                j -= 1
        if j == 0:
            while i > 0:
                str1 += v[i]
                str2 += '-'
                i -= 1
        return 0
    if back[i, j] == 0:
        OUTPUTLCS(v, w, i, j - 1)
        str1 += '-'
        str2 += w[j]
    elif back[i, j] == 1:
        OUTPUTLCS(v, w, i - 1, j)
        str1 += v[i]
        str2 += '-'
    else:
        OUTPUTLCS(v, w, i - 1, j - 1)
        str1 += v[i]
        str2 += w[j]

def main():
    global str1
    global str2
    str1 = ''
    str2 = ''
    with open('inputGA.txt', 'r') as fin:
        v = '0' + fin.readline()[:-1]
        w = '9' + fin.readline()[:-1]
    with open('BLOSUM62.txt', 'r') as ftable:
        acids = ftable.readline().split(' ')
        temp = acids[-1].split('\n')
        acids[-1] = temp[0]
        score = {}
        weight = []
        while True:
            tempW = ftable.readline().split(' ')
            if tempW[0] == '':
                break
            weight.append(tempW)
            temp = weight[-1][-1].split('\n')
            weight[-1][-1] = temp[0]
    for i in range(len(weight)):
        for j in range(len(weight[i])):
            score[acids[i], acids[j]] = weight[i][j]
    #print score
    s = GA(score, v, w)
    OUTPUTLCS(v, w, len(v) - 1, len(w) - 1)
    with open('outputGA.txt', 'w') as fout:
        fout.write(str(s) + '\r\n')
        fout.write(str1 + '\r\n')
        fout.write(str2)

main()