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

def is_line_graph(adj_matrix):
    """
    Given an adjacency matrix, returns True if the corresponding graph is a line graph, False otherwise.
    """
    n = len(adj_matrix)
    for i in range(n):
        degree = sum(adj_matrix[i])
        if degree not in (1, 2):
            return False
    return True



def find_root_graph(line_graph):
    """
    Given the adjacency matrix of a line graph, returns the adjacency list of the corresponding root graph.
    """
    n = len(line_graph)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if line_graph[i][j] == 1:
                edges.append((i,j))

    root_graph = {}
    for edge1 in edges:
        for edge2 in edges:
            if edge1 != edge2 and set(edge1) & set(edge2):
                if edge1 not in root_graph:
                    root_graph[edge1] = set()
                if edge2 not in root_graph:
                    root_graph[edge2] = set()
                root_graph[edge1].add(edge2)
                root_graph[edge2].add(edge1)
    return root_graph

def print_dimacs_graph(root_graph):
    """
    Given the adjacency list of a graph, prints the graph in DIMACS format.
    """
    num_vertices = len(root_graph)
    num_edges = sum(len(adj_list) for adj_list in root_graph.values()) // 2

    # Print the header
    print(f"{num_vertices} {num_edges}")

    # Print the edges
    for vertex, adj_list in root_graph.items():
        for adj_vertex in adj_list:
            if vertex < adj_vertex:  # Avoid printing duplicates
                print(f" {vertex+1} {adj_vertex+1}")

graph = sys.argv[1]
adj_mat(graph)
root_graph = find_root_graph(adj_matrix)
if is_line_graph(adj_matrix):
    print_dimacs_graph(find_root_graph(adj_matrix))
else:
    print('Not a line graph')