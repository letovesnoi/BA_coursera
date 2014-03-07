__author__ = 'lenk'

def BWTC(s):
    cyclicRotation = []
    for i in range(1, len(s) + 1):
        cyclicRotation.append(s[-i:] + s[:-i])
    cyclicRotation.sort()
    BWT = ''
    for string in cyclicRotation:
        BWT += string[-1]
    return BWT

def countLenRuns(BWT):
    i = 0
    count = 0
    while i + 1 < len(BWT):
        countG = 0
        while BWT[i] == BWT[i + 1] and i + 1 < len(BWT):
            i += 1
            countG += 1
        i += 1
        if countG >= 10:
            count += 1
    return count


def main():
    with open('inputBWT.txt', 'r') as fin:
        s = fin.readline()
    BWT = BWTC(s)
    with open('outputBWT.txt', 'w') as fout:
        fout.write(BWT)
    #print countLenRuns(BWT)

#main()