__author__ = 'lenk'

edge = []
s = {}
sigma = 5

def LINEARSPACEALIGNMENT(v, w, score, top, bottom, left, right):
    global edge
    global sigma
    if top == bottom:
        temp = top
        temp1 = left
        for i in range(abs(right - left)):
            edge.append((temp, temp1))
            temp1 += 1
        if top == len(v) - 1:
            edge.append((len(v) - 1, len(w) - 1))
        return

    ans = middleEdge(v, w, score, top, bottom, left, right)
    ansB = ans['begin']
    iB = ansB['middle']
    jB = ansB['maxj']

    ansE = ans['end']
    iE = ansE['middle']
    jE = ansE['maxj']

    LINEARSPACEALIGNMENT(v, w, score, top, iB, left, jB)
    edge.append((iB, jB))

    newiB = iB
    newjB = jB

    if (jB == jE and iB + 1 == iE) or (jB + 1 == jE and iB + 1 == iE):
        newiB += 1
    if (jB + 1 == jE and iB == iE) or (jB + 1 == jE and iB + 1 == iE):
        newjB += 1
    iB = newiB
    jB = newjB

    LINEARSPACEALIGNMENT(v, w, score, iB, bottom, jB, right)

def middleEdge(v, w, score, top, bottom, left, right):
    ans = {}
    ansB = {}

    mV = '0' + v[top + 1:bottom + 1][:]
    mW = '9' + w[left + 1:right + 1][:]
    middle = (top + bottom) / 2
    fromSource = FromSource(score, mV, mW, middle, top)
    fromSource1 = fromSource['middle']
    fromSource2 = fromSource['middle+1']
    toSink = ToSink(score, mV, mW, middle, top)
    toSink1 = toSink['middle']
    toSink2 = toSink['middle+1']

    maxj1 = maxLength(fromSource1, toSink1)
    maxj2 = maxLength(fromSource2, toSink2)

    ansB['fromSource'] = fromSource1
    ansB['toSink'] = toSink1
    ansB['maxj'] = maxj1 + left
    ansB['middle'] = middle

    ansE = {}
    maxjTemp = ansB['maxj'] + 1 - left
    middle2 = middle + 1

    while maxj2 + left != ansB['maxj'] + 1 and maxj2 + left != ansB['maxj']:
        del fromSource2[maxj2]
        del toSink2[maxj2]
        maxj2 = maxLength(fromSource2, toSink2)
    if maxjTemp in ansB['fromSource']:
        if ansB['fromSource'][maxjTemp] + ansB['toSink'][maxjTemp] > fromSource2[maxj2] + toSink2[maxj2]:
            maxj2 = maxjTemp
            middle2 = ansB['middle']

    ansE['fromSource'] = fromSource2
    ansE['toSink'] = toSink2
    ansE['maxj'] = maxj2 + left
    ansE['middle'] = middle2

    ans['begin'] = ansB
    ans['end'] = ansE

    return ans

def FromSource(score, v, w, middle, top):
    global s
    global sigma
    ans = {}
    ans1 = {}
    ans2 = {}
    s[0, 0] = 0
    for i in range(1, middle + 2 - top):
        s[i, 0] = s[i - 1, 0] - sigma
    for j in range(1, len(w)):
        s[0, j] = s[0, j - 1] - sigma
    for i in range(1, middle + 2 - top):
        for j in range(1, len(w)):
            #if v[i] == w[j]:
            s[i, j] = max(s[i - 1, j] - sigma, s[i, j - 1] - sigma, s[i - 1, j - 1] + int(score[v[i], w[j]]))
            #else:
            #    s[i, j] = max(s[i - 1, j] - sigma, s[i, j - 1] - sigma)
        if i != middle - top + 1:
            for j in range(1, len(w)):
                del s[i - 1, j]

    for j in range(len(w)):
        ans1[j] = s[middle - top, j]
        ans2[j] = s[middle + 1 - top, j]

    ans['middle'] = ans1
    ans['middle+1'] = ans2
    return ans

def ToSink(score, v, w, middle, top):
    ans = {}
    newV = ''
    newW = ''
    for i in range(len(v)):
        newV += v[-i]
    for i in range(len(w)):
        newW += w[-i]
    if top == middle + 1:
        temp = FromSource(score, newV, newW, top - 1, top)
    else:
        temp = FromSource(score, newV, newW, len(newV) - 2 - middle + 2 * top, top)
    ans1 = temp['middle']
    ans2 = temp['middle+1']
    newAns1 = {}
    newAns2 = {}
    for i in range(len(ans1)):
        newAns1[i] = ans1[len(ans1) - i - 1]
        newAns2[i] = ans2[len(ans2) - i - 1]
    ans['middle'] = newAns2
    ans['middle+1'] = newAns1
    return ans

def maxLength(fromSource, toSink):
    length = {}
    max = fromSource[fromSource.keys()[0]] + toSink[toSink.keys()[0]]
    maxj = fromSource.keys()[0]
    for j in fromSource:
        length[j] = fromSource[j] + toSink[j]
        if length[j] > max:
            max = length[j]
            maxj = j
    return maxj

def OUTPUTLCS(v, w, edge, score):
    global str1
    global str2
    global maxScore
    global sigma
    str1 = ''
    str2 = ''
    maxScore = 0
    for i in range(len(edge) - 1):
        if edge[i][1] + 1 == edge[i + 1][1] and edge[i][0] == edge[i + 1][0]:
            str1 += w[edge[i + 1][1]]
            str2 += '-'
            maxScore -= sigma
        if edge[i][1] + 1 == edge[i + 1][1] and edge[i][0] + 1 == edge[i + 1][0]:
            str1 += w[edge[i + 1][1]]
            str2 += v[edge[i][0] + 1]
            maxScore += int(score[v[edge[i][0] + 1], w[edge[i + 1][1]]])
        if edge[i][1] == edge[i + 1][1] and edge[i][0] + 1 == edge[i + 1][0]:
            str1 += '-'
            str2 += v[edge[i + 1][0]]
            maxScore -= sigma

def main():
    global edge
    global str1
    global str2
    global maxScore
    with open('inputLSA.txt', 'r') as fin:
        w = '0' + fin.readline()[:-1]
        v = '9' + fin.readline()[:-1]
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
    LINEARSPACEALIGNMENT(v, w, score, 0, len(v) - 1, 0, len(w) - 1)
    OUTPUTLCS(v, w, edge, score)
    #print(edge)
    print(maxScore)
    with open('outputLSA.txt', 'w') as fout:
        fout.write(str(maxScore) + '\r\n')
        fout.write(str1 + '\r\n' + str2)

main()