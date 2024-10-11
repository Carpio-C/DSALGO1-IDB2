class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def length(self):
        return len(self.items)

    def first(self):
        if not self.is_empty():
            return self.items[0]

print('Answer for TABLE:')

Q = Queue()
Q.enqueue(5)
Q.enqueue(3)
print(Q.length())
print(Q.dequeue())
print(Q.is_empty())
print(Q.dequeue())
print(Q.is_empty())
Q.enqueue(7)
Q.enqueue(9)
print(Q.first())
Q.enqueue(4)
print(Q.length())
print(Q.dequeue())





print()
print()

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)


    def is_empty(self):
        return len(self.items) == 0

    def length(self):
        return len(self.items)


print("Answer for 2nd Question:")

Q = Queue()

Q.enqueue(5)
Q.enqueue(3)
print(Q.dequeue())
Q.enqueue(2)
Q.enqueue(8)
print(Q.dequeue())
print(Q.dequeue())
Q.enqueue(9)
Q.enqueue(1)
print(Q.dequeue())
Q.enqueue(7)
Q.enqueue(6)
print(Q.dequeue())
print(Q.dequeue())
Q.enqueue(4)
print(Q.dequeue())
print(Q.dequeue())


