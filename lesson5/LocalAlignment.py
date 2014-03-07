__author__ = 'lenk'

back = {}
maxS = 0
index = [0, 0]

def LA(score, v, w):
    global back
    global maxS
    global index
    s = {}
    s[0, 0] = 0
    for i in range(1, len(v)):
        s[i, 0] = s[i - 1, 0] - 5
    for j in range(1, len(w)):
        s[0, j] = s[0, j - 1] - 5
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            s[i, j] = max(s[i - 1, j] - 5, s[i, j - 1] - 5)
            s[i, j] = max(s[i, j], s[i - 1, j - 1] + int(score[v[i], w[j]]))
            s[i, j] = max(s[i, j], 0)

            if s[i, j] > maxS:
                maxS = s[i, j]
                index = [i, j]

            if s[i, j] == s[i, j - 1] - 5:
                back[i, j] = 0
            elif s[i, j] == s[i - 1, j] - 5:
                back[i, j] = 1
            elif s[i, j] == s[i - 1, j - 1] + int(score[v[i], w[j]]) and v[i] == w[j]:
                back[i, j] = 2
            elif s[i, j] == s[i - 1, j - 1] + int(score[v[i], w[j]]) and v[i] != w[j]:
                back[i, j] = 3
            elif s[i, j] == 0:
                back[i, j] = 4
    #print index
    return maxS

def OUTPUTLCS(v, w, i, j):
    global back
    global str1
    global str2
    if i == 0 or j == 0:
        return 0
    if back[i, j] == 4:
        return 0
    elif back[i, j] == 0:
        OUTPUTLCS(v, w, i, j - 1)
        str1 += '-'
        str2 += w[j]
    elif back[i, j] == 1:
        OUTPUTLCS(v, w, i - 1, j)
        str1 += v[i]
        str2 += '-'
    else:
        OUTPUTLCS(v, w, i - 1, j - 1)
        str1 += v[i]
        str2 += w[j]

'''def getGraph(score, v, w):
    allVertex = []
    for i in range(len(v)):
        for j in range(len(w)):
            allVertex.append((i, j))
    graph = {}

    graph[0, 0] = {}
    for vertex in allVertex:
        graph[0, 0][vertex] = 0
    del graph[0, 0][0, 0]

    for i in range(len(v) - 1):
        for j in range(len(w) - 1):
            graph[i, j] = {(i + 1, j): -5, (i, j + 1): -5, (i + 1, j + 1): score[v[i + 1], w[j + 1]],
                           (len(v) - 1, len(w) - 1): 0}
    for i in range(len(v) - 1):
        j = len(w) - 1
        graph[i, j] = {(i + 1, j): -5, (len(v) - 1, len(w) - 1): 0}
    for j in range(len(w) - 1):
        i = len(v) - 1
        graph[i, j] = {(i, j + 1): -5, (len(v) - 1, len(w) - 1): 0}
    graph[len(v) - 2, len(w) - 2][len(v) - 1, len(w) - 1] = max(0, score[v[len(v) - 1], w[len(w) - 1]])

    return graph'''


'''def LPDAG(graph, start_node, goal_node):
    back = {}
    s = {}
    s['0'] = '0'
    grey = []
    #for vertex in allVertex:
    #    s[vertex] = 0
    grey.append(start_node)
    s[grey[0]] = 0
    while len(grey) != 0:
        node = grey[0]
        grey.remove(node)
        if node in graph:
            for child in graph[node].keys():
                if child not in s:
                    s[child] = 0
                if s[child] < s[node] + int(graph[node][child]):
                    s[child] = s[node] + int(graph[node][child])
                    back[child] = node
                grey.append(child)
        #print grey
    print(s[goal_node])
    current = goal_node
    temp = [current]
    print('levelup')
    while current in back:
        temp.append(back[current])
        current = back[current]
    #print(temp)
    return temp

def getAlign(temp, v, w):
    global str1new
    global str2new
    str1 = ''
    str2 = ''
    for i in range(len(temp) - 1):
        if temp[i + 1][0] == temp[i][0] - 1 and temp[i + 1][1] == temp[i][1] - 1:
            str1 += v[temp[i][0]]
            str2 += w[temp[i][1]]
        if temp[i + 1][0] == temp[i][0] and temp[i + 1][1] == temp[i][1] - 1:
            str1 += '-'
            str2 += w[temp[i][1]]
        if temp[i + 1][0] == temp[i][0] - 1 and temp[i + 1][1] == temp[i][1]:
            str1 += v[temp[i][0]]
            str2 += '-'
    for i in range(len(str1) - 1, -1, -1):
        str1new += str1[i]
        str2new += str2[i]
    print(str1new)
    print(str2new)'''

def main():
    global str1
    global str2
    global allVertex
    global index
    str1 = ''
    str2 = ''
    with open('inputLA.txt', 'r') as fin:
        v = fin.readline()[:-1]
        w = fin.readline()[:-1]
    with open('PAM250.txt', 'r') as ftable:
        acids = ftable.readline().split(' ')
        temp = acids[-1].split('\n')
        acids[-1] = temp[0]
        score = {}
        weight = []
        while True:
            tempW = ftable.readline().split(' ')
            if tempW[0] == '':
                break
            weight.append(tempW)
            temp = weight[-1][-1].split('\n')
            weight[-1][-1] = temp[0]
    for i in range(len(weight)):
        for j in range(len(weight[i])):
            score[acids[i], acids[j]] = weight[i][j]
    #print score
    #graph = getGraph(score, v, w)
    #start = (0, 0)
    #end = (len(v) - 1, len(w) - 1)
    #temp = LPDAG(graph, start, end)
    #print temp
    #getAlign(temp, v, w)
    print LA(score, v, w)
    OUTPUTLCS(v, w, index[0], index[1])
    with open('outputLA.txt', 'w') as fout:
        #fout.write(str(s) + '\r\n')
        fout.write(str1 + '\r\n')
        fout.write(str2)

main()