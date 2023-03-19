from typing import List, Tuple
import csv

def create_graph(files: List[List[int]], limits: List[Tuple[int, int]]) -> List[List[int]]:
    num_files = len(files)
    num_providers = len(limits)
    V = num_files + num_providers + 2 # add source and sink nodes
    graph = [[0] * V for i in range(V)]

    # add edges between files and providers
    for file_idx, providers in enumerate(files):
        for provider_idx in providers:
            graph[file_idx+1][num_files+provider_idx+1] = 1

    # add edges from source to files
    for file_idx in range(num_files):
        graph[0][file_idx+1] = 1

    # add edges from providers to sink with capacity equal to daily limits
    for provider_idx, limit in limits:
        graph[num_files+provider_idx+1][-1] = limit

    return graph

def bfs(graph: List[List[int]], s: int, t: int, parent: List[int]) -> bool:
    visited = [False] * len(graph)
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)

        for v in range(len(graph)):
            if not visited[v] and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True

    return False

def max_flow(graph: List[List[int]], s: int, t: int) -> int:
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, s, t, parent):
        path_flow = float("Inf")
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u

        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow

def read_storage_locations(file_path):
    with open(file_path, 'r') as f:
        # Read the first line to get the number of files
        num_files = int(f.readline().strip().split('\t')[0])
        
        # Initialize an empty dictionary to store the storage locations
        storage_locations = {}
        
        # Loop over the remaining lines of the file
        for line in f:
            # Split the line by tab to get the file ID and storage provider IDs
            parts = line.strip().split('\t')
            
            # The first part is the file ID
            file_id = int(parts[0])
            
            # The remaining parts are the storage provider IDs
            storage_providers = [int(x) for x in parts[1:]]
            
            # Add the storage providers for this file to the dictionary
            storage_locations[file_id] = storage_providers
            
    return storage_locations

def smart_download(files_file: str, limits_file: str) -> None:
    # read input files
    # with open(files_file, "r") as f:
    #     lines = f.readlines()
    # num_files = int(lines[0])
    # files = [[] for i in range(num_files)]
    # for line in lines[1:]:
    #     u, *v_list = map(int, line.strip().split())
    #     for v in v_list:
    #         files[u-1].append(v-1)
    files = read_storage_locations(files_file)

    with open(limits_file, "r") as f:
        reader = csv.reader(f)
        limits = [tuple(map(int, row)) for row in reader]

    # create graph
    graph = create_graph(files, limits)

    # find maximum flow
    max_flow_val = max_flow(graph, 0, len(graph)-1)

    # determine how many files to download from each provider
    for provider_idx, limit in limits:
        provider_flow = 0
        for file_idx in range(num_files):
            if graph[num_files+provider_idx+1][file_idx+1] == 1:
                provider_flow += 1
        print(f"{provider_idx}: {min(provider_flow, limit)} files")

smart_download(files_file = 'storageLocations.txt', limits_file ='dailyLimits.csv')
read_storage_locations('storageLocations.txt')