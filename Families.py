import sys
from collections import deque
import pandas as pd
import numpy as np
import os

def Families(graph):

    import sys
    from collections import deque
    import pandas as pd
    import numpy as np
    import os
    filePath = sys.argv[1]

    graph = pd.read_csv(graph, sep=r'\n|\t', engine='python', header=None)

    #removes header row with #of nodes and # of edges
    graph = graph.iloc[1:]
    #if values are not integers
    nodes = np.unique(graph.values)
    #find the value of each column not containing n where n appears in the row
    for node in nodes:
        listOfChildren = list(np.array(graph[graph.values == node]).flat)
        #remove n from list and find unique values
        listOfChildren = set([ i for i in listOfChildren if i!=node ])
        print(node , listOfChildren)

#filePath = input("Please enter file: ")

#Families(filePath)

graph = sys.argv[1]
Families(graph)
#st = int(sys.argv[2])