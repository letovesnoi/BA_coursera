__author__ = 'lenk'

def deBruijnfromkmers(Patterns):
    #Patterns = readPatterns()
    k = len(Patterns[0])
    list = {}
    for edge in Patterns:
        if edge[:k - 1] not in list:
            list[edge[:k - 1]] = {}
        if edge[1:] not in list[edge[:k - 1]]:
            list[edge[:k - 1]][edge[1:]] = 1
        else:
            list[edge[:k - 1]][edge[1:]] += 1
    return list

def readPatterns():
    with open('inputDeBruijnkmers.txt', 'r') as fin:
        Patterns = []
        while fin:
            Patterns.append(fin.readline()[:-1])
            if Patterns[-1] == '':
                Patterns = Patterns[:-1]
                break
    return Patterns

def write(list):
    with open('outputDeBruijnkmers.txt', 'w') as fout:
        for vertex in list:
            fout.write(vertex + ' -> ')
            for i in range(len(list[vertex])):
                neighbour = list[vertex].keys()[i]
                for j in range(list[vertex][neighbour]):
                    fout.write(neighbour)
                    if i != len(list[vertex].keys()) - 1:
                        fout.write(',')
            fout.write('\r\n')

def main():
    list = deBruijnfromkmers()
    write(list)

#main()