class Node:
    """A node in a singly linked stack."""
    def __init__(self, element, next_node=None):
        self.element = element
        self.next = next_node


class LinkedStack:
    """A stack implemented using a singly linked list."""
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, element):
        """Push an element onto the stack."""
        new_node = Node(element, self.head)
        self.head = new_node
        self.size += 1

    def pop(self):
        """Pop the top element from the stack."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        result = self.head.element
        self.head = self.head.next
        self.size -= 1
        return result

    def top(self):
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("Top from an empty stack")
        return self.head.element
