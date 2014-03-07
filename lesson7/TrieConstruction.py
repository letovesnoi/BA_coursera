
filename = "dataset.txt"
counter = 1

def buildTrie(words):
    _end = '_end_'
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict = current_dict.setdefault(_end, _end)
    return root

def output(current_dict, previous_counter):
    global counter
    previous_counter = counter
    for key in reversed(sorted(current_dict.iterkeys())):
        if key != '_end_':
            counter += 1
            print previous_counter, counter, key
            output(current_dict[key], previous_counter)

def main():
    with open(filename) as f:
        words = f.read().split()
    trie = buildTrie(words)
    output(trie, 1)

#main()