__author__ = 'lenk'
''' MEDIANSTRING(Dna, k)
        BestPattern ← AAA…AA
        for each k-mer Pattern from AAA…AA to TTT…TT
            if d(Pattern, Dna) < d(BestPattern, Dna)
                 BestPattern ← Pattern
        output BestPattern  '''

alphabet = ["A", "C", "G", "T"]

def expandkmers(k, listP):
    for i in range(k - 1):
        tempL = len(listP)
        for ip in range(tempL):
            for i in range(len(alphabet)):
                temp = listP[ip][:]
                temp.append(alphabet[i])
                listP.append(temp)
        for ip in range(tempL):
            listP.pop(0)
    return listP

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
            return 1
    return 0

def generateKmersMutate(kmers, d):
    outList = []
    k = len(kmers)
    listP = [["A"], ["C"], ["G"], ["T"]]
    expandkmers(k, listP)
    for i in range(len(listP)):
        countM = 0
        for j in range(len(kmers)):
            if kmers[j] != listP[i][j]:
                countM += 1
        if countM <= d:
            outList.append(listP[i])
    return outList

def dMin(strkmer, strDNA):
    '''min = 1
    while 1 == 1:
        listdMK = generateKmersMutate(strkmer, min)
        for i in range(len(listdMK)):
            if KMPMatcher(strDNA, listdMK[i]):
                return min
            else:
                min += 1'''
    d = []
    for i in range(len(strDNA) - len(strkmer) + 1):
        d.append(0)
    for i in range(len(strDNA) - len(strkmer) + 1):
        for j in range(len(strkmer)):
            if strkmer[j] != strDNA[i + j]:
                d[i] += 1
    min = d[0]
    for i in range(len(strDNA) - len(strkmer) + 1):
        if d[i] < min:
            min = d[i]
    return min

def d(strkmer, listDNA):
    ansH = 0
    for i in range(len(listDNA)):
        strDNA = ''
        for j in range(len(listDNA[i])):
            strDNA += listDNA[i][j]
        ansH += dMin(strkmer, strDNA)
    return ansH

def main():
    with open('inputMS.txt', 'r') as f:
        k = int(f.readline())
        listDNA = f.readlines()
        for i in range(len(listDNA)):
            listDNA[i] = listDNA[i][:-1]
    f.close()
    BestPattern = ''
    for i in range(k):
        BestPattern += 'A'
    listkmersPatterns = expandkmers(k, [['A'], ['C'], ['G'], ['T']])
    for i in range(len(listkmersPatterns)):
        strkmerPattern = ''
        for j in range(len(listkmersPatterns[i])):
            strkmerPattern += listkmersPatterns[i][j]
        if d(strkmerPattern, listDNA) <= d(BestPattern, listDNA):
                 BestPattern = strkmerPattern
    print(BestPattern)

main()