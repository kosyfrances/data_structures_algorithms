# ((1 + (7 * 2)) + (3 * 4))

#                            a +
#                             / \
#                            /   \
#                           /     \
#                        b +       * c
#                         / \     / \
#                        /   \  f3   4 g
#                     d 1   e *
#                            / \
#                          h7   2i


# a.evaluate() -> 27
#    b.evaluate() -> 15
#        d.evaluate() -> 1
#        e.evaluate() -> 14
#            h.evaluate() -> 7
#            i.evaluate() -> 2
#    c.evaluate() -> 12
#        f.evaluate() -> 3
#        g.evaluate() -> 4

# ((1 + (x * 2)) + (3 * y))
# a.evaluate(x = 19, y = -1)


class Node(object):
    """Creates a node with children."""

    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data

    def evaluate(self, **kwargs):
        raise NotImplementedError()


class OperationNode(Node):
    """Creates a node for operators with access to evaluation afterwards."""

    operations = {
        "+": lambda a, b: a + b,
        "*": lambda a, b: a * b
    }

    def __init__(self, left, right, operator):
        super(OperationNode, self).__init__(left, right, operator)

    def evaluate(self, **kwargs):
        """Evaluate tree expression recursively."""
        operator_func = self.operations[self.data]

        return operator_func(self.left.evaluate(**kwargs), self.right.evaluate(**kwargs))


class ConstantNode(Node):
    """Creates a node without children."""

    def __init__(self, value):
        super(ConstantNode, self).__init__(None, None, value)

    def evaluate(self, **kwargs):
        return self.data


class VariableNode(Node):
    """
    Creates a variable like x or y which can be replaced with actual
    numbers during evaluation.
    """

    def __init__(self, variable):
        super(VariableNode, self).__init__(None, None, variable)

    def evaluate(self, **kwargs):
        return kwargs[self.data]

# h = ConstantNode(7)
h = VariableNode("x")

i = ConstantNode(2)
e = OperationNode(h, i, "*")
d = ConstantNode(1)
b = OperationNode(d, e, "+")

f = ConstantNode(3)
# g = ConstantNode(4)
g = VariableNode("y")
c = OperationNode(f, g, "*")

a = OperationNode(b, c, "+")

print a.evaluate(x=7, y=4)
# kwargs = { "x": 7, "y": 4}
