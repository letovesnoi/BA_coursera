__author__ = 'lenk'

def countProbably(Text, i, k, mProfile):
    Pattern = Text[i:i + k]
    ans = 1
    for i in range(k):
        if Pattern[i] == 'A':
            ans *= float(mProfile[i][0])
        elif Pattern[i] == 'C':
            ans *= float(mProfile[i][1])
        elif Pattern[i] == 'G':
            ans *= float(mProfile[i][2])
        elif Pattern[i] == 'T':
            ans *= float(mProfile[i][3])
    return ans

def MostProbablyKmer(Text, k, mProfile):
    M = []
    for i in range(len(Text) - k + 1):
        M.append(countProbably(Text, i, k, mProfile))
    max = 0
    indMax = 0
    for i in range(len(M)):
        if M[i] > max:
            max = M[i]
            indMax = i
    return Text[indMax:indMax + k]


def main():
    with open('inputP.txt', 'r') as f:
        Text = f.readline()
        k = int(f.readline())
        f.readline()
        mProfile = []
        for line in f:
            mProfile.append(line.split())
    f.close
    maxProbablyS = MostProbablyKmer(Text, k, mProfile)
    print(str(maxProbablyS))

#main()