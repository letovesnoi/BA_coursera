from numpy.distutils.fcompiler.g95 import G95FCompiler

__author__ = 'lenk'

import GREEDYMOTIFSEARCHpseudocounts
#import Profile
import random

def RANDOMIZEDMOTIFSEARCH(Dna, k, t, BestMotifs):
    import Profile
    random.seed()
    Randoms = []
    for i in range(t):
        Randoms.append(random.randint(0, len(listDNA[0]) - k))
    Motifs = []
    for i in range(t):
        Motifs.append(listDNA[i][Randoms[i]:Randoms[i] + k])
    score = GREEDYMOTIFSEARCHpseudocounts.Score(GREEDYMOTIFSEARCHpseudocounts.formProfile(Motifs)[0], Motifs,
                                                GREEDYMOTIFSEARCHpseudocounts.formProfile(Motifs)[1])
    #print(score)
    while True:
        mProfile = GREEDYMOTIFSEARCHpseudocounts.formProfile(Motifs)[0]
        Motifs = []
        for i in range(len(Dna)):
            Motifs.append(Profile.MostProbablyKmer(Dna[i], k, mProfile))
        if GREEDYMOTIFSEARCHpseudocounts.Score(GREEDYMOTIFSEARCHpseudocounts.formProfile(Motifs)[0], Motifs,
                                               GREEDYMOTIFSEARCHpseudocounts.formProfile(Motifs)[1]) < \
                GREEDYMOTIFSEARCHpseudocounts.Score(GREEDYMOTIFSEARCHpseudocounts.formProfile(BestMotifs)[0], BestMotifs,
                                                    GREEDYMOTIFSEARCHpseudocounts.formProfile(BestMotifs)[1]):
            BestMotifs = Motifs[:]
            score = GREEDYMOTIFSEARCHpseudocounts.Score(GREEDYMOTIFSEARCHpseudocounts.formProfile(Motifs)[0], Motifs,
                                                        GREEDYMOTIFSEARCHpseudocounts.formProfile(Motifs)[1])
            print(score)
        else:
            print(BestMotifs)
            return BestMotifs


with open('inputRMS.txt', 'r') as f:
    k, t = f.readline().split()
    k = int(k)
    t = int(t)
    listDNA = []
    for i in range(t):
        listDNA.append(f.readline())
        listDNA[i] = listDNA[i][:-1]
f.close()
with open('outputRMS.txt', 'w') as f1:
    flag = 0
    random.seed()
    Randoms = []
    for i in range(t):
        Randoms.append(random.randint(0, len(listDNA[0]) - k))
    Motifs = []
    for i in range(t):
        Motifs.append(listDNA[i][Randoms[i]:Randoms[i] + k])
    Best = Motifs[:]
    for i in range(1000):
        Best = RANDOMIZEDMOTIFSEARCH(listDNA, k, t, Best)
    for i in range(len(Best)):
        f1.write(str(Best[i]) + '\r\n')
f1.close()
