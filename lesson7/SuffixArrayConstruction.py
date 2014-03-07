__author__ = 'lenk'

def SuffixArrayConstraction(Text):
    suffixes = []
    dict = {}
    suffixArray = []
    for i in range(len(Text)):
        suffixes.append(Text[i:])
        #dict[Text[i:]] = i
    #suffixes.sort()
    #for suffix in suffixes:
    #    suffixArray.append(dict[suffix])
    return suffixArray

def main():
    with open('inputSAC.txt', 'r') as fin:
        Text = fin.readline()
    suffixArray = SuffixArrayConstraction(Text)
    '''with open('outputSAC.txt', 'w') as fout:
        for i in range(len(suffixArray) - 1):
            fout.write(str(suffixArray[i]) + ', ')
        fout.write(str(suffixArray[-1]))'''

main()