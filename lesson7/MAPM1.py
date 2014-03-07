__author__ = 'lenk'

import SuffixArray

def LastToFirst(FirstColumn, LastColumn):
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

def FirstOccurrence(FirstColumn):
    firstOccurence = {}
    symbols = ['$', 'A', 'C', 'G', 'T']
    for symbol in symbols:
        firstOccurence[symbol] = FirstColumn.find(symbol)

    return firstOccurence

def Count(LastColumn):
    symbols = ['$', 'A', 'C', 'G', 'T']
    count = {'$':[0], 'A':[0], 'C':[0], 'G':[0], 'T':[0]}
    for symbol in symbols:
        for j in LastColumn:
            if j == symbol:
                count[symbol].append(count[symbol][-1] + 1)
            else:
                count[symbol].append(count[symbol][-1])
    return count

def BWMATCHING(LastColumn, Pattern, FirstOccurrence, Count, d, lastToFirst):
    MM = {}
    for i in range(len(LastColumn)):
        MM[i] = 0
    keys = MM.keys()
    top = 0
    bottom = len(LastColumn) - 1
    while top <= bottom:
        if Pattern != '':
            symbol = Pattern[-1:]
            Pattern = Pattern[:-1]
            currentMM = {}
            for i in range(len(LastColumn[top:bottom + 1])):
                if LastColumn[i + top] != symbol:
                    currentMM[lastToFirst[i + top]] = MM[keys[i]] + 1
                    if currentMM[lastToFirst[i + top]] > d:
                        del currentMM[lastToFirst[i + top]]
                else:
                    currentMM[lastToFirst[i + top]] = MM[keys[i]]
            MM = currentMM.copy()
            keys = MM.keys()
            top = MM.keys()[0]
            bottom = MM.keys()[-1]
        else:
            return 0
    return top, bottom

def main():
    with open('inputMAPM.txt', 'r') as fin:
        Text = fin.readline()[:-1] + '$'
        Patterns = fin.readline()[:-1].split(' ')
        d = int(fin.readline())

    suffixArray = SuffixArray.sort_bucket(Text, (i for i in range(len(Text))), 1)

    LastColumn = ''
    for i in range(len(suffixArray)):
        LastColumn += Text[suffixArray[i] - 1]

    FirstColumnList = []
    for i in range(len(LastColumn)):
        FirstColumnList.append(LastColumn[i])
    FirstColumnList.sort()
    FirstColumn=''
    for i in range(len(FirstColumnList)):
        FirstColumn += FirstColumnList[i]

    firstOccurrence = FirstOccurrence(FirstColumn)
    count = Count(LastColumn)
    lastToFirst= LastToFirst(FirstColumn, LastColumn)

    ans = []
    for i in range(len(Patterns)):
        pair = BWMATCHING(LastColumn, Patterns[i], firstOccurrence, count, d, lastToFirst)
        #for key in MM.keys():
        #    ans.append(suffixArray[key])
        if pair != 0:
            ans.extend(suffixArray[pair[0]:pair[1]])
    ans.sort()

    with open('outputMAPM.txt', 'w') as fout:
        for i in range(len(ans)):
            fout.write(str(ans[i]) + ' ')

main()