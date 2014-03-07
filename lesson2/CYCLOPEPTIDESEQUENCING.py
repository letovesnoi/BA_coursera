__author__ = 'lenk'
mass = [57, 71, 87, 97,	99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
Spectrum = []
Inp = []
listP = []

def getSpectrumPeptide(ip):
    peptide = listP[ip][:]
    tempspectrum = [0]
    for count in range(1, len(peptide)):
        for pos in range(len(peptide) - count + 1):
            Pp = peptide[pos:pos + count]
            sum = 0
            for i in range(count):
                temp = 0
                while mass[temp] != Pp[i]:
                    temp += 1
                sum = sum + mass[temp]
            tempspectrum.append(sum)
    sum = 0
    for i in range(len(peptide)):
        temp = 0
        while mass[temp] != peptide[i]:
            temp += 1
        sum = sum + mass[temp]
    tempspectrum.append(sum)
    tempspectrum.sort()
    return tempspectrum

def getCycloSpectrumPeptide(ip):
    tempCyclospectrum = [0]
    peptide = listP[ip][:]
    #for i in range(len(listP[ip])):
    #    peptide.append(listP[ip][i])
    #pep = listP[ip][:]
    #peptide = pep[:]
    for i in range(len(listP[ip]) - 2):
        peptide.append(listP[ip][i])
    #peptide += pep[0:-2]
    for count in range(1, len(listP[ip])):
        for pos in range(len(listP[ip])):
            Pp = peptide[pos:pos+count]
            sum = 0
            for i in range(count):
                j = 0
                while mass[j] != Pp[i]:
                    j += 1
                sum = sum + mass[j]
            tempCyclospectrum.append(sum)
    sum = 0
    for i in range(len(listP[ip])):
        j = 0
        while mass[j] != peptide[i]:
            j += 1
        sum = sum + mass[j]
    tempCyclospectrum.append(sum)
    tempCyclospectrum.sort()
    return tempCyclospectrum


def compareSpectrum(ip):
    tempCyclospectrum = getCycloSpectrumPeptide(ip)
    if len(tempCyclospectrum) == len(Spectrum):
        for j in range(len(Spectrum)):
            if int(Spectrum[j]) != tempCyclospectrum[j]:
                return 0
        return 1
    return 0

def consistent(ip):
    l = 0
    tempspectrum = getSpectrumPeptide(ip)
    for j in range(len(tempspectrum)):
        while (int(Spectrum[l]) != tempspectrum[j]) and (l < len(Spectrum)):
            l += 1
            if l == len(Spectrum):
                return 0
        if l >= len(Spectrum):
                return 0
    return 1

def main():
    begF = 1
    with open('input.txt', 'r') as f:
        Inp.append(f.readline().split())
        for i in range(len(Inp[0])):
            Spectrum.append(int(Inp[0][i]))
    f.close()
    Spectrum.sort()
    for i in range(18):
        listP.append([mass[i]])
    while len(listP) != 0 or begF == 1:
        begF = 0
        tempL = len(listP)
        for ip in range(tempL):
            for i in range(18):
                k = listP[ip][:]
                k.append(mass[i])
                listP.append(k)
        for ip in range(tempL):
            listP.pop(0)
        #print(str(listP))
        ind = []
        f1 = open('output.txt', 'w')
        for ip in range(len(listP)):
            if compareSpectrum(ip):
                for i in range(len(listP[ip]) - 1):
                    f1.write(str(listP[ip][i]))
                    f1.write('-')
                f1.write(str(listP[ip][len(listP[ip]) - 1]))
                f1.write(' ')
                #listP.pop(ip)
                ind.append(ip)
            elif not consistent(ip):
                #listP.pop(ip)
                ind.append(ip)
        countI = 0
        for index in ind:
            listP.pop(index - countI)
            countI += 1
    f1.close()

main()