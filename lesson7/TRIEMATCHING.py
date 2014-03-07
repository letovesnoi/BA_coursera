def prefixTrieMatching(text, trie, j, dictionary):
    i = 0
    symbol = text[i]
    current_dict = trie
    while True:
        if symbol in current_dict:
            current_dict = current_dict[symbol]
            if i + 1 < len(text):
                symbol = text[i+1]
                i += 1
            else:
                if '_end_' in current_dict:
                    dictionary[current_dict['_end_']].append(j)
                    return 0
            if '_end_' in current_dict:
                dictionary[current_dict['_end_']].append(j)
                return 0
        else:
            return 0
    

def buildTrie(words):
    _end = '_end_'
    _start = '_start_'
    root = dict()
    for i, word in enumerate(words):
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict = current_dict.setdefault(_end, i)
    return root


def TrieMatching(filename):
    with open(filename) as f:
        words = f.read().split()
    text = words[0]
    patterns = words[1:]
    trie = buildTrie(patterns)
    j = 0
    dictionary = {}
    for i in range(len(words) - 1):
        dictionary[i] = []
    while text != "":
        prefixTrieMatching(text, trie, j, dictionary)
        text = text[1:]
        j += 1
    all = []
    for key in dictionary:
        all.extend(dictionary[key])
    all.sort()
    allS = ''
    for i in all:
        allS += str(i) + ' '
    print(allS)

filename = "dataset.txt"
TrieMatching(filename)
