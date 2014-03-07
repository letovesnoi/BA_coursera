__author__ = 'lenk'

'''MOTIFENUMERATION(Dna, k, d)
        for each k-mer a in Dna
            for each k-mer a’ differing from a by at most d mutations
                if a’ appears in each string from Dna with at most d mutations
                    output a’'''
alphabet = ["A", "C", "G", "T"]

def expand(listP):
    tempL = len(listP)
    for ip in range(tempL):
        for i in range(len(alphabet)):
            k = listP[ip][:]
            k.append(alphabet[i])
            listP.append(k)
    for ip in range(tempL):
        listP.pop(0)

def generateKmersMutate(kmers, d):
    outList = []
    k = len(kmers)
    listP = [["A"], ["C"], ["G"], ["T"]]
    for i in range(k - 1):
        expand(listP)
    for i in range(len(listP)):
        countM = 0
        for j in range(len(kmers)):
            if kmers[j] != listP[i][j]:
                countM += 1
        if countM <= d:
            outList.append(listP[i])
    return outList

def computePrefixF(P):
    m = len(P)
    pi = []
    pi.append(0)
    pi.append(0)
    k = -1
    for q in range(2, m + 1):
        while k > 0 and P[k + 1] != P[q - 1]:
            k = pi[k] - 1
        if P[k + 1] == P[q - 1]:
            k += 1
        pi.append(k + 1)
    return pi


def KMPMatcher(T, P):
    count = 0
    n = len(T)
    m = len(P)
    pi = computePrefixF(P)
    q = 0
    for i in range(0, n):
        while q > 0 and P[q] != T[i]:
            q = pi[q]
        if P[q] == T[i]:
            q += 1
        if q == m:
            count += 1
            return count
            #q = pi[q]
    return  0



def main():
    with open('inputME.txt', 'r') as f:
        k, d = f.readline().split()
        k, d = int(k), int(d)
        listDNA = f.readlines()
        for i in range(len(listDNA)):
            listDNA[i] = listDNA[i][:-1]
    f.close()
    kmers = []
    allKmersMutate = []
    for i in range(len(listDNA)):
        for j in range(len(listDNA[i]) - k + 1):
            kmers.append(listDNA[i][j:j + k])
    kmers = set(kmers)
    #for each k-mer a in Dna
    for a in kmers:
        kmersM = generateKmersMutate(a, d)
        #for each k-mer a’ differing from a by at most d mutations
        for i in range(len(kmersM)):
            strkmersM = ''
            for l in range(len(kmersM[i])):
                strkmersM = strkmersM + kmersM[i][l]
            kmersMM = generateKmersMutate(strkmersM, d)
            countF = 0
            #for each k-mer a'' differing from a' by at most d mutations
            for j in range(len(listDNA)):
                for l in range(len(kmersMM)):
                    strkmersMM = ''
                    for t in range(len(kmersMM[l])):
                        strkmersMM = strkmersMM + kmersMM[l][t]
                    countF1 = countF
                    countF = countF + KMPMatcher(listDNA[j], strkmersMM, countF)
                    if countF1 != countF:
                        #print('strkmersMM', strkmersMM, 'strkmersM', strkmersM, 'countF', countF, ' j', j)
                        break
            if countF == len(listDNA):
                #print(strkmersM)
                allKmersMutate.append(strkmersM)
    with open('outputME.txt', 'w') as f1:
        #f1.write(str(listDNA))
        #f1.write(str(kmers))
        f1.write(str(set(allKmersMutate)))
    f1.close()

main()
