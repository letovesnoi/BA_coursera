__author__ = 'lenk'

def FromSource(score, v, w, middle):
    ans = {}
    sigma = 5
    s = {}
    s[0, 0] = 5
    for i in range(1, middle + 1):
        s[i, 0] = s[i - 1, 0] - sigma
    for j in range(1, len(w)):
        s[0, j] = s[0, j - 1] - sigma
    for i in range(1, middle + 1):
        for j in range(1, len(w)):
            #if v[i] == w[j]:
            s[i, j] = max(s[i - 1, j] - sigma, s[i, j - 1] - sigma, s[i - 1, j - 1] + int(score[v[i], w[j]]))
            #else:
            #    s[i, j] = max(s[i - 1, j] - sigma, s[i, j - 1] - sigma)
        for j in range(1, len(w)):
            del s[i - 1, j]
    for j in range(len(w)):
        ans[j] = s[middle, j]
    return ans

def ToSink(score, v, w, middle):
    ans = {}
    newV = ''
    newW = ''
    for i in range(len(v)):
        newV += v[-i]
    for i in range(len(w)):
        newW += w[-i]
    temp = FromSource(score, newV, newW, len(newV) -1 - middle)
    for i in range(len(temp)):
        ans[i] = temp[len(temp) - i - 1]
    #print(ans)
    return ans

def MaxLength(fromSource, toSink):
    length = {}
    max = fromSource[0] + toSink[0]
    maxj = 0
    for j in range(1, len(fromSource)):
        length[j] = fromSource[j] + toSink[j]
        if length[j] > max:
            max = length[j]
            maxj = j
    return maxj

def main():
    global str1
    global str2
    str1 = ''
    str2 = ''
    with open('inputMA.txt', 'r') as fin:
        w = fin.readline()[:-1]
        v = fin.readline()[:-1]
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

    middle = (len(v) - 1) / 2
    fromSource = FromSource(score, v, w, middle)
    toSink = ToSink(score, v, w, middle)
    maxj = MaxLength(fromSource, toSink)

    maxjTemp = maxj + 1
    middle1 = middle + 1
    fromSource1 = FromSource(score, v, w, middle1)
    toSink1 = ToSink(score, v, w, middle1)
    maxj1 = MaxLength(fromSource1, toSink1)
    if fromSource[maxjTemp] + toSink[maxjTemp] > fromSource1[maxj1] + toSink1[maxj1]:
        maxj1 = maxjTemp
        middle1 = middle
    print '(' + str(maxj) + ', ' + str(middle) + ') (' + str(maxj1) + ', ' + str(middle1) + ')'

main()