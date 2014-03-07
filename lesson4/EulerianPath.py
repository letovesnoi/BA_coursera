__author__ = 'lenk'

import EulerianCycle

vertex = []

def addEdge(graph):
    global vertex
    countIN = {}
    countOUT = {}
    for i in graph:
        for j in graph[i]:
            if j not in countIN:
                countIN[j] = graph[i][j]
            else:
                countIN[j] += graph[i][j]
            if i not in countOUT:
                countOUT[i] = graph[i][j]
            else:
                countOUT[i] += graph[i][j]
    for i in countOUT:
        if i not in countIN:
            vertex.append([i, 1])
    for i in countIN:
        if i not in graph:
            vertex.append([i, 0])
        else:
            if countOUT[i] != countIN[i]:
                if countOUT[i] < countIN[i]:
                    vertex.append([i, 0])
                else:
                    vertex.append([i, 1])
        if len(vertex) == 2:
            if vertex[0][1] == 0:
                if vertex[0][0] not in graph:
                    graph[vertex[0][0]] = {}
                if vertex[1][0] in graph[vertex[0][0]]:
                    graph[vertex[0][0]][vertex[1][0]] += 1
                else:
                    graph[vertex[0][0]][vertex[1][0]] = 1
                print(vertex)
                return graph
            elif vertex[1][1] == 0:
                if vertex[1][0] not in graph:
                    graph[vertex[1][0]] = {}
                if vertex[0][0] in graph[vertex[1][0]]:
                    graph[vertex[1][0]][vertex[0][0]] += 1
                else:
                    graph[vertex[1][0]][vertex[0][0]] = 1
                print(vertex)
                return graph
    print(vertex)
    return graph

def EULERIANPATH(list):
    global vertex
    newlist = addEdge(list)
    cycle = EulerianCycle.EULERIANCYCLE(newlist)

    if vertex[0][1] == 1:
        begin = vertex[1][0]
        end = vertex[0][0]
    else:
        begin = vertex[0][0]
        end = vertex[1][0]

    for i in range(len(cycle) - 1):
        if cycle[i] == begin and cycle[i + 1] == end:
            iBegin = i + 1
            break

    path = cycle[:-1]
    path = path[iBegin:] + path[:iBegin]
    return path

def main():
    list = EulerianCycle.readGraph()
    path = EULERIANPATH(list)
    EulerianCycle.writeCycle(path)

#main()