import pytest
from graph import Node


sample_data = [
    (Node(), 0, [])
]


@pytest.mark.parametrize("node,expected_data,expected_neighbors",
                         sample_data)
def test_creation_other(node, expected_data, expected_neighbors):
    assert node.data == expected_data
    assert node.neighbors == expected_neighbors


def test_node_creation():
    node = Node()
    assert node.data == 0
    assert node.neighbors == []

    second_node = Node(3)
    assert second_node.data == 3
    assert second_node.neighbors == []

    neighbors = [node, second_node]
    neighbor_node = Node(3, neighbors)
    assert neighbor_node.data == 3
    assert neighbor_node.neighbors is neighbors


def test_add_neighbor():
    first = Node(2)
    second = Node(3)
    third = Node(4)

    node = Node(5)
    node.add_neighbor(first)
    node.add_neighbor(second)
    node.add_neighbor(third)

    expected_neighbors = [first, second, third]
    assert node.neighbors == expected_neighbors
