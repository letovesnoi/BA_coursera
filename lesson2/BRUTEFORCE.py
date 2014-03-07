__author__ = 'lenk'

mArray = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

def rec(M, mArray, t):
    count = 0
    if M < 0:
        return 0
    if M == 0:
        return 1
    for mass in mArray:
        temp = M - mass
        if temp in t:
            count += t[temp]
        else:
            tempCount = rec(temp, mArray, t)
            t[temp] = tempCount
            count += tempCount
    return count

print(rec(9120, mArray, {}))
