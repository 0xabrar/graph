from graph.graph import Graph
from graph.visual import convert_node
from graph.traversals import dfs, bfs

import networkx as nx


def pprint(graph):
    """ Display the adjacency list listing for a graph.

    :param graph: the graph to pretty print
    """
    nodes = [(node.data, [x.data for x in node.neighbors])
             for node in graph.get_nodes()]
    for node, neighbors in nodes:
        print(node, neighbors)


def has_cycle(graph):
    """ Find out whether a graph has a cycle.

    :param graph: the graph to check for cycles
    :return: True if the graph has a cycle, False otherwise
    """
    if isinstance(graph, Graph):
        graph = convert_node(graph.get_nodes())

    try:
        nx.find_cycle(graph) != []
        return True
    except nx.exception.NetworkXNoCycle:
        return False


def print_data(node_list):
    """ Prints out the payload information inside of a node list.

    :param: node_list: the node list to print
    """
    for node in node_list:
        print(node.data)


def get_data(node_list):
    """ Return the payload data from a node list.

    :param node_list: the node list to retrieve payload data from
    :return: list of data
    """
    return [node.data for node in node_list]


def _inspect_print(properties):
    """ Pretty print the inspect values on the graph.

    :param properties: the properties to print
    """
    print("{")
    for (key, value) in properties.items():
        print("\t", key, ":", value)
    print("}")


def inspect(graph):
    """ Checks through a graph to print off it's relevant properties.

    :param graph: the Graph to inspect
    """
    properties = {}
    networkx_graph = convert_node(graph.get_nodes())
    properties["has_cycle"] = has_cycle(networkx_graph)

    graph_node = graph.get_nodes()[0]
    properties["dfs_traversal"] = get_data(dfs(graph_node))
    properties["bfs_traversal"] = get_data(bfs(graph_node))
    _inspect_print(properties)
