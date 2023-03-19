import pandas as pd
import numpy as np
import collections
import operator
import os
import re
import sys
def bipartite(graph):
    ################################################
    #Problem 2
    ############################################################
    #given a graph determine if it is bipartite
 

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

    for list in list1:
        u,v = list
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1

    graph = adj_matrix

    #start at node
    start = 1
    #give color
    colors = [False] * numOfNodes
    #colors[start] = 'b'
    queue = []
    queue.append(start)
    colorOptions = ['r', 'b']
    colors[start] = 'r'
    #find children
    notBipartite = False
    while not all(colors):
        if notBipartite:
            break
        s = queue.pop()
        kids = np.nonzero(graph[s])[0]
        
        #cfind color for children
        if colors[s]=='r':
            color = 'b'
        else: color = 'r'
        for kid in kids:
            if not colors[kid]:
                colors[kid]=color
                queue.append(kid)
            if colors[kid] == colors[s]:
                notBipartite = True
                print("Not Bipartite")
            
        #catch not connected bits
        if not all(colors) and not queue:
            queue.append(colors.index(False))
            colors[queue[0]]='r'
    if not notBipartite:
        print('Bipartite')

graph = sys.argv[1]
bipartite(graph)
