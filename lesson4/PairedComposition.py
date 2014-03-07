__author__ = 'lenk'

def pairedComposition(k, d, Text):
    list = []
    for i in range(len(Text) - 2 * k - d + 1):
        list.append(Text[i:i + k] + Text[i + k + d: i + 2 * k + d])
    list.sort()
    #print(list)
    return list

def main():
    with open('inputPaired.txt', 'r') as fin:
        k, d = fin.readline().split()
        k = int(k)
        d = int(d)
        Text = fin.readline()
    kdmers = pairedComposition(k, d, Text)
    with open('outputPaired.txt', 'w') as fout:
        for i in range(len(kdmers)):
            fout.write('(' + kdmers[i][:k] + '|' + kdmers[i][k:] + '), ')

main()