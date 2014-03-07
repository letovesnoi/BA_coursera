__author__ = 'lenk'

import GREEDYMOTIFSEARCHpseudocounts
import random
import Profile

def RANDOM(DNA, k, mProfile):
    m = []
    nm = []
    c = 0
    for i in range(len(DNA) - k + 1):
        m.append(Profile.countProbably(DNA, i, k, mProfile))
        c += m[-1]
    for i in range(len(DNA) - k + 1):
        m[i] /= c
    p = random.randint(0, 10e13 - 1)
    sum = -1
    i = 0
    while sum < p:
        sum += int(m[i] * 10e13)
        i += 1
    return i - 1

def GIBBSSAMPLER(Dna, k, t, N, BestMotifs):
    global scoreBM
    #random.seed()
    Randoms = []
    for i in range(t):
        Randoms.append(random.randint(0, len(listDNA[0]) - k))
    Motifs = []
    for i in range(t):
        Motifs.append(listDNA[i][Randoms[i]:Randoms[i] + k])
    for j in range(N):
        #random.seed()
        i = random.randint(0, t - 1)
        exceptMotifs = Motifs[:i]
        exceptMotifs.extend(Motifs[i + 1:])
        mProfile = GREEDYMOTIFSEARCHpseudocounts.formProfile(exceptMotifs)[0]
        #Motifs[i] = Profile.MostProbablyKmer(Dna[i], k, mProfile)
        l = RANDOM(listDNA[i], k, mProfile)
        Motifs[i] = Dna[i][l:l + k]
        listARG = GREEDYMOTIFSEARCHpseudocounts.formProfile(Motifs)[:]
        profileARG = listARG[0][:]
        allcountARG = listARG[1][:]
        scoreM = GREEDYMOTIFSEARCHpseudocounts.Score(profileARG, Motifs, allcountARG)
        if scoreM < scoreBM:
            BestMotifs = Motifs[:]
            scoreBM = scoreM
            print(scoreBM)
    return BestMotifs


with open('inputGS.txt', 'r') as f:
    k, t, N = f.readline().split()
    k = int(k)
    t = int(t)
    N = int(N)
    listDNA = []
    for i in range(t):
        listDNA.append(f.readline())
        listDNA[i] = listDNA[i][:-1]
f.close()
with open('outputGS.txt', 'w') as f1:
    flag = 0
    random.seed()
    Randoms = []
    for i in range(t):
        Randoms.append(random.randint(0, len(listDNA[0]) - k))
    Motifs = []
    for i in range(t):
        Motifs.append(listDNA[i][Randoms[i]:Randoms[i] + k])
    Best = Motifs[:]
    listARG = GREEDYMOTIFSEARCHpseudocounts.formProfile(Best)[:]
    profileARG = listARG[0][:]
    allcountARG = listARG[1][:]
    scoreBM = GREEDYMOTIFSEARCHpseudocounts.Score(profileARG, Best, allcountARG)
    for i in range(20):
        #random.seed()
        Best = GIBBSSAMPLER(listDNA, k, t, N, Best)
    for i in range(len(Best)):
        f1.write(str(Best[i]) + '\r\n')
f1.close()
