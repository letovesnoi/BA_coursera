__author__ = 'lenk'

back = {}

def LCS(v, w):
    global back
    s = {}
    for i in range(len(v)):
        s[i, 0] = 0
    for j in range(len(w)):
        s[0, j] = 0
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            if v[i] == w[j]:
                s[i, j] = max(s[i - 1, j], s[i, j - 1], s[i - 1, j - 1] + 1)
                if s[i, j] == s[i - 1, j]:
                    back[i, j] = (i - 1, j)
                elif s[i, j] == s[i, j - 1]:
                    back[i, j] = (i, j - 1)
                else:
                    back[i, j] = (i - 1, j - 1)
            else:
                s[i, j] = max(s[i - 1, j], s[i, j - 1])
                if s[i, j] == s[i-1, j]:
                    back[i, j] = (i - 1, j)
                elif s[i, j] == s[i, j - 1]:
                    back[i, j] = (i, j - 1)

def OUTPUTLCS(v, i, j):
    global back
    global str
    temp = ''
    while i != 0 and j != 0:
        if back[i, j] == (i, j - 1):
            j -= 1
        elif back[i, j] == (i - 1, j):
            i -= 1
        elif back[i, j] == (i - 1, j - 1):
            temp += v[i]
            i -= 1
            j -= 1
    for i in range(len(temp)):
        str += temp[len(temp) - i - 1]
    '''if i == 0 or j == 0:
        return 0
    if back[i, j] == 0:
        OUTPUTLCS(v, i, j - 1)
    elif back[i, j] == 1:
        OUTPUTLCS(v, i - 1, j)
    else:
        OUTPUTLCS(v, i - 1, j - 1)
        str += v[i]'''

def main():
    global str
    global back
    str = ''
    with open('inputLCS.txt', 'r') as fin:
        v = fin.readline()[:-1]
        w = fin.readline()[:-1]
    LCS(v, w)
    OUTPUTLCS(v, len(v) - 1, len(w) - 1)
    with open('outputLCS.txt', 'w') as fout:
        fout.write(str)
    print str
main()
