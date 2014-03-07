__author__ = 'lenk'

def overlap(Pattern):
    list = {}
    k = len(Pattern[0])
    for read in Pattern:
        list[read] = []
        for neighbor in Pattern:
            if read[1:k] == neighbor[:k - 1]:
                list[read].append(neighbor)
    return list

Pattern = []
with open('inputOverlap.txt', 'r') as fin:
    while fin:
        Pattern.append(fin.readline()[:-1])
        if Pattern[-1] == '':
            Pattern = Pattern[:-1]
            break
graphOverlap = overlap(Pattern)
print(graphOverlap)

with open('outputOverlap.txt', 'w') as fout:
    for kmer in graphOverlap:
        for i in range(len(graphOverlap[kmer])):
            fout.write(kmer + ' -> ' + graphOverlap[kmer][i] + '\r\n')