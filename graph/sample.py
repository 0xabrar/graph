from graph.node import Node
from graph.graph import display_traversal, convert_node
from graph.traversals import dfs

def sample_convert():
    really_really_last = Node(6)
    really_last = Node(5, [really_really_last])
    last = Node(4, [really_last])
    a = Node(3, [last])
    b = Node(2, [a])
    c = Node(1, [a, b])
    d = Node(0, [c])

    # TODO: change labeling to actual name
    display_traversal(d, dfs)
