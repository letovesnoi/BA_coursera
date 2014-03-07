__author__ = 'lenk'

def printNewPermutation(newPermutation):
    with open('outputGS.txt', 'a') as fout:
        fout.write('(')
        for i in range(len(newPermutation)):
            if i != len(newPermutation) - 1:
                fout.write(newPermutation[i] + ' ')
            else:
                fout.write(newPermutation[i])
        fout.write(')\r\n')

def GREEDYSORTING(P, permutation):
    dist = 0
    currentPermutation = permutation[:]
    for i in range(1, len(P) + 1):
        newPermutation = currentPermutation[:i - 1]
        if '+' + str(i) in P:
            s = '+' + str(i)
        else:
            s = '-' + str(i)
        if P[s] != i - 1:
            temp = currentPermutation[i - 1: P[s] + 1][:]
            for j in range(i - 1, P[s] + 1):
                if temp[j - i - 1][0] == '-':
                    temp[j - i - 1] = '+' + temp[j - i - 1][1:]
                else:
                    temp[j - i - 1] = '-' + temp[j - i - 1][1:]
            temp.reverse()
            newPermutation.extend(temp)
            newPermutation.extend(currentPermutation[P[s] + 1:])
            P = {}
            for i in range(len(newPermutation)):
                P[newPermutation[i]] = i
            dist += 1
            printNewPermutation(newPermutation)
            if s[0] == '+':
                newPermutation[P['-' + s[1:]]] = '+' + newPermutation[P['-' + s[1:]]][1:]
                P = {}
                for i in range(len(newPermutation)):
                    P[newPermutation[i]] = i
                dist += 1
                printNewPermutation(newPermutation)
        else:
            newPermutation.extend(currentPermutation[P[s]:])
            if s[0] == '-':
                newPermutation[P[s]] = '+' + newPermutation[P[s]][1:]
                P = {}
                for i in range(len(newPermutation)):
                    P[newPermutation[i]] = i
                dist += 1
                printNewPermutation(newPermutation)
        currentPermutation = newPermutation[:]

    return dist

def main():
    with open('inputGS.txt', 'r') as fin:
        temp = fin.readline()
        temp = temp[1:-1][:]
        permutation = temp.split(' ')
    P = {}
    for i in range(len(permutation)):
        P[permutation[i]] = i
    GREEDYSORTING(P, permutation)

main()