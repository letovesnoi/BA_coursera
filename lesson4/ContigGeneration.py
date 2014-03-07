__author__ = 'lenk'

import DeBruijnfromkmers

def contigs(list):
    countIN = {}
    countOUT = {}
    for i in list:
        for j in list[i]:
            if j not in countIN:
                countIN[j] = list[i][j]
            else:
                countIN[j] += list[i][j]
            if i not in countOUT:
                countOUT[i] = list[i][j]
            else:
                countOUT[i] += list[i][j]

    for i in countIN:
        if i not in countOUT:
            countOUT[i] = 0
    for i in countOUT:
        if i not in countIN:
            countIN[i] = 0

    tempCountIn = countIN.copy()
    tempCountOut = countOUT.copy()
    unvertex = list.keys()[:]

    cont = []
    while len(unvertex) != 0:
        newStart = unvertex[0]
        if list[newStart] == {}:
            break
        while countOUT[newStart] == 1 and countIN[newStart] == 1:
            if newStart in list and list[newStart].keys() != []:
                if newStart == list[newStart].keys()[0]:
                    cont.append(newStart + list[newStart].keys()[0][-1:])
                    unvertex.remove(newStart)
                    break
            unvertex.remove(newStart)
            newStart = unvertex[0]

        cont.append(newStart[:])
        currentStart = list[newStart].keys()[0]
        list[newStart][currentStart] -= 1

        tempCountIn[currentStart] -= 1

        tempCountOut[newStart] -= 1
        if tempCountOut[newStart] == 0:
            unvertex.remove(newStart)

        if list[newStart][currentStart] == 0:
           del list[newStart][currentStart]

        while countOUT[currentStart] == 1 and countIN[currentStart] == 1:
            i = list[currentStart].keys()[0]

            tempCountIn[i] -= 1
            tempCountOut[currentStart] -= 1

            list[currentStart][i] -= 1
            if list[currentStart][i] == 0:
                del list[currentStart][i]

            cont[-1] += currentStart[-1]
            if currentStart in unvertex and tempCountOut[currentStart] == 0 and tempCountIn[currentStart] == 0:
                unvertex.remove(currentStart)
            currentStart = i
            if currentStart in unvertex and tempCountOut[currentStart] == 0 and tempCountIn[currentStart] == 0:
                unvertex.remove(currentStart)
        cont[-1] += currentStart[-1:]

    cont.sort()
    return cont

def contigGeneration():
    list = DeBruijnfromkmers.deBruijnfromkmers()
    contig = contigs(list)

    with open('outputContigs.txt', 'w') as f:
        for i in contig:
            f.write(i + '\r\n')

#contigGeneration()