__author__ = 'lenk'

graph = {}
blocks = 0

def getGraph(P, Q):
    global graph
    global blocks
    listPath = []
    listPath.extend(P)
    listPath.extend(Q)
    for i in range(len(listPath)):
        genomePath = listPath[i].split(' ')
        blocks += len(genomePath)
        genomePath.append(genomePath[0])
        getEdges(genomePath)
    return graph

def getEdges(genomePath):
    global graph
    for i in range(len(genomePath) - 1):
        if genomePath[i][0] == '+' and genomePath[i + 1][0] == '+':
            if '+' + genomePath[i][1:] not in graph:
                graph['+' + genomePath[i][1:]] = []
            if '-' + genomePath[i + 1][1:] not in graph:
                graph['-' + genomePath[i + 1][1:]] = []
            graph['+' + genomePath[i][1:]].append('-' + genomePath[i + 1][1:])
            graph['-' + genomePath[i + 1][1:]].append('+' + genomePath[i][1:])
        if genomePath[i][0] == '+' and genomePath[i + 1][0] == '-':
            if '+' + genomePath[i][1:] not in graph:
                graph['+' + genomePath[i][1:]] = []
            if '+' + genomePath[i + 1][1:] not in graph:
                graph['+' + genomePath[i + 1][1:]] = []
            graph['+' + genomePath[i][1:]].append('+' + genomePath[i + 1][1:])
            graph['+' + genomePath[i + 1][1:]].append('+' + genomePath[i][1:])
        if genomePath[i][0] == '-' and genomePath[i + 1][0] == '+':
            if '-' + genomePath[i][1:] not in graph:
                graph['-' + genomePath[i][1:]] = []
            if '-' + genomePath[i + 1][1:] not in graph:
                graph['-' + genomePath[i + 1][1:]] = []
            graph['-' + genomePath[i][1:]].append('-' + genomePath[i + 1][1:])
            graph['-' + genomePath[i + 1][1:]].append('-' + genomePath[i][1:])
        if genomePath[i][0] == '-' and genomePath[i + 1][0] == '-':
            if '-' + genomePath[i][1:] not in graph:
                graph['-' + genomePath[i][1:]] = []
            if '+' + genomePath[i + 1][1:] not in graph:
                graph['+' + genomePath[i + 1][1:]] = []
            graph['-' + genomePath[i][1:]].append('+' + genomePath[i + 1][1:])
            graph['+' + genomePath[i + 1][1:]].append('-' + genomePath[i][1:])

def countCYCLE(graph):
    count = 0
    while len(graph) != 0:
        start = graph.keys()[0]
        current = graph[start][0]
        graph[start].remove(current)
        graph[current].remove(start)
        while current != start:
            newCurrent = graph[current][0]
            graph[current].remove(newCurrent)
            if graph[current] == []:
                del graph[current]
            graph[newCurrent].remove(current)
            if graph[newCurrent] == []:
                del graph[newCurrent]
            current = newCurrent
        count += 1
    return count

def main():
    global blocks
    with open('inputBD.txt', 'r') as fin:
        temp = fin.readline()[:-1]
        P = temp.split(')(')
        P[0] = P[0][1:]
        P[len(P) - 1] = P[len(P) - 1][:-1]
        temp = fin.readline()[:-1]
        Q = temp.split(')(')
        Q[0] = Q[0][1:]
        Q[len(Q) - 1] = Q[len(Q) - 1][:-1]
        #print P, Q
    graph = getGraph(P, Q)
    #print graph
    count = countCYCLE(graph)
    #print count
    d = blocks / 2 - count
    print d

main()
