def min_max_dens(graph):
    #This is assuming every vertice has an edge and is listed in the dimacs file
    #I was unaware there could be isolated vertices

    import pandas as pd
    import collections
    import operator

    #Read in Text file
    graph = pd.read_csv(graph, sep=r'\n|\t', engine='python', header=None)
    #get number of edges and vertices from top row of dataframe
    numEdge = graph[1].iloc[0]
    numVert = graph[0].iloc[0]
    #remove top row of data frame
    graph = graph.iloc[1:]
    
    #find the max number of times a vertice occurs in the datafame giving the max degree
    max = "Max: " + str(graph.apply(pd.Series.value_counts).sum(axis=1).max())
    #find the min number of times a vertice occurs in the datafame giving the min degree
    min = "Min: " + str(graph.apply(pd.Series.value_counts).sum(axis=1).min())
    
    dens = "Density: " +str(numEdge/(numVert*(numVert-1)/2))
    print(max, min, dens)

filePath = input("Please enter filepath: ")
min_max_dens(filePath)