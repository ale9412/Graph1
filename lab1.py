import argparse, random, pprint
from graph import make_graph_obj, check_path, is_connected

parser = argparse.ArgumentParser(description='Graph processing')
parser.add_argument('graph_data', metavar='file', type=str, help='Path to file containing the graph edges')
parser.add_argument('--route',metavar="route-file", type=str, required=False, help='Path to file containing a route to test')
parser.add_argument('--dpf-check', action="store_true", required=False, help='Check if the graph is fully connected')
parser.add_argument('--show', action="store_true", required=False, help='Check graph structure')
parser.add_argument('--ecircuit', action="store_true", required=False, help='Find the path that includes')


args = parser.parse_args()
graph_edges = args.graph_data
route  = args.route
check = args.dpf_check
show = args.show

airports, graph_obj = make_graph_obj(graph_edges)


if route:
    print("\nPath exist:",check_path(graph_obj, route))

if check:
    vertex = random.choice(airports)
    is_connected(graph_obj, vertex)
    for airport in airports:
        if graph_obj[airport]["labeled"] == False:
            print("\nThe graphic is not connected" )
            break
    else:
        print("\nThe graphic is connected")

if show:
    pprint.pprint(graph_obj)