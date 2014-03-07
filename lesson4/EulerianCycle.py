__author__ = 'lenk'

def EULERIANCYCLE(list):
    cycle = []
    tempcycle = []
    tempcircular = ''

    unused = list.copy()
    unvertex = []

    newStart = unused.keys()[0]
    currentStart = unused[newStart].keys()[0]

    cycle.append(newStart)
    circular = str(cycle[0][:-1])
    cycle.append(currentStart)
    circular += currentStart[:-1]

    if newStart not in unvertex:
        unvertex.append(newStart)
    if currentStart not in unvertex:
        unvertex.append(currentStart)

    unused[newStart][currentStart] -= 1
    if unused[newStart][currentStart] == 0:
        del unused[newStart][currentStart]
    if unused[newStart] == {}:
        del unused[newStart]
        unvertex.remove(newStart)

    while newStart != currentStart:
        i = unused[currentStart].keys()[0]

        unused[currentStart][i] -= 1
        if unused[currentStart][i] == 0:
            del unused[currentStart][i]
        if unused[currentStart] == {}:
            del unused[currentStart]
            unvertex.remove(currentStart)

        if (i in unused) and (i not in unvertex):
           unvertex.append(i)

        currentStart = i
        if newStart != currentStart:
            cycle.append(currentStart)
            circular += currentStart[:-1]
    tempcycle.append(currentStart)
    tempcircular += currentStart[-1]

    while len(unused) != 0:
        tempcycle = []
        tempcircular = ''

        newStart = unvertex[0]
        currentStart = unused[newStart].keys()[0]

        tempcycle.append(currentStart)
        tempcircular += currentStart[:-1]

        if newStart not in unvertex:
            unvertex.append(newStart)
        if currentStart not in unvertex:
            unvertex.append(currentStart)

        unused[newStart][currentStart] -= 1
        if unused[newStart][currentStart] == 0:
           del unused[newStart][currentStart]
        if unused[newStart] == {}:
            del unused[newStart]
            unvertex.remove(newStart)

        while newStart != currentStart:
            i = unused[currentStart].keys()[0]

            unused[currentStart][i] -= 1
            if unused[currentStart][i] == 0:
                del unused[currentStart][i]
            if unused[currentStart] == {}:
                del unused[currentStart]
                unvertex.remove(currentStart)

            if (i in unused) and (i not in unvertex):
                unvertex.append(i)

            currentStart = i
            tempcycle.append(currentStart)
            tempcircular += currentStart[:-1]
        #print(tempcycle)

        cycle = cycle[cycle.index(newStart):] + cycle[:cycle.index(newStart) + 1] + tempcycle[:-1]
        circular = circular[circular.index(newStart[-1:]):] + circular[:circular.index(newStart[-1:]) + 1]
    cycle += tempcycle[-1:]
    circular += tempcircular[-1:]
    return cycle
    #return circular

def readGraph():
    with open('inputEulerian.txt', 'r') as fin:
        list = {}
        while fin:
            temp = fin.readline().split(' ')
            if temp[0] == '':
                break
            temp[2] = temp[2][:-1]
            neighbor = temp[2].split(',')
            if temp[0] not in list:
                list[temp[0]] = {}
            for i in neighbor:
                if i not in list[temp[0]]:
                    list[temp[0]][i] = 1
                else:
                    list[temp[0]][i] += 1
    return list

def writeCycle(cycle):
    with open('outputEulerian.txt', 'w') as fout:
        for i in range(len(cycle)):
            fout.write(cycle[i])
            if i != len(cycle) - 1:
                fout.write('->')
        fout.write('\r\n')


def main():
    list = readGraph()
    cycle = EULERIANCYCLE(list)
    writeCycle(cycle)

main()