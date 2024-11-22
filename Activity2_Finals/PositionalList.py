class Node:
    """A node in the doubly linked positional list."""
    def __init__(self, element, prev=None, next=None):
        self.element = element
        self.prev = prev
        self.next = next


class PositionalList:
    """Doubly linked list supporting positional access."""
    def __init__(self):
        self.header = Node(None)
        self.trailer = Node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _insert_between(self, element, predecessor, successor):
        """Add element between two existing nodes and return new node."""
        new_node = Node(element, predecessor, successor)
        predecessor.next = new_node
        successor.prev = new_node
        self.size += 1
        return new_node

    def add_last(self, element):
        """Add element to the end of the list."""
        return self._insert_between(element, self.trailer.prev, self.trailer)

    def to_list(self):
        """Return all elements in the list as a Python list."""
        result = []
        current = self.header.next
        while current != self.trailer:
            result.append(current.element)
            current = current.next
        return result

    def insertion_sort(self, ascending=True):
        """Sort the list using insertion sort algorithm."""
        if self.size < 2:
            return

        current = self.header.next.next
        while current != self.trailer:
            key = current.element
            prev = current.prev

            while prev != self.header and ((key < prev.element) if ascending else (key > prev.element)):
                prev.next.element = prev.element
                prev = prev.prev

            prev.next.element = key
            current = current.next
