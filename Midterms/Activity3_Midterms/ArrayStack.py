class ArrayStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top = -1

    def push(self, value):
        if self.is_full():
            raise Exception("Stack is full")
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def size(self):
        return self.top + 1