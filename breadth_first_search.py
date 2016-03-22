test_input = """2
4 2
1 2
1 3
1
3 1
2 3
2"""

input_data = test_input.splitlines()
test_case = int(input_data.pop(0)[0])

splitted_data = []
new_list = []

for i in input_data:
    s = (map(int, i.split()))
    new_list.append(s)
    if len(s) == 1:
        splitted_data.append(new_list)
        new_list = []

print splitted_data

# test_cases = data.pop(0)[0]
# slice_end = (i for i in data if len(i) == 1)

# splitted_data = [data[data[0]:i + n] for i in xrange(0, len(input), n)]
# [[4,2],[1,2],[1,3],[1]]
#    0     1     2    3
#         [.......]
# [1:M+1] = [1:3]

# 1S   2     4
# O----O     O
# |
# |
# 3

for i in range(0, test_case):
    data = splitted_data.pop(0)
    print data

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

    for i, node in enumerate(nodes):
        print "Node", i + 1
        print "Neighbours:", ", ".join(str(neighbour.number) for neighbour in node.neighbours)
        if node.is_start:
            print "This is the start node"
        print

    node_queue = [start_node]

    while len(node_queue) > 0:
        print "queue = [" + ", ".join(str(node.number) for node in node_queue) + "]"
        current_node = node_queue.pop()
        print "Checking node", current_node.number, "- Distance from start node:",
        current_node.distance_from_start

        current_node_neighbours = current_node.neighbours
        for neighbour in current_node_neighbours:
            print "  Neighbour: ", neighbour.number
            if neighbour.distance_from_start < 0:
                neighbour.distance_from_start = current_node.distance_from_start + 6
                print "  Neighbour's distance from start:", neighbour.distance_from_start
                node_queue.insert(0, neighbour)
                print "  adding node", neighbour.number, "to queue"
            else:
                print "  Skipping because this node has been reached before"

    print
    for node in nodes:
        print "Node", node.number, "has distance", node.distance_from_start,
        "from the start"
        if node.distance_from_start == 6 or node.distance_from_start == -1:
            print node.distance_from_start,


    # Checking node 3 - Distance from start node: 12
    #  Neighbour:  2
    #  Skipping because this node has been reached before
    #  Neighbour:  5
    #  Neighbour's distance from start: 18
    #  adding node 5 to queue

    """5 4
    1 2
    2 3
    3 5
    1 4
    1"""

    # 1    2    3    5
    # O----O----O----O
    # |
    # |
    # |
    # O 4

    # 1 is start node
    # checking node 1 - distance from start: 0
    #   Neighbour: 2
    #      Neighbour's distance from start: 6
    #      adding node 2 to queue
    #   Neighbour: 4
    #      Neighbour's distance from start: 6
    #      adding node 4 to queue
    #
    # queue = [node2, node4]

    # next while loop iteration:
    # checking node 2 - distance from start: 6
    #   Neighbour: 3
    #      Neighbour's distance from start: 12
    #      adding node 3 to the queue
    #   Neighbour: 1
    #      skipping because this node has been reached before

    # queue = [node4, node3]
    # .... handle node 4 ....
    # queue = [node3]

    # checking node 3 - distance from start: 12
    #   Neighbour: 5
    #      Neighbour's distance from start: 18
    #      adding node 3 to the queue
    #   Neighbour: 2
    #      skipping because this node has been reached before
