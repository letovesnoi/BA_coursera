__author__ = 'lenk'

back = {}

def LPDAG(graph, allVertex, start_node, goal_node):
    global back
    s = {}
    s['0'] = '0'
    visited = {}
    grey = []
    for vertex in allVertex:
        visited[vertex] = 0
        s[vertex] = 0
    grey.append(start_node)
    visited[start_node] = 1
    while len(grey) != 0:
        node = grey[0]
        grey.remove(node)
        #if node == goal_node:
        #    print(s[goal_node])
        #    return True
        if node in graph:
            for child in graph[node].keys():
                if s[child] < s[node] + int(graph[node][child]):
                    s[child] = s[node] + int(graph[node][child])
                    back[child] = node
                #if visited[child] == 0:
                grey.append(child)
                #    visited[child] = 1
    print(s[goal_node])
    #print(s)
    current = goal_node
    temp = [current]
    while current in back:
        temp.append(back[current])
        current = back[current]
    #print(temp)
    return temp

def printPath(temp):
    str = ''
    for i in range(len(temp) - 1, -1, -1):
        if i == 0:
            str += temp[i]
        else:
            str += temp[i] + '->'
    print(str)

def main():
    graph = {}
    allVertex = []
    with open('inputLPDAG.txt', 'r') as fin:
        source = fin.readline()[:-1]
        sink = fin.readline()[:-1]
        while True:
            temp = fin.readline()
            if temp == '':
                break
            temp1 = temp.split('->')
            temp2 = temp1[1].split(':')
            begin = temp1[0]
            end = temp2[0]
            allVertex.append(begin)
            allVertex.append(end)
            w = temp2[1][:-1]
            if begin not in graph:
                graph[begin] = {}
            graph[begin][end] = w
    allVertex = set(allVertex)
    #print(graph)
    temp = LPDAG(graph, allVertex, source, sink)
    printPath(temp)

#main()
