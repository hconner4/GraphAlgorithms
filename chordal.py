# Define a function to check if a graph is chordal
import re
import numpy as np

def adj_mat(graph):
    """
    Convert a DIMACS format file into an adjacency matrix.
    """
    with open(graph, "r") as f:
        data = f.read()
        data = re.findall('\d+', data)

    # Perform conversion
    data1 = [int(i) for i in data]

    # Remove first 3 entries in graph
    num_nodes = data1.pop(0)
    num_edges = data1.pop(0)

    list1 = [data1[i:i+2] for i in range(0, len(data1), 2)]

    # Create an empty adjacency matrix with n x n size
    adj_matrix = np.zeros((num_nodes, num_nodes), dtype=np.int)

    for l in list1:
        u, v = l
        adj_matrix[u-1][v-1] += 1
        adj_matrix[v-1][u-1] += 1

    return adj_matrix



def is_chordal(adj_matrix):
    # Get the number of vertices in the graph
    n = len(adj_matrix)
    
    # Initialize a set to store the vertices
    vertices = set(range(n))
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {v: set() for v in vertices}
    
    # Compute the neighbor sets for each vertex
    for i in range(n):
        for j in range(i+1, n):
            if adj_matrix[i][j]:
                neighbors[i].add(j)
                neighbors[j].add(i)
    
    # Initialize a set to store the remaining vertices to be eliminated
    remaining_vertices = set(vertices)
    # Initialize a list to store the elimination ordering
    elimination_order = []
    
    # Iterate until all vertices have been eliminated
    while remaining_vertices:
        # Find a vertex with minimum degree
        v = min(remaining_vertices, key=lambda x: len(neighbors[x]))
        
        # Eliminate the vertex and add it to the elimination ordering
        remaining_vertices.remove(v)
        elimination_order.append(v)
        
        # Find all the non-neighbor pairs in the neighborhood of v
        non_neighbor_pairs = [(u, w) for u in neighbors[v] for w in neighbors[v] if u != w and w not in neighbors[u]]
        
        # Add a chord between each non-neighbor pair
        for u, w in non_neighbor_pairs:
            if u in neighbors[w]:
                return False
            neighbors[u].add(w)
            neighbors[w].add(u)
    
    # If the elimination ordering is a perfect elimination ordering, the graph is chordal
    for i, v in enumerate(elimination_order[:-1]):
        neighbors_v = neighbors[v]
        remaining_neighbors = set(neighbors_v).intersection(elimination_order[i+1:])
        for w in remaining_neighbors:
            if w not in neighbors_v:
                return False
    return True


graph = sys.argv[1]
adj_matrix = adj_mat(graph)
is_chordal(adj_matrix)