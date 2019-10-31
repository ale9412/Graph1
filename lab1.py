import argparse, random, pprint
from graph import make_graph_obj, check_path, is_connected, euler_circuit

parser = argparse.ArgumentParser(description='Graph processing')
parser.add_argument('graph_data', metavar='file', type=str, help='Path to file containing the graph edges')
parser.add_argument('--route',metavar="route-file", type=str, required=False, help='Path to file containing a route to test')
parser.add_argument('--dpf-check', action="store_true", required=False, help='Check if the graph is fully connected')
parser.add_argument('--show', action="store_true", required=False, help='Check graph structure')
parser.add_argument('--circuit', action="store_true", required=False, help='Determine if exist an euler circuit this option has implicit the --dpf-check')


args = parser.parse_args()
graph_edges = args.graph_data
route  = args.route
check = args.dpf_check
show = args.show
circuit = args.circuit

airports, graph_obj = make_graph_obj(graph_edges)

def check_connected():
    vertex = random.choice(airports)
    connected = is_connected(graph_obj, vertex)
    if connected: 
        return True
    else: 
        return False

if route:
    print("\nPath exist:",check_path(graph_obj, route))

if check:
    if check_connected(): print("The graph is connected")
    else: print("The graph is not connected")

if show:
    pprint.pprint(graph_obj)


if circuit:
    connected = check_connected()
    if euler_circuit(graph_obj) and connected:
        print("\nIt is possible to find an euler circuit")
    else:
        print("\nIt is not possible to find an euler circuit")

print([graph_obj[v]["name"] for v in graph_obj if len(graph_obj[v]["vertices"]) % 2 != 0])