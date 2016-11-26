class Node(object):

    def __init__(self, data=0, neighbors=None):
        """ Initialize the node with some data and neighbors.

        :param data: the payload of the node
        :param neighbors: the neighbors of a node passed as a list
        :param edge_weights: the edge weights of the node passed in as a list
                             the index of the edge_weights list corresponds
                             with the index of neighbor list
        """
        if neighbors is None:
            neighbors = []

        self.data = data
        self.neighbors = neighbors

    def add_neighbor(self, neighbor):
        """ Add a neighbor to this node.

        :param neighbor: the neighbor to add
        """
        self._check_valid_node(neighbor)
        self.neighbors.append(neighbor)

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
