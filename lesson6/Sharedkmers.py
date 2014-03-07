__author__ = 'lenk'

dict = {}

def reverseComplement(kmer):
    rckmer = ''
    for i in range(len(kmer) - 1, -1, -1):
        if kmer[i] == 'A':
            rckmer += 'T'
        if kmer[i] == 'C':
            rckmer += 'G'
        if kmer[i] == 'G':
            rckmer += 'C'
        if kmer[i] == 'T':
            rckmer += 'A'
    return rckmer

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


def KMPMatcher(T, P, j):
    global dict
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
            if P not in dict:
                dict[P] = []
            dict[P].append((j, i - m + 1))
            q = pi[q]

def findSharedkmers(k, genome1, genome2):
    global dict
    for i in range(len(genome1) - k + 1):
        kmer1 = genome1[i: i + k]
        if kmer1 not in dict and reverseComplement(kmer1) not in dict:
            KMPMatcher(genome2, kmer1, i)
            KMPMatcher(genome2, reverseComplement(kmer1), i)
        else:
            temp = []
            for pair in dict[kmer1]:
                temp.append((i, pair[1]))
            dict[kmer1].extend(temp)
    return dict

def funct(genome1, genome2, k):
    dict1 = {}
    dict2 = {}
    for i in range(len(genome1) - k + 1):
        kmer = genome1[i:i + k]
        if kmer not in dict1:
            dict1[kmer] = []
        dict1[kmer].append(i)
        rckmer = reverseComplement(kmer)
        if rckmer not in dict1:
            dict1[rckmer] = []
        dict1[rckmer].append(i)
    for i in range(len(genome2) - k + 1):
        kmer = genome2[i:i + k]
        if kmer not in dict2:
            dict2[kmer] = []
        dict2[kmer].append(i)
        rckmer = reverseComplement(kmer)
        if rckmer not in dict2:
            dict2[rckmer] = []
        dict2[rckmer].append(i)

    list = []
    for kmer in dict1:
        for i in range(len(dict1[kmer])):
            if kmer in dict2:
                for j in range(len(dict2[kmer])):
                    if (dict1[kmer][i], dict2[kmer][j]) not in list:
                        list.append((dict1[kmer][i], dict2[kmer][j]))
    return list


def main():
    with open('inputSK.txt', 'r') as fin:
        k = fin.readline()[:-1]
        k = int(k)
        genome1 = fin.readline()[:-1]
        genome2 = fin.readline()[:-1]
        ans = funct(genome1, genome2, k)
        with open('outputSK.txt', 'w') as fout:
            for pair in ans:
                fout.write(str(pair) + '\r\n')

main()
