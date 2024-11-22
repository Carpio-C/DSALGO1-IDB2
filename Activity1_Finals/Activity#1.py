from collections import deque

from collections import deque
def enqueue(Q, e):
    Q.append(e)

def dequeue(Q):
    if Q:
        return Q.pop(0)
    else:
        raise Exception("Queue is empty")

def push(D, e):
    D.appendleft(e)

def pop(D):
    if D:
        return D.pop()
    else:
        raise Exception("Deque is empty")

D = deque([1, 2, 3, 4, 5, 6, 7, 8])
Q = []


four = D[3]
five = D[4]

D.remove(four)
D.remove(five)

D.insert(3, five)
D.insert(4, four)

print("Dequeue:")
print("D:", list(D))
print("Q:", Q)
print()

print(D)

print()
class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0



D = deque([1, 2, 3, 4, 5, 6, 7, 8])
S = Stack()


for _ in range(3):
    S.push(D.popleft())


S.push(D.popleft())


S.push(D.popleft())


while not S.is_empty():
    D.appendleft(S.pop())



D[3], D[4] = D[4], D[3]

print("Stack:")
print(list(D))
