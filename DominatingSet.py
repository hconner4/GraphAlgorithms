import pandas as pd
import numpy as np
import collections
import operator
import os
import re
from collections import Counter
from functools import reduce
import sys
import copy
from operator import itemgetter

def DominatingSet(graph):

    #graph = sys.argv[1]
    # graph = 'graph2_cc.txt'
    #os.chdir(r'/Users/hconner/')
    my_file = open(graph, "r")
    data = my_file.read()
    data = re.findall('\d+', data)

    # perform conversion
    data1 = [int(i) for i in data]

    #remove first 3 entries in  graph
    numOfNodes = data1.pop(0)
    numOfEdges = data1.pop(0)

    list1 = [data1[i:i+2] for i in range(0, len(data1), 2)]

    # Create an empty adjacency matrix with n x n size
    adj_matrix = [[0 for x in range(numOfNodes)] for y in range(numOfNodes)]

    for l in list1:
        u,v = l
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1

    graph = adj_matrix
    route = []
    NotPosibles = []
    #This gives the most highly connected node and its children
    def highlyConnected(subgraph, NotPosibles):
        NumberOfConnections = [sum(i) for i in zip(*subgraph)]
        indexes, values = zip(*sorted(enumerate(NumberOfConnections), key=itemgetter(1)))
        #NumberOfConnections = [NumberOfConnections[i] for i in NumConn]
        #find the values not in not possible
        res = [x for x in indexes if x not in NotPosibles]
        
        stop = res[len(res)-1]
        
        childs = [ind for ind, ele in enumerate(adj_matrix[stop]) if ele == 1]
        return(stop, childs)


    keepGoing = True
    NumberOfConnections = [sum(i) for i in zip(*graph)]
    indexes, values = zip(*sorted(enumerate(NumberOfConnections), key=itemgetter(1)))
    #NumberOfConnections = [NumberOfConnections[i] for i in NumConn]
    #find the values not in not possible
    res = indexes
    stop = res[len(res)-1]
    childs = [ind for ind, ele in enumerate(adj_matrix[stop]) if ele == 1]
    route.append(stop)
    childs.append(stop)
    NotPosibles.extend(childs)
    while keepGoing:
        stop, childs = highlyConnected(graph, NotPosibles)
        route.append(stop)
        childs.append(stop)
        NotPosibles.extend(childs)
        
        if(len(set(NotPosibles)) == numOfNodes):
            keepGoing = False

    return(len(route))

graph = sys.argv[1]
# graph = 'graph2_cc.txt'
result = DominatingSet(graph)
print(result)