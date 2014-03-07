__author__ = 'lenk'

def composition(k, Text):
    list = []
    for i in range(len(Text) - k + 1):
        list.append(Text[i:i + k])
    list.sort()
    return list

def main():
    with open('inputCompositon.txt', 'r') as fin:
        k = int(fin.readline())
        Text = fin.readline()
    kmers = composition(k, Text)
    with open('outputCompositon.txt', 'w') as fout:
        for i in range(len(kmers)):
            fout.write(str(kmers[i]) + '\r\n')

#main()