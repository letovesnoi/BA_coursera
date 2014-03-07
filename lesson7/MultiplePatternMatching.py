__author__ = 'lenk'

import SuffixArray
import BWTC
import BWMATCHING

def FirstOccurrence(FirstColumn):
    firstOccurence = {}
    symbols = ['$', 'A', 'C', 'G', 'T']
    for symbol in symbols:
        firstOccurence[symbol] = FirstColumn.find(symbol)
    return firstOccurence

def Count(LastColumn, C):
    symbols = ['$', 'A', 'C', 'G', 'T']
    count = {'$':[0], 'A':[0], 'C':[0], 'G':[0], 'T':[0]}
    for symbol in symbols:
        tempCount = 0
        for i in range(1, len(LastColumn) + 1):
            j = LastColumn[i - 1]
            if j == symbol:
                tempCount += 1
            if (i) % C == 0:
                count[symbol].append(tempCount)
    return count

def checkPoint(index, symbol, LasTColumn, C):
    addCount = 0
    currentNI = index / C + 1
    begin = (currentNI - 1) * C
    end = index
    for i in range(begin, end, 1):
        if LasTColumn[i] == symbol:
            addCount += 1
    return addCount

def BWMATCHING(LastColumn, Pattern, FirstOccurrence, Count, C):
        top = 0
        bottom = len(LastColumn) - 1
        while top <= bottom:
            if Pattern != '':
                symbol = Pattern[-1:]
                Pattern = Pattern[:-1]
                if symbol in LastColumn[top:bottom + 1]:
                    temptop = top
                    tempbottom = bottom
                    top = FirstOccurrence[symbol] + Count[symbol][temptop / C]
                    addCount = checkPoint(temptop, symbol, LastColumn, C)
                    top += addCount
                    bottom = FirstOccurrence[symbol] + Count[symbol][(tempbottom + 1) / C] - 1
                    addCount = checkPoint(tempbottom + 1, symbol, LastColumn, C)
                    bottom += addCount
                else:
                    return 0
            else:
                return [top, bottom]

def main():
    C = 100
    with open('inputMPM.txt', 'r') as fin:
        Text = fin.readline()[:-1] + '$'
        Patterns = []
        for line in fin:
            Patterns.append(line[:-1])

    LastColumn = BWTC.BWTC(Text)
    FirstColumnList = []
    for i in range(len(LastColumn)):
        FirstColumnList.append(LastColumn[i])
    FirstColumnList.sort()
    FirstColumn=''
    for i in range(len(FirstColumnList)):
        FirstColumn += FirstColumnList[i]

    firstOccurence = FirstOccurrence(FirstColumn)
    count = Count(LastColumn, C)
    suffixArray = SuffixArray.sort_bucket(Text, (i for i in range(len(Text))), 1)

    ans = []
    for i in range(len(Patterns)):
        pair = BWMATCHING(LastColumn, Patterns[i], firstOccurence, count, C)
        if pair != 0:
            ans.extend(suffixArray[pair[0]:pair[1] + 1])
    ans.sort()

    with open('outputMPM.txt', 'w') as fout:
        for i in range(len(ans)):
            fout.write(str(ans[i]) + ' ')

main()