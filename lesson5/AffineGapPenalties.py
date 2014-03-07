__author__ = 'lenk'

back = {}

def GA(score, v, w):
    global back
    e = 1
    sigma = 11
    lower = {}
    middle = {}
    upper = {}

    lower[0, 0] = -1 * sigma
    upper[0, 0] = -1 * sigma
    middle[0, 0] = 0
    for i in range(1, len(v)):
        upper[i, 0] = upper[i - 1, 0] - e
        middle[i, 0] = upper[i, 0]
    for j in range(1, len(w)):
        lower[0, j] = lower[0, j - 1] - e
        middle[0, j] = lower[0, j]

    for i in range(1, len(v)):
        for j in range(1, len(w)):

            lower[i, j] = max(lower[i - 1, j] - e, middle[i - 1, j] - sigma)
            upper[i, j] = max(upper[i, j - 1] - e, middle[i, j - 1] - sigma)
            middle[i, j] = max(lower[i, j], middle[i - 1, j - 1] + int(score[v[i], w[j]]), upper[i, j])

            if middle[i, j] == middle[i - 1, j - 1] + int(score[v[i], w[j]]):
                back[i, j] = 2
            elif middle[i, j] == upper[i, j]:
                back[i, j] = 1
            elif middle[i, j] == lower[i, j]:
                back[i, j] = 0

    return middle[len(v) - 1, len(w) - 1]

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
    if back[i, j] == 1:
        OUTPUTLCS(v, w, i, j - 1)
        str1 += '-'
        str2 += w[j]
    elif back[i, j] == 0:
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
    with open('inputAGP.txt', 'r') as fin:
        v = fin.readline()[:-1]
        w = fin.readline()[:-1]
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
    print s
    OUTPUTLCS(v, w, len(v) - 1, len(w) - 1)
    with open('outputAGP.txt', 'w') as fout:
        fout.write(str(s) + '\r\n')
        fout.write(str1 + '\r\n')
        fout.write(str2)

main()