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

    def reversed(self):
        l = LinkedList()

        current_node = self.last

        while current_node:
            l.append(current_node.value)
            current_node = current_node.prev

        return l

    def reverse(self):
        # in-place
        self.first, self.last = self.last, self.first

        current_node = self.first

        while current_node:
            current_node.next, current_node.prev = current_node.prev, current_node.next
            current_node = current_node.next

    def delete_node(self, node):
        prev = node.prev # None
        next = node.next # [7]

        if prev:
            prev.next = next
        else:
            # node is the first node of the list
            self.first = next

        if next:
            next.prev = prev
        else:
            self.last = prev

    # remove all elements for which func returns true
    def remove_where(self, func):
        current_node = self.first

        while current_node:
            if func(current_node.value):
                self.delete_node(current_node)

            current_node = current_node.next

    def insert_before(self, old_node, new_value):
        new_node = LinkedListNode(new_value, old_node.prev, old_node)
        prev = old_node.prev

        if prev:
            prev.next = new_node
        else:
            self.first = new_node

        old_node.prev = new_node


l = LinkedList()
l.prepend(15)
l.prepend(0)
l.append("world")
l.append(1)
l.prepend("hello")
l.prepend(7)

# LinkedList([31, 7, 0, 15, 1, 8, 100])

# is_even = lambda n: n % 2 == 0
# l.remove_where(is_even) #

# LinkedList([31, 7, 15, 1])

# print l

# l.reverse()

# print l # <- reversed list

# [7,"hello",0,15,"world",1]
