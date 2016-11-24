from graph.node import Node
from random import sample, randint, choice


class Graph():

    def get_nodes(self):
        """
        :return the list of nodes from the graph
        """
        return self._graph

    def __init__(self, num_nodes, directed=False, weighted=False, cycles=0):
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
        self._graph = []

        available = []
        # default node domain is integers from 0...num_nodes
        node_domain = [x for x in range(num_nodes)]
        for x in sample(node_domain, num_nodes):
            available.append(Node(x))

        self._generate_graph(available)
        if cycles > 0:
            self._set_cycles(cycles)

    def _set_cycles(self, cycles=0):

        for _ in range(cycles):
            source = choice(self._graph)
            destination = choice(self._graph)
            source.add_neighbor(destination)
            destination.add_neighbor(source)

    def _generate_graph(self, available):
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
