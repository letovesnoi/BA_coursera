__author__ = 'lenk'

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
                return bottom - top + 1

def main():
    countList = []
    with open('dataset_101_6 (3).txt', 'r') as fin:
        LastColumn = fin.readline()[:-1]
        Patterns = fin.readline().split(' ')
    FirstColumnList = []
    for i in range(len(LastColumn)):
        FirstColumnList.append(LastColumn[i])
    FirstColumnList.sort()
    FirstColumn=''
    for i in range(len(FirstColumnList)):
        FirstColumn += FirstColumnList[i]

    firstOccurence = FirstOccurrence(FirstColumn)
    count = Count(LastColumn)
    for i in range(len(Patterns)):
        countList.append(BWMATCHING(LastColumn, Patterns[i], firstOccurence, count))

    with open('outputBWM.txt', 'w') as fout:
        for i in range(len(countList)):
            fout.write(str(countList[i]) + ' ')

main()