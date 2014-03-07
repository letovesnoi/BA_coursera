__author__ = 'lenk'

import DeBruijnfromkmers
import EulerianCycle
import StringComposition

def generatePatterns(k):
    patterns = []
    for i in range(2 ** (k)):
        tempi = i
        patterns.append('')
        while tempi >= 1:
            r = tempi - tempi / 2 * 2
            tempi = tempi / 2
            patterns[-1] += str(r)
    for j in range(len(patterns)):
        for i in range(k - len(patterns[j])):
            patterns[j] += '0'
    #print(patterns)
    return patterns

def kUniversalCircularString(k):
    patterns = generatePatterns(k)
    graph = DeBruijnfromkmers.deBruijnfromkmers(patterns)
    cycle = EulerianCycle.EULERIANCYCLE(graph)
    #print(cycle)
    #EulerianCycle.writeCycle(cycle)
    circular = str(cycle[0][:-1])
    for i in cycle:
        circular += i[-1:]
    newCircular = circular
    for j in range(len(circular) - 1, 1, -1):
        if circular[:j] == circular[-j:]:
            newCircular = circular[:-j]
            break

    #print(circular)
    return newCircular

def main():
    with open('inputkUniversal.txt', 'r') as fin:
        k = int(fin.read())
    circular = kUniversalCircularString(k)
    with open('outputkUniversal.txt', 'w') as fout:
        fout.write(str(circular))
main()
