__author__ = 'lenk'
import LEADERBOARDCYCLOPEPTIDESEQUENCING1

count = []

def cutM(M, spectralConvolution):
    indel = []
    for i in range(len(spectralConvolution)):
        if spectralConvolution[i] < 57 or spectralConvolution[i] > 200:
            indel.append(i)
    countI = 0
    for index in indel:
        spectralConvolution.pop(index - countI)
        count.pop(index - countI)
        countI += 1
    indel = []
    count.sort()
    count.reverse()
    if M < len(spectralConvolution):
        meetMin = count[int(M - 1)]
    elif len(spectralConvolution) != 0:
        meetMin = count[-1]
    else:
        return []
    countI = 0
    for i in range(len(spectralConvolution)):
        if count[i] < meetMin:
            indel.append(i)
    for index in indel:
        spectralConvolution.pop(index - countI)
        count.pop(index - countI)
        countI += 1
    for i in range(len(indel)):
            indel.pop()
    return spectralConvolution

def spectralConvolution(Spectrum):
    m = []
    tempCount = []
    for i in range(1, len(Spectrum)):
        for j in range(i - 1, 0, -1):
            if Spectrum[i] != Spectrum[j]:
                m.append(Spectrum[i] - Spectrum[j])
    max = m[0]
    for i in range(1, len(m)):
        if m[i] > max:
            max = m[i]

    for i in range(max + 1):
        tempCount.append(0)
        count.append(0)
    for i in range(len(m)):
        tempCount[m[i]] += 1
        count[m[i]] += 1
    ans = []
    for i in range(max + 1):
        currentMax = count[0]
        ans.append(0)
        for j in range(max + 1):
            if tempCount[j] >= currentMax and tempCount[j] != 0:
                currentMax = tempCount[j]
                ans[-1] = j
        if tempCount[ans[-1]] != 0:
            tempCount[ans[-1]] = 0
        if currentMax == 0:
            return ans[:-1]
    return ans

def main():
    Inp = []
    Spectrum = []
    with open('inputSC.txt', 'r') as f:
        M = int(f.readline())
        N = int(f.readline())
        Inp.append(f.readline().split())
        for i in range(len(Inp[0])):
            Spectrum.append(int(Inp[0][i]))
    f.close()
    Spectrum.sort()
    LEADERBOARDCYCLOPEPTIDESEQUENCING1.LEADERBOARDCYCLOPEPTIDESEQUENCING(cutM(M, spectralConvolution(Spectrum)), Spectrum, N)
    #print(str(spectralConvolution(Spectrum)))

main()