__author__ = 'lenk'

import Profile

def formProfile(Motifs):
    count = []
    Profile = []
    for i in range(len(Motifs[0])):
        Profile.append([])
        for j in range(4):
            Profile[i].append(0)
    for i in range(len(Motifs[0])):
        count.append([0, 0, 0, 0])
    for i in range(len(Motifs)):
        for j in range(len(Motifs[i])):
            if Motifs[i][j] == 'A':
                count[j][0] += 1
            if Motifs[i][j] == 'C':
                count[j][1] += 1
            if Motifs[i][j] == 'G':
                count[j][2] += 1
            if Motifs[i][j] == 'T':
                count[j][3] += 1
    for i in range(len(Motifs[0])):
        for j in range(4):
            Profile[i][j] = count[i][j] * 1.0 / len(Motifs)
    return Profile

def Score(Profile, Motifs):
    maxProbably = []
    Alphmax = []
    fmax = []
    for i in range(len(Motifs[0])):
        maxProbably.append(0)
        Alphmax.append(0)
        fmax.append('A')
        for j in range(4):
            if Profile[i][j] > maxProbably[i]:
                maxProbably[i] = Profile[i][j]
                Alphmax[i] = j
    for i in range(len(Motifs[0])):
        if Alphmax[i] == 0:
            Alphmax[i] = 'A'
        elif Alphmax[i] == 1:
            Alphmax[i] = 'C'
        elif Alphmax[i] == 2:
            Alphmax[i] = 'G'
        elif Alphmax[i] == 3:
            Alphmax[i] = 'T'
    score = 0
    for i in range(len(Motifs[0])):
        for j in range(len(Motifs)):
            if Motifs[j][i] != Alphmax[i]:
                if Motifs[j][i] == 'A':
                    score += len(Motifs) * Profile[i][0]
                if Motifs[j][i] == 'C':
                    score += len(Motifs) * Profile[i][1]
                if Motifs[j][i] == 'G':
                    score += len(Motifs) * Profile[i][2]
                if Motifs[j][i] == 'T':
                    score += len(Motifs) * Profile[i][3]
    return score

def main():
    with open('inputGM.txt', 'r') as f:
        k, t = f.readline().split()
        k, t = int(k), int(t)
        listDNA = f.readlines()
        for i in range(len(listDNA)):
            listDNA[i] = listDNA[i][:-1]
    f.close()
    BestMotifs = []
    for i in range(t):
        BestMotifs.append(listDNA[i][:k])
    for i in range(len(listDNA[0]) - k + 1):
        motif0 = listDNA[0][i:i + k]
        Motifs = []
        Motifs.append(motif0)
        for j in range(1, t):
            mProfile = formProfile(Motifs)
            Motifi = Profile.MostProbablyKmer(listDNA[j], k, mProfile)
            Motifs.append(Motifi)
        if Score(formProfile(Motifs), Motifs) < Score(formProfile(BestMotifs), BestMotifs):
            BestMotifs = Motifs
            #print('score=', str(Score(formProfile(BestMotifs), BestMotifs)))
    for i in range(len(BestMotifs)):
        print(str(BestMotifs[i]))

#main()