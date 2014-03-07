__author__ = 'lenk'

def addSuffix(suffix, dictTree):
    current = ''
    previous = current
    ind = 0
    while current == suffix[:len(current)]:
        if dictTree[current] != []:
            for child in dictTree[current]:
                for i in range(len(child), ind, -1):
                    if child[:i] == suffix[:len(child[:i])]:
                        previous = current
                        current = child
                        ind = i
                        break
            if previous == current:
                dictTree[current].append(suffix[ind:])
                break
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
    #print dictTree

def main():
    with open('inputSTC.txt', 'r') as fin:
        Text = fin.readline()
    constructST(Text)

main()