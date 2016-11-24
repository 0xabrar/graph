from graph.node import Node
from random import sample, randint, choice


class Graph():
    """ Used for representing graphs. Includes a list of Node objects 
        for the graph representation. Holds status for the number of cycles in the graph
        as well as whether it is directed or weighted.
    """

    def get_nodes(self):
        """ :return the list of nodes from the graph """
        return self._graph


    def is_directed(self):
        """ :return: True if the graph is directed, False otherwise. """
        return self._directed


    def is_weighted(self):
        """ :return: True if the graph is weighted, False otherwise. """
        return self._weighted

    
    def get_num_nodes(self):
        """ :return: the number of nodes in the graph. """
        return len(self._graph)


    def get_num_cycles(self):
        """ :return: then number of cycles in the graph. """
        return self._num_cycles


    def has_cycles(self):
        """ :return: True if the graph has cycles, False otherwise. """
        return len(self.get_num_cycles) != 0

    def __init__(self, num_nodes, directed=False, weighted=False, num_cycles=0):
        '''
        :param num_nodes: the number of nodes to include in the graph
        :param directed: True if the graph is directed, False otherwise
        :param weighted: True if the graph is weighted, False otherwise
        :param cycles: True if the graph has cycles, False otherwise

        every node will have between 1 and 3 other edges
        '''

        if num_nodes <= 0:
            raise ValueError("must enter a  number of nodes >= 1")

        self._directed = directed
        self._weighted = weighted
        self._num_cycles = num_cycles
        self._graph = []

        available = []
        # default node domain is integers from 0...num_nodes
        node_domain = [x for x in range(num_nodes)]
        for x in sample(node_domain, num_nodes):
            available.append(Node(x))

        self._generate_graph(available)
        if num_cycles > 0:
            self._set_cycles(num_cycles)

    def _set_cycles(self, num_cycles=0):
        """ Set cycles to the existing graph.

        :param num_cycles: the number of cycles to include in the graph
        """
        for _ in range(cycles):
            source = choice(self._graph)
            destination = choice(self._graph)
            source.add_neighbor(destination)
            destination.add_neighbor(source)

    def _generate_graph(self, available):
        """ From the list of available node values, generate a graph by randomly selecting 
        values for nodes and adding [1, 3] neighbors for each of the nodes. Assumes that 
        the values in the list available are randomly generated.

        :param available: a list of the available values to create the graph (domain)
        """
        open_set = []
        while available or open_set:

            if open_set == []:
                pick = available.pop()
            else:
                pick = choice(open_set)
                open_set = [x for x in open_set if x is not pick]

            n = len(available)
            num_edges = randint(1, 3)
            if num_edges > n:
                num_edges = n

            neighbors = available[n - num_edges:n]
            for neighbor in neighbors:
                pick.add_neighbor(neighbor)
                if not self._directed:
                    neighbor.add_neighbor(pick)

            available = [x for x in available if x not in neighbors]
            open_set.extend(neighbors)
            self._graph.append(pick)
