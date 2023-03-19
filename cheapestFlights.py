#Problem 1
############################################################
import pandas as pd
import numpy as np
import collections
import operator
import os
import re
import sys

def cheapestFlight(graph, src, dest, k):

    #os.chdir(r'/Users/hconner/')
    #graph = 'graph2_weights.txt'
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



    #src = 2
    #dest = 5
    #k = 10
    distances = [float('inf')] * (numOfNodes + 1)
    distances[src] = 0
    queue = [(src, 0, [src])]

    while queue:
        curr, cost, path = queue.pop(0)
        if curr == dest and len(path) - 1 <= k:
            break#return (path, cost)
        
        kids = np.nonzero(adj_matrix[curr])[0]
        for kid in kids:
            
            if len(path) <= k and distances[kid] > cost + w:
                distances[kid] = cost + adj_matrix[curr][kid]
                queue.append((kid, cost + adj_matrix[curr][kid], path + [kid]))
    print(path, cost)


graph = sys.argv[1]
src = int(sys.argv[2])
dest = int(sys.argv[3])
k = int(sys.argv[4])

cheapestFlight(graph, src, dest, k)
    


