from collections import deque
from graph.graph import Graph


def dfs(node, result=None, discovered=None):
    """ Used to recursively compute dfs on a node using
        a result and discovered set. Assumes that the graph is disconnected.

        :param node: the node to perform dfs on
        :param result: the existing result list
        :param discovered: the set of visited nodes so far
        :return: a list for the dfs traversal starting at Node node
    """

    # don't want users to pass in a graph, but in case they do
    if isinstance(node, Graph):
        node = node.get_nodes()[0]

    if node is None:
        return []

    if discovered is None:
        discovered = set()

    if result is None:
        result = []

    discovered.add(node)
    result.append(node)

    for neighbor in node.get_neighbors():
        if neighbor not in discovered:
            dfs(neighbor, result, discovered)

    return result


def bfs(node):
    """ Return a list of the breadth first search traversal of a node.
        Assumes that the graph is disconnected.

    :param node: the node to perform bfs on
    :return: a list for the bfs traversal starting at Node node
    """

    # don't want users to pass in an instance of Graph, but if they do
    if isinstance(node, Graph):
        node = node.get_nodes()[0]

    if node is None:
        return []

    result = []
    visited = set()
    queue = deque()

    queue.append(node)
    visited.add(node)

    while queue:
        current = queue.popleft()
        for neighbor in current.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

        result.append(current)

    return result
