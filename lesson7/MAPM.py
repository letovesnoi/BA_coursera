__author__ = 'lenk'

import SuffixArray

def LastToFirst(LastColumn):
    FirstColumnList = []
    for i in range(len(LastColumn)):
        FirstColumnList.append(LastColumn[i])
    FirstColumnList.sort()
    FirstColumn=''
    for i in range(len(FirstColumnList)):
        FirstColumn += FirstColumnList[i]

    first = {}
    firstCount = {'$':1, 'A':1, 'C':1, 'G':1, 'T':1}
    for i in range(len(FirstColumn)):
        first[FirstColumn[i], firstCount[FirstColumn[i]]] = i
        firstCount[FirstColumn[i]] += 1

    last = {}
    lastCount = {'$':1, 'A':1, 'C':1, 'G':1, 'T':1}
    for i in range(len(LastColumn)):
        last[i] = (LastColumn[i], lastCount[LastColumn[i]])
        lastCount[LastColumn[i]] += 1

    lastToFirst = {}
    for i in range(len(last)):
        lastToFirst[i] = first[last[i]]

    return lastToFirst

def BWMATCHING(LastColumn, Pattern, d, lastToFirst):
    MM = {}
    for i in range(len(LastColumn)):
        MM[i] = 0
    while Pattern != '':
        symbol = Pattern[-1:]
        Pattern = Pattern[:-1]
        currentMM = {}
        for key in MM.keys():
            if LastColumn[key] != symbol:
                currentMM[lastToFirst[key]] = MM[key] + 1
                if currentMM[lastToFirst[key]] > d:
                    del currentMM[lastToFirst[key]]
            else:
                currentMM[lastToFirst[key]] = MM[key]
        MM = currentMM.copy()
    return MM

def main():
    with open('dataset_104_6.txt', 'r') as fin:
        Text = fin.readline()[:-1] + '$'
        Patterns = fin.readline()[:-1].split(' ')
        d = int(fin.readline())

    suffixArray = SuffixArray.sort_bucket(Text, (i for i in range(len(Text))), 1)
    LastColumn = ''
    for i in range(len(suffixArray)):
        LastColumn += Text[suffixArray[i] - 1]

    lastToFirst = LastToFirst(LastColumn)

    ans = []
    for i in range(len(Patterns)):
        MM = BWMATCHING(LastColumn, Patterns[i], d, lastToFirst)
        for key in MM.keys():
            ans.append(suffixArray[key])
    ans.sort()

    with open('outputMAPM.txt', 'w') as fout:
        for i in range(len(ans)):
            fout.write(str(ans[i]) + ' ')

main()