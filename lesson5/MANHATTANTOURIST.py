__author__ = 'lenk'

def MANHATTANTOURIST(n, m, down, right):
        s = {}
        s[0, 0] = 0
        for i in range(1, n + 1):
            s[i, 0] = s[i - 1, 0] + int(down[i - 1][0])
        for j in range(1, m + 1):
            s[0, j] = s[0, j - 1] + int(right[0][j - 1])
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s[i, j] = max(s[i - 1, j] + int(down[i - 1][j]), s[i, j - 1] + int(right[i][j - 1]))
        return s[n, m]

def main():
    with open('inputDPM.txt', 'r') as fin:
        n = int(fin.readline())
        m = int(fin.readline())
        down = []
        right = []
        for i in range(n):
            down.append(fin.readline().split(' '))
            temp = down[-1][-1].split('\n')
            down[-1][-1] = temp[0]
        fin.readline()
        for i in range(n + 1):
            right.append(fin.readline().split(' '))
            temp = right[-1][-1].split('\n')
            right[-1][-1] = temp[0]
    #print(down)
    #print(right)
    print MANHATTANTOURIST(n, m, down, right)

main()