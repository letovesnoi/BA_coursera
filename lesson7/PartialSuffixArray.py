__author__ = 'lenk'

import SuffixArray

def main():
    with open('inputPSAC.txt', 'r') as fin:
        Text = fin.readline()
        K = int(fin.readline())
    suffixArray = SuffixArray.sort_bucket(Text, (i for i in range(len(Text))), 1)
    PSA = []
    for i in range(len(suffixArray)):
        if suffixArray[i] % K == 0:
            PSA.append((i - 1, suffixArray[i]))
    with open('outputPSAC.txt', 'w') as fout:
        for i in range(len(PSA)):
            fout.write(str(PSA[i][0]) + ',' + str(PSA[i][1]) + '\r\n')

main()