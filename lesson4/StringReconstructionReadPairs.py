__author__ = 'lenk'

import EulerianPath

def writePathString(path):
    string = path[0][:-1]
    for i in path:
        string += str(i[-1:])
    with open('outputEulerian.txt', 'w') as fout:
        fout.write(string)

def main():
    path = EulerianPath.EULERIANPATH()
    writePathString(path)
    print path

main()