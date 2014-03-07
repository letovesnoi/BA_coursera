__author__ = 'lenk'

def addSuffix(suffix, dictTree):
    current = ''
    previous = current
    ind = 0
    while current in suffix:
        #ind += len(current)
        if dictTree[current] != []:
            for child in dictTree[current]:
                for i in range(len(child), 0, -1):
                    if child[:i] == suffix[ind:ind + len(child[:i])]:
                        previous = current
                        current = child
                        ind += i
                        temp = i
                        break
                    if previous != current:
                        break
                if previous != current and ind == 0:
                    break
                if ind != 0:
                    continue
            if previous == current:
                dictTree[current].append(suffix[ind:])
                break
            '''else:
                dictTree[current].append(suffix[ind:ind + temp])
                dictTree[current].remove(current)
                if suffix[ind:ind + temp] not in dictTree:
                   dictTree[suffix[ind:ind + temp]] = []
                dictTree[suffix[ind:ind + temp]].append(suffix)
                dictTree[suffix[ind:ind + temp]].append(current)'''
        else:
            dictTree[current].append(suffix[ind:])
            break
    if current[:ind] != '':
        dictTree[previous].append(current[:ind])
        dictTree[previous].remove(current)
    if current[:] != '':
        if current[:ind] not in dictTree:
            dictTree[current[:ind]] = []
        dictTree[current[:ind]].append(current)
        dictTree[current[:ind]].append(suffix)
    return dictTree

def constructST(Text):
    dictTree = {}
    dictTree[''] = []
    for i in range(len(Text)):
        suffix = Text[i:]
        dictTree = addSuffix(suffix, dictTree)
    print dictTree

def main():
    with open('inputSTC.txt', 'r') as fin:
        Text = fin.readline()
    constructST(Text)

main()