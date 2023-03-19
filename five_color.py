import os
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


#os.chdir('/Users/hconner')


def adj_mat(graph):
        
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

    return(np.array(adj_matrix))




def five_color_planar(adj_matrix):
    n = adj_matrix.shape[0]
    colors = np.zeros(n, dtype=int)
    available_colors = [1, 2, 3, 4, 5]
    degrees = np.sum(adj_matrix, axis=1)
    
    while np.any(colors == 0):
        # Find a vertex with maximum degree that still needs to be colored
        v = np.argmax((degrees > 0) & (colors == 0))
        
        # Assign the smallest available color to the vertex
        used_colors = []
        for u in range(n):
            if adj_matrix[v,u] == 1 and colors[u] != 0:
                used_colors.append(colors[u])
        for color in available_colors:
            if color not in used_colors:
                colors[v] = color
                break
        
        # Update the degrees of the adjacent vertices
        degrees[adj_matrix[v,:] == 1] -= 1
    
    return colors

graph = sys.argv[1]
#graph = 'graph2_cc.txt'
adj_matrix = adj_mat(graph)
if any(np.sum(adj_matrix, 0)<5):
    colors = five_color_planar(adj_matrix)
else:
    colors = "no vertice with less than 6 degrees"

print(colors)


