__author__ = 'lenk'

def LastToFirst(i, first, last):
    return first[last[i]]

def BWMATCHING(LastColumn, Pattern, first, last):
        top = 0
        bottom = len(LastColumn) - 1
        while top <= bottom:
            if Pattern != '':
                symbol = Pattern[-1:]
                Pattern = Pattern[:-1]
                if symbol in LastColumn[top:bottom + 1]:
                    topIndex = LastColumn[top:bottom + 1].find(symbol) + top
                    bottomIndex = LastColumn[top:bottom + 1].rfind(symbol) + top
                    top = LastToFirst(topIndex, first, last)
                    bottom = LastToFirst(bottomIndex, first, last)
                else:
                    return 0
            else:
                return bottom - top + 1

def main():
    countList = []
    with open('dataset_101_6 (4).txt', 'r') as fin:
        LastColumn = fin.readline()[:-1]
        Patterns = fin.readline().split(' ')
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

    for i in range(len(Patterns)):
        countList.append(BWMATCHING(LastColumn, Patterns[i], first, last))

    with open('outputBWM.txt', 'w') as fout:
        for i in range(len(countList)):
            fout.write(str(countList[i]) + ' ')

#main()