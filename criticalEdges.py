import pandas as pd
import numpy as np
import collections
import operator
import os
import re
from collections import Counter
from functools import reduce
import sys

def criticalEdges(graph):

    #os.chdir(r'/Users/hconner/')
    my_file = open(graph, "r")
    data = my_file.read()
    data = re.findall('\d+', data)

    # perform conversion
    data1 = [int(i) for i in data]

    #remove first 3 entries in  graph
    numOfNodes = data1.pop(0)
    numOfEdges = data1.pop(0)


    list1 = [data1[i:i+3] for i in range(0, len(data1), 3)]

    # Create an empty adjacency matrix with n x n size
    adj_matrix = [[0 for x in range(numOfNodes)] for y in range(numOfNodes)]

    for list in list1:
        u,v,w = list
        adj_matrix[u][v] = w
        adj_matrix[v][u] = w

    graph = adj_matrix


    # number of vertices in graph
    N = len(graph)
    #creating graph by adjacency matrix method

    selected_node = [0] * len(graph)

    no_edge = 0


    routes = []
    costs = []

    for i in range(len(graph)):
        selected_node = [0] * len(graph)
        selected_node[i] = True
        route = []
        cost = []
        
        no_edge = 0
        
        while (no_edge < len(graph) - 1):
    
            minimum = float('inf')
            a = 0
            b = 0
            for m in range(len(graph)):
                if selected_node[m]:
                    for n in range(len(graph)):
                        if ((not selected_node[n]) and graph[m][n]):  
                            # not in selected and there is an edge
                            if minimum > graph[m][n]:
                                minimum = graph[m][n]
                                a = m
                                b = n
            #print(str(a) + " " + str(b) + " " + str(graph[a][b]))
            route.append(tuple([a,b]))
            cost.append(graph[a][b])
            selected_node[b] = True
            no_edge += 1

        routes.append((route))
        costs.append(cost)





    criticalEdges = pd.Series(routes).explode().value_counts()
    print(criticalEdges[criticalEdges ==criticalEdges.max()].index)

####################
graph = sys.argv[1]
criticalEdges(graph)