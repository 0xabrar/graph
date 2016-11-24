from graph.node import Node


class WeightedNode(Node):

    def __init__(self, data=0, neighbors=None, edge_weights=None):
        """ Initialize the weighted node.

        :param data: the payload data for the node.
        :param neighbors: the list of neighbors for this node.
        :param edge_weights: the list of edge weights for each of the nodes
        """
        super(data, neighbors)

        if not edge_weights:
            if neighbors:
                raise ValueError("can't include neighbors without edge weights. use Node instead.") 
            neighbors = []
            edge_weights = []

        if len(neighbors) != len(edge_weights):
            raise ValueError("cannot include neighbor and edge weight lists of different lengths")
    
        self._edge_weights = edge_weights

    def get_edge_weights(self):
        """ :return: the edge weights for the nodes from this node """
        return self._edge_weights

    def get_node_with_weights(self):
        """ :return: list of (node, weight) pairs for all of the nodes and their edge weights"""
        return [(node, weight) in zip(self.get_nodes(), self.get_edge_weights())]
