__author__ = 'lenk'

def countBreak(permutation):
    count = 0
    P = {}
    for i in range(len(permutation)):
        P[permutation[i]] = i
    if P[permutation[0]] != 1:
        count += 1
    if P[permutation[len(permutation) - 1]] + 1 != permutation[len(permutation) - 1]:
        count += 1
    i = 0
    while i in range(len(permutation) - 1):
        if int(permutation[i][1:]) == int(permutation[i + 1][1:]) - 1 \
            and permutation[i][0] == permutation[i + 1][0] and permutation[i][0] == '+':
            while int(permutation[i][1:]) == int(permutation[i + 1][1:]) - 1 \
                and permutation[i][0] == permutation[i + 1][0] and permutation[i][0] == '+':
                i += 1
                if i == len(permutation) - 1:
                    break
        elif permutation[i][0] == permutation[i + 1][0] and permutation[i + 1][0] == '-' \
            and int(permutation[i + 1][1:]) == int(permutation[i][1:]) - 1:
            while permutation[i][0] == permutation[i + 1][0] and permutation[i + 1][0] == '-' \
                and int(permutation[i + 1][1:]) == int(permutation[i][1:]) - 1:
                i += 1
                if i == len(permutation) - 1:
                    break
        i += 1
        count += 1
    return count

def main():
    with open('inputNofB.txt', 'r') as fin:
        temp = fin.readline()
        temp = temp[1:-1][:]
        permutation = temp.split(' ')
    print countBreak(permutation)

main()