"""
Question from https://www.hackerrank.com/challenges/bfsshortreach

Given an undirected graph consisting of NN nodes (labelled 1 to N)
where a specific given node SS represents the start position and an edge
between any two nodes is of length 66 units in the graph.

It is required to calculate the shortest distance from start position
(Node S) to all of the other nodes in the graph.

Note 1: If a node is unreachable , the distance is assumed as −1−1.
Note 2: The length of each edge in the graph is 66 units.
"""

test_case = int(raw_input())

data = []

for i in xrange(0, test_case):
    MN = (map(int, raw_input().split()))
    data.append(MN)
    N = MN[1]
    for i in xrange(0, N):
        data.append((map(int, raw_input().split())))
    data.append((map(int, raw_input().split())))

    class Node(object):
        def __init__(self, number):
            self.neighbours = []
            self.distance_from_start = -1
            self.number = number
            self.is_start = False

    N = data[0][0]
    M = data[0][1]

    # take N and M from the first line
    # create a list of N Node objects
    nodes = [Node(i + 1) for i in xrange(N)]

    for edge in data[1:M+1]:
        # data[1:M+1] = [[1,2],[1,3]]
        # edge = [1,2]
        x, y = edge  # this edge connects node x with node y
        nodes[x - 1].neighbours.append(nodes[y - 1])
        nodes[y - 1].neighbours.append(nodes[x - 1])

    S = data[-1][0]

    start_node = nodes[S - 1]
    start_node.is_start = True
    start_node.distance_from_start = 0

    node_queue = [start_node]

    while len(node_queue) > 0:
        current_node = node_queue.pop()

        current_node_neighbours = current_node.neighbours
        for neighbour in current_node_neighbours:
            if neighbour.distance_from_start < 0:
                neighbour.distance_from_start = current_node.distance_from_start + 6
                node_queue.insert(0, neighbour)

    for node in nodes:
        if node.distance_from_start == 6 or node.distance_from_start == -1:
            print node.distance_from_start,
    print

    data = []
