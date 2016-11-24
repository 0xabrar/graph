class Node():

    def __init__(self, data=0, neighbors=None, edge_weights=None):
        """ Initialize the node with some data and neighbors.

        :param data: the payload of the node
        :param neighbors: the neighbors of a node passed as a list
        :param edge_weights: the edge weights of the node passed in as a list
                             the index of the edge_weights list corresponds
                             with the index of neighbor list
        """
        if neighbors is None:
            neighbors = []

        if edge_weights is None:
            edge_weights = []

        self.data = data
        self.neighbors = neighbors
        self.edge_weights = edge_weights

    def add_neighbor(self, neighbor):
        """ Add a neighbor to this node.

        :param neighbor: the neighbor to add
        """
        self._check_valid_node(neighbor)
        self.neighbors.append(neighbor)

    def add_edge_weight(self, weight):
        """ Adds weight of the edge.

        :param weight: the weight(float) to be added
        """

        self._check_valid_weight(weight)
        self.edge_weights.append(weight)

    def remove_neighbor(self, neighbor):
        """ Remove a neighbor from this node.

        :param neighbor: the neighbor to remove
        """

        self._check_valid_node(neighbor)
        for ind, node in enumerate(self.neighbors):
            if node is neighbor:
                self.neighbors.pop(ind)

    def _check_valid_node(self, node):
        """ Checks if a node is valid by asserting that it is not None
            and an instance of Node.

        :param node: the node to check
        """
        if not node or not isinstance(node, Node):
            raise ValueError("must insert a node object as a neighbor")

    def _check_valid_weight(self, weight):
        """ Checks if a weight is valid by asserting that it is a float value.

        :param weight: the weight value to check
        """
        if not isinstance(weight, float):
            raise ValueError("must insert a float value for weight")

    def get_neighbors(self):
        """ Return this node's neighbors. """
        return self.neighbors

    def get_edge_weights(self):
        """ Return this node's edge_weights. """
        return self.edge_weights
