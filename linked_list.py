class LinkedListNode:

    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.next = next_node
        self.prev = prev_node


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def prepend(self, value):
        new_first = LinkedListNode(value, None, self.first)
        old_first = self.first

        if old_first:
            # the list was not empty
            old_first.prev = new_first
        else:
            # the list was empty
            self.last = new_first

        self.first = new_first

    def append(self, value):
        new_last = LinkedListNode(value, self.last, None)
        old_last = self.last

        if old_last:
            # the list was not empty
            old_last.next = new_last
        else:
            # the list was empty
            self.first = new_last

        self.last = new_last

    def __repr__(self):
        l = []

        current_node = self.first
        while current_node:

            l.append(current_node.value)
            current_node = current_node.next

        return "LinkedList(" + repr(l) + ")"

    def reverse(self):
        l = []

        current_node = self.last

        while current_node:
            l.append(current_node.value)
            current_node = current_node.prev

        return "LinkedList(" + repr(l) + ")"


l = LinkedList()
l.prepend(15)
l.prepend(0)
l.append("world")
l.append(1)
l.prepend("hello")
l.prepend(7)

# Result will be [7,"hello",0,15,"world",1]
