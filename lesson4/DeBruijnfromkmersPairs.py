__author__ = 'lenk'

import EulerianPath

def deBruijnfromkmers():
    Patterns = readPatterns()
    k = len(Patterns[0][0])
    list = {}
    for edge in Patterns:
        if str([edge[0][:k - 1], edge[1][:k - 1]]) not in list:
            list[edge[0][:k - 1], edge[1][:k - 1]] = {}
        if str([edge[0][1:], edge[1][1:]]) not in list[edge[0][:k - 1], edge[1][:k - 1]]:
            list[edge[0][:k - 1], edge[1][:k - 1]][edge[0][1:], edge[1][1:]] = 1
        else:
            list[edge[0][:k - 1], edge[1][:k - 1]][edge[0][1:], edge[1][1:]] += 1
    return list

def readPatterns():
    global d
    with open('inputReadPairs.txt', 'r') as fin:
        d = int(fin.readline())
        Patterns = []
        while fin:
            Patterns.append(fin.readline()[:-1].split('|'))
            if Patterns[-1] == ['']:
                Patterns = Patterns[:-1]
                break
    return Patterns

def writePathPairs(path):
    global d
    k = len(path[0][0]) + 1
    genome1 = path[0][0][:-1]
    genome2 = path[0][1][:-1]
    for i in path:
        genome1 += i[0][-1:]
        genome2 += i[1][-1:]
    genome = genome1[:] + genome2[-k - d:]
    with open('outputReadPairs.txt', 'w') as fout:
        fout.write(genome)

def main():
    list = deBruijnfromkmers()
    path = EulerianPath.EULERIANPATH(list)
    #print(path)
    writePathPairs(path)

main()