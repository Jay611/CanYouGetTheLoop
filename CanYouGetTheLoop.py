"""
You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop.

For example in the following picture the tail's size is 3 and the loop size is 11.
"""
import sys

sys.setrecursionlimit(5000)


class Node:
    def __init__(self):
        self.next = None
        self.link_count = 0


def loop_size(node):
    if node.next is not None:
        if node.next.link_count == 0:
            node.next.link_count = node.link_count + 1
            return loop_size(node.next)
        else:
            return node.link_count - node.next.link_count + 1
    else:
        return -1


def create_chain(num_of_node, size_of_loop):
    nodes = [Node() for _ in range(num_of_node)]
    for node, next_node in zip(nodes, nodes[1:]):
        node.next = next_node
    nodes[num_of_node - 1].next = nodes[num_of_node - size_of_loop]
    return nodes[0]


# Make a short chain with a loop of 3
node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(loop_size(node1))
# Test.assert_equals(loop_size(node1), 3, 'Loop size of 3 expected')


# Make a longer chain with a loop of 29
nodes = [Node() for _ in range(50)]
for node, next_node in zip(nodes, nodes[1:]):
    node.next = next_node
nodes[49].next = nodes[21]
print(loop_size(nodes[0]))
# Test.assert_equals(loop_size(nodes[0]), 29, 'Loop size of 29 expected')

# Make a very long chain with a loop of 1087
chain = create_chain(3904, 1087)
print(loop_size(chain))
# Test.assert_equals(loop_size(chain), 1087, 'Loop size of 1087 expected')
