################# To know how to use this program execute in the command line: ################
#################                   python lab1.py -h                          ################

import argparse, random, pprint
from graph import make_graph_obj, check_path, is_connected, euler_circuit

parser = argparse.ArgumentParser(description='Graph processing')
parser.add_argument('graph_data', metavar='edges_file', type=str, help='Path to file containing the graph edges')
parser.add_argument('--route',metavar="route-file", type=str, required=False, help='Path to file containing a route to test')
parser.add_argument('--dpf-check', action="store_true", required=False, help='Check if the graph is fully connected')
parser.add_argument('--show', action="store_true", required=False, help='Check graph structure')
parser.add_argument('--circuit', action="store_true", required=False, help='Determine if exist an euler circuit this option has implicit the --dpf-check')
parser.add_argument('--add-conn', action="store_true", required=False, help='Add new connections')


args = parser.parse_args()
graph_edges = args.graph_data
route  = args.route
check = args.dpf_check
show = args.show
circuit = args.circuit
add_conn = args.add_conn

airports, graph_obj = make_graph_obj(graph_edges)

if add_conn:
    print("Adding connections")
    f = open("datos.txt", "a")
    f.write("\nSan Diego,Atlanta")
    f.write("\nNew York,St. Louis")
    f.write("\nMinneapolis,Phoenix")
    f.close()

def check_connected():
    vertex = random.choice(airports)
    connected = is_connected(graph_obj, vertex)
    if connected: 
        return True
    else: 
        return False
# Exercise 2
if route:
    print("\nPath exist:",check_path(graph_obj, route))

# Exercise 3

if check:
    if check_connected(): print("The graph is connected")
    else: print("The graph is not connected")

if show:
    pprint.pprint(graph_obj)

#  Exercise 4

if circuit:
    connected = check_connected()
    if euler_circuit(graph_obj) and connected:
        print("\nIt is possible to find an euler circuit")
    else:
        print("\nIt is not possible to find an euler circuit")

# Exercise 5

odds = [graph_obj[v]["name"] for v in graph_obj if len(graph_obj[v]["vertices"]) % 2 != 0]

""" To make the graph to contain an euler circuit we have to modify the conexion of the airports 
describes in the variable odds(make a print of this var to see)
"For this we add the following conexions:
    1. San Diego -> Atlanta
    2. New York -> St. Louis
    3. Minneapolis -> Phoenix

If you want to add this connections to the current edges file and check afterwards run the following command in the command line:
    python lab1.py datos.txt --add-con
Then check if it is an euler circuit with:
    python lab1.py datos.txt --circuit
"""



# Exercise 6

""" It is not possible in this graph to find an euler path, for this to be possible we have 
to guarantee that every vertex in the graph has a pair number of vertices attached to itexcept 
New York and Atlanta which are the start and the end of the path, for this we make the following connections:

    1. San Diego -> Phoenix
    2. St. Louis -> Minneapolis 

That will guarantee that our graph includes an euler path that start in New York and finish in Atlanta"""