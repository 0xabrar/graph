# Graph

**Graph** is a minimal Python library which provides you with a simple API to generate, visualize, and inspect graphs - so you can skip the tedious work of mocking up test graphs. If you create a function for performing a traversal on a graph, you can pass your function as an argument to our of our helpers to visualize your traversal.

# Installation
You'll need to start with cloning the module.  


``` bash
$ git clone https://github.com/abrarisme/graph/
$ python graph/setup.py install
```
    
# Getting Started
By default, **Graph** uses the following class to represent a graph.  

``` python
class Graph(object):
    
    def __init__(self, num_nodes, directed=False, weighted=False, cycles=0):
        self._directed = directed
        self._weighted = weighted
        self._graph = graph  
```
You can call `graph.get_nodes()` to return the list of `Node` within the graph. Usually,
you'll want to work with Node objects themselves, and you can find their representation below.

``` python
class Node(object):
    
    def __init__(self, data, neighbors=None):
        self.data = data
        self.neighbors = neighbors
```
            
Generate, pretty-print, and visualize all sorts of graphs:   

``` python
from graph import Graph, display_graph, display_traversal, pprint, inspect
from my_code import my_topological_sort

# generate an undirected graph with no cycles or weighting (10 nodes)
graph = Graph(10) 

# make a weighted, directed graph with 2 cycles (10 nodes)
directed_graph = Graph(10, directed=True, weighted = True, cycles=2)

# pretty-print out the graphs in stdout
pprint(graph)
pprint(directed_graph)

# display relevant properties of the graph
inspect(graph)

# display the regular graph
display_graph(graph)

# open a figure and display the step-by-step BFS traversal of a graph
display_traversal(graph)

# display the traversal of your own algorithm
display_traversal(graph, my_topological_sort)
```
