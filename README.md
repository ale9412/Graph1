# Graph1 

Program for simple graphic analysis

# Usage

* usage: lab1.py ```[-h] [--route route-file] [--dpf-check] [--show] [--circuit] [--add-conn] ``` <edges_file>

**Graph processing**

* positional arguments:
  1. edges_file             &nbsp;&nbsp;&nbsp;Path to file containing the graph edges

* optional arguments:
  1. ```-h, --help```              Show this help message and exit
  2. ```--route <route-file>```    Path to file containing a route to test
  3. ```--dpf-check```             Check if the graph is fully connected
  4. ```--show```                  Check graph structure
  5. ```--circuit```               Determine if exist an euler circuit this option has implicit the --dpf-check
  6. ```--add-conn```              Add new connections
           
          