import sys
from collections import deque
import pandas as pd
import numpy as np
import os

def BFS(graph, start):
    from collections import deque
    import pandas as pd
    import numpy as np
    import os

    #assuming txt file is in working directory
    graph = pd.read_csv(graph, sep=r'\n|\t', engine='python', header=None)
    #get number of nodes
    numOfNodes = graph[0].iloc[0]
    #remove header row from dataframe
    graph = graph.iloc[1:]


    #making a list to print out
    #visited = []
    visited = [False] * numOfNodes

    # make an empty queue for bfs
    queue = []
    #start = 0
    # mark gave node as visited and add it to the queue
    #visited[start] = True
    queue.append(start)

    #make list of children
    nodes = list(range(numOfNodes))
    #find the value of each column not containing n where n appears in the row
    #make datafrane for return
    families = pd.DataFrame(columns=['node', 'children'])
    for node in nodes:
        listOfChildren = list(np.array(graph[graph.values == node]).flat)
        #remove n from list and find unique values
        listOfChildren = list(set([ i for i in listOfChildren if i!=node ]))
        #save as dataframe
        families.loc[len(families.index)] = [node, listOfChildren]
        #df.loc[len(df.index)] 
        #print(node , listOfChildren)
        
    families.children = families.children.sort_values()

    cycle = []

    while queue:

        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)
        cycle.append(s)
        #print (s, end = " ")
        visited[s] = True
        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in families[families['node']==s]['children'].iloc[0]:
            #print(i)
            if visited[i] == False and i not in queue:
                queue.append(i)
                #make the printable list?
                
                #visited[i] = True
        #don't let it die if it is not connected
        if not all(visited) and not queue:
            #find first value where visited is false
            queue.append(visited.index(False))
            #visited[visited.index(False)]=True
    print(cycle)

# filePath = input("Please enter file: ")
# start = input("Starting vertice: ")
# start = int(start)
graph = sys.argv[1]
start = int(sys.argv[2])
BFS(graph, start)