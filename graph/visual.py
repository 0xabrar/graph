from collections import deque
from copy import deepcopy

import matplotlib.pyplot as plt
import networkx as nx

from graph.node import Node
from graph.graph import Graph
from graph.traversals import dfs


def _generate_traversal_colors(graph, graph_traversal):
    """ Generate a list of list corresponding to the change in colors
        as we go through a traversal on the graph.

    :param graph: the graph that is being traversed
    :param graph_traversal: the node values from a graph traversal
        in order as a list
    """
    color_transitions = []

    for i in range(1, len(graph_traversal) + 1):
        current_traversed = graph_traversal[:i]
        nodes = nx.nodes(graph)
        colors = ["g" if node in current_traversed else "b" for node in nodes]
        color_transitions.append(deepcopy(colors))

    return color_transitions


def display_graph(graph):
    """ Display a graph.

        :param graph: the graph to display (in Node class form)
    """
    if isinstance(graph, Graph):
        graph = graph.get_nodes()[0]

    # converting to networkx representation
    graph = convert_node(graph)
    nx.draw_networkx(graph)
    return


def display_traversal(graph, func=dfs):
    """ Display a traversal on a graph given the function for
        traversing the graph.

    :param graph: the graph that is being traversed (in Node class form)
    :param func: the function for performing the traversal
    """
    if isinstance(graph, Graph):
        graph = graph.get_nodes()[0]

    graph_traversal = func(graph)
    graph = convert_node(graph_traversal)
    graph_traversal = [node.data for node in graph_traversal]

    plt.ion()
    color_transitions = _generate_traversal_colors(graph, graph_traversal)
    layout = nx.spring_layout(graph)  # need to keep positions constant

    for colors in color_transitions:
        nx.draw_networkx(graph, node_color=colors, pos=layout)
        plt.pause(1)
        plt.clf()

    return


def _convert_node(node, visited=None):
    """ Performs BFS on the given node in order to discover of the edge
    pairs that exist from this node point.

    :param node: the source node to get edges from
    :param visted: a set indicating the visited values in traversal
    """
    edges = []
    if visited is None:
        visited = set()
    queue = deque()

    if node not in visited:
        queue.append(node)

    while queue:
        current_node = queue.popleft()
        visited.add(current_node)

        for neighbor in current_node.get_neighbors():
            edges.append([current_node, neighbor])
            if neighbor not in visited:
                queue.append(neighbor)

    return edges


def convert_node(node_list):
    """Convert a Node class graph representation into an
        networkx graph representation.

    :param node_list: the list of nodes from the graph to covert.
        optional to just pass single node.
    """
    if isinstance(node_list, Node):
        node_list = [node_list]

    visited = set()
    edges = []
    for node in node_list:
        edges.extend(_convert_node(node, visited))

    graph = nx.Graph()
    for (u, v) in edges:
        graph.add_edge(u.data, v.data)
    return graph
