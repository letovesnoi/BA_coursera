__author__ = 'lenk'

def deBruijnGraph(k, read):
    list = {}
    for i in range(len(read) - k):
        if read[i:i + k] not in list:
            list[read[i:i + k]] = {}
        neighbor = read[i + 1:i + k + 1]
        if neighbor not in list[read[i:i + k]]:
            list[read[i:i + k]][neighbor] = 1
        else:
            list[read[i:i + k]][neighbor] += 1
    return list

with open('inputDeBruijn.txt', 'r') as fin:
    k = int(fin.readline())
    Text = fin.readline()
list = deBruijnGraph(k - 1, Text)

with open('outputDeBruijn.txt', 'w') as fout:
    for vertex in list:
        fout.write(vertex + ' -> ')
        for i in range(len(list[vertex].keys())):
            neighbour = list[vertex].keys()[i]
            fout.write(neighbour)
            if i != len(list[vertex].keys()) - 1:
                fout.write(',')
        fout.write('\r\n')