__author__ = 'lenk'

def IBWTC(last):
    lastList= []
    firstList = []
    lastCount = {'$': 1, 'A' : 1, 'C' : 1, 'G' : 1, 'T' : 1}
    for i in range(len(last)):
        lastList.append((last[i], lastCount[last[i]]))
        lastCount[last[i]] += 1
    first = []
    for i in range(len(last)):
        first.append(last[i])
    first.sort()
    firstCount = {'$': 1, 'A' : 1, 'C' : 1, 'G' : 1, 'T' : 1}
    for i in range(len(first)):
        firstList.append((first[i], firstCount[first[i]]))
        firstCount[first[i]] += 1

    print(lastList)
    print(firstList)

    #dictFL = {}
    dictLF = {}
    for i in range(len(last)):
        #dictFL[firstList[i]] = lastList[i]
        dictLF[lastList[i]] = firstList[i]

    currentF = firstList[0]
    i = 1
    IBWT = ''
    while i <= len(last):
        IBWT += dictLF[currentF][0]
        currentF = dictLF[currentF]
        i += 1
    return IBWT

def main():
    with open('inputIBWT.txt', 'r') as fin:
        last = fin.readline()
    IBWT = IBWTC(last)
    with open('outputIBWT.txt', 'w') as fout:
        fout.write(IBWT)

main()