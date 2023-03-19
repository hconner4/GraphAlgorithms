import mip


def read_dimacs(filename):
    with open(filename) as f:
        lines = f.readlines()
    edges = []
    for line in lines:
        parts = line.strip().split('\t')
        u, v = int(parts[0]), int(parts[1])
        edges.append((u, v))
    num_vertices = edges[0][0]
    edges.pop(0)
    adjacency = [[0] * num_vertices for _ in range(num_vertices)]
    for edge in edges:
        adjacency[edge[0]-1][edge[1]-1] = 1
        adjacency[edge[1]-1][edge[0]-1] = 1
    return adjacency

def max_clique(filename):
    adjacency = read_dimacs(filename)
    num_vertices = len(adjacency)

    model = mip.Model()
    x = [model.add_var(var_type=mip.BINARY) for i in range(num_vertices)]

    # Objective function: maximize the sum of x_i
    model.objective = mip.maximize(mip.xsum(x))

    # Constraint: every pair of vertices in the clique must be adjacent
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if adjacency[i][j] == 1:
                model += x[i] + x[j] <= 1

    status = model.optimize()

    if status == mip.OptimizationStatus.OPTIMAL:
        max_clique = [i+1 for i in range(num_vertices) if x[i].x >= 0.99]
        print(f"Largest clique: {max_clique}")
    else:
        print("No clique found.")


# Example usage
max_clique('graph2_cc.txt')
