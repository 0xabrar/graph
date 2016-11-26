from graph.node import Node


class WeightedNode(Node):
    """ Used for representing weighted nodes that are part of a graph.
    Includes edge_weights, which is a list of all of the node neighbor
    edge weights.
    """

    def __init__(self, data=0, neighbors=None, edge_weights=None):
        """ Initialize the weighted node.

        :param data: the payload data for the node.
        :param neighbors: the list of neighbors for this node.
        :param edge_weights: the list of edge weights for each of the nodes
        """
        super().__init__(data, neighbors)

        if neighbors is None:
            neighbors = []
            edge_weights = []

        if edge_weights is None:
            raise ValueError(
                "can't include neighbors without edge weights. " +
                "use Node instead.")

        if len(neighbors) != len(edge_weights):
            raise ValueError("cannot include neighbor and edge weight" +
                             "lists of different lengths")

        self.edge_weights = edge_weights

    def get_neighbors_with_weights(self):
        """ :return: list of (node, weight) pairs for all of
                the nodes and their edge weights"""
        return [(node, weight) for (node, weight) in zip(
            self.get_neighbors(), self.get_edge_weights())]
