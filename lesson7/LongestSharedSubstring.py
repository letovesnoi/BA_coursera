__author__ = 'lenk'

import SuffixTreeConstruction
import TrieConstruction

def getWordsTwo(Text1, Text2):
    wordsTwo = []
    for i in range(len(Text1) - 1, -1, -1):
        wordsTwo.append(Text1[i:] + '_first_')
    for i in range(len(Text2) - 1, -1, -1):
        wordsTwo.append(Text2[i:] + '_second_')

def main():
    with open('inputLSS.txt', 'r') as fin:
        Text1 = fin.readline()[:-1]
        Text2 = fin.readline()[:-1]
    words = getWordsTwo(Text1, Text2)
    suffixTrietemp = TrieConstruction.buildTrie(words)
    suffixTrie = {}
    suffixTrie['root'] = suffixTrietemp
    SuffixTreeConstruction.iterative_dfs(suffixTrie, path=[])
