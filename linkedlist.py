class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f"<{type(self)} head={self.head.data} tail={self.tail.data}>"

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = None
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = None

    def length(self):

        current = self.head
        counter = 0

        while current is not None:
            counter += 1
            current = current.next

        return counter

    # def delete(self, node):
    #     print(node)
    #     print(node.data)
    #     print(node.next)
    #     node.data = node.next.data
    #     node.next = node.next.next
