__author__ = 'lenk'

import SuffixArray
import BWMATCHING

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

def BWMATCHING(LastColumn, Pattern, FirstOccurrence, Count):
        top = 0
        bottom = len(LastColumn) - 1
        while top <= bottom:
            if Pattern != '':
                symbol = Pattern[-1:]
                Pattern = Pattern[:-1]
                if symbol in LastColumn[top:bottom + 1]:
                    top = FirstOccurrence[symbol] + Count[symbol][top]
                    bottom = FirstOccurrence[symbol] + Count[symbol][bottom + 1] - 1
                else:
                    return 0
            else:
                return [top, bottom]

def main():
    with open('dataset_104_6 (4).txt', 'r') as fin:
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

    firstOccurence = FirstOccurrence(FirstColumn)
    count = Count(LastColumn)

    reans = []
    for pattern in Patterns:
        tempreans = []
        for part in range(d + 1):
            ans = []
            pos = part * len(pattern) / (d + 1)
            l = len(pattern) / (d + 1)
            partPattern = pattern[pos:pos + l]
            if part == d:
                partPattern = pattern[pos:]
            pair = BWMATCHING(LastColumn, partPattern, firstOccurence, count)
            if pair != 0:
                ans.extend(suffixArray[pair[0]:pair[1] + 1])
            tempPattern = pattern[:]
            for m in ans:
                if m - pos + len(tempPattern) <= len(Text) and m - pos >= 0:
                    tempText = Text[m - pos:m - pos + len(tempPattern)]
                else:
                    break
                #   tempText = Text[m:] + Text[len(Text) - len(tempPattern):m]
                tempD = 0
                for i in range(len(tempPattern)):
                    if tempPattern[i] != tempText[i]:
                        tempD += 1
                    if tempD > d:
                        break
                if tempD <= d:
                    if m - pos not in tempreans:
                        tempreans.append(m - pos)
        reans.extend(tempreans)
    reans.sort()
    #print reans[:10]


    with open('outputMAPM.txt', 'w') as fout:
        for i in range(len(reans)):
            fout.write(str(reans[i]) + ' ')

main()