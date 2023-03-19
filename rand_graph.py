import random
import sys

def generate_random_graph(n: int, p: float, filename: str):
    # Create adjacency matrix for empty graph
    adj = [[0 for j in range(n)] for i in range(n)]

    # Add edges with probability p
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                adj[i][j] = adj[j][i] = 1

    #turn matrix into dimacs
    edges = []
    for i in range(len(adj)):
        for j in range(len(adj)):
            if adj[i][j] == 1:
                edges.append((i, j))

    # Open the output file for writing the edges
    with open(filename, 'w') as f:
        # Write each edge to a new line in the output file
        f.write(f"{len(adj)}  {len(edges)} \n")
        for edge in edges:
            
            f.write(f"{edge[0]} {edge[1]}\n")

n = int(sys.argv[1])
filename = sys.argv[2]
randgraph = generate_random_graph(n=14, p=.15, filename=filename)
