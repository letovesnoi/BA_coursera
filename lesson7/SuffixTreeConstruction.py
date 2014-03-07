__author__ = 'lenk'

import TrieConstruction

'''def dfs(trie, node):
    for i in trie[node]:
        if i == '_end_':
            break
        currentTrieTemp = trie[node][i]
        currentTrie = {}
        currentTrie['root'] = currentTrieTemp
        dfs(currentTrie, currentTrie.keys()[0])'''

def iterative_dfs(graph, path=[]):
    edges = []
    graph = graph.items()
    t = []
    t.extend(graph)
    tempE = ''
    while t:
        temp = t.pop(0)
        v = temp[0]
        if v == '_end_':
            if t:
                tempE = t[0][0]
                if len(t[0][1]) != 1:
                    edges.append(tempE)
                    tempE = ''
            continue
        graph = temp[1].items()
        if graph[0][0] != '_end_':
            tempE += graph[0][0]
        if len(graph[0][1]) != 1:
            edges.append(tempE)
            tempE = ''
        #path = path + [v]
        t = graph + t
    with open('outputSTC.txt', 'w') as fout:
        for edge in edges:
            fout.write(edge + '\r\n')
    return path

def getWords(Text):
    words = []
    for i in range(len(Text) - 1, -1, -1):
        words.append(Text[i:])
    return words

def main():
    with open('inputSTC.txt', 'r') as fin:
        Text = fin.readline()
    words = getWords(Text)
    suffixTrietemp = TrieConstruction.buildTrie(words)
    suffixTrie = {}
    suffixTrie['root'] = suffixTrietemp
    #TrieConstruction.output(suffixTrie, 1)
    #dfs(suffixTrie, suffixTrie.keys()[0])
    #print
    iterative_dfs(suffixTrie, path=[])

main()