import sys
import re

def make_graph_obj(edges_file):
    file = open(edges_file)
    content = file.read()
    file.close()
    edges = content.split("\n")

    # List with all pair of edges
    edges = [pair.split(",") for pair in edges]

    # Set with unique airports names
    airports = set(re.split("[,|\n]", content))
    airports = list(airports)
    # This object will contain the final structure of the graph
    graph = {}

    for airport in airports:
        graph[airport] = {"vertices":[],"name":airport, "labeled":False}
        for pair in edges:
            if airport in pair:
                graph[airport]["vertices"].append(pair[0] if airport == pair[1] else pair[1])   
    
    return airports, graph

def check_path(graph, file):
    # Find if the path given exist
    route_file = open(file)
    route = route_file.read().strip().split("\n")
    route_file.close()
    print("\n"+"->".join(route))
    for e in range(len(route)-1):
        adjacent_airports = graph[route[e]]["vertices"]
        if route[e+1] not in adjacent_airports:
            return False
    else: return True

# Input: A graph G and a vertex v of G
# Output: All vertices reachable from v get labeled as discovered
# procedure DFS(G,v):
#     label v as discovered
#     for all directed edges from v to w that are in G.adjacentEdges(v) do
#         if vertex w is not labeled as discovered then
#             recursively call DFS(G,w)

def is_connected(graph, vertex):
    # Appy the DPF algorithm
    vertices = graph[vertex]["vertices"]
    graph[vertex]["labeled"] = True
    for v in vertices:
        if graph[v]["labeled"] == False:
            is_connected(graph, v)
    for airport in graph:
        if graph[airport]["labeled"] == False:
            return False
            break
    else:
        return True

def euler_circuit(graph):
    for node in graph:
        if len(graph[node]["vertices"]) % 2 != 0:
            return False
    return True

