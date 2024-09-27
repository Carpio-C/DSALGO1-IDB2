class Stack:
    def __init__(s):
        s.items = []

    def push(s, item):
        s.items.append(item)

    def pop(s):
        if not s.is_empty():
            return s.items.pop()
        return None

    def top(s):
        if not s.is_empty():
            return s.items[-1]
        return None

    def is_empty(s):
        return len(s.items) == 0

    def length(s):
        return len(s.items)

print("Stack Data Structure")
print("Answer for TABLE:")
S = Stack()
S.push(5)
S.push(3)
print(S.length())
print(S.pop())
print(S.is_empty())
print(S.pop())
print(S.is_empty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(S.length())
print(S.pop())
S.push(6)
S.push(8)
print(S.pop())
print()

class Stack:
    def __init__(s):
        s.items = []

    def push(s, item):
        s.items.append(item)

    def pop(s):
        if not s.is_empty():
            return s.items.pop()
        return None

    def is_empty(s):
        return len(s.items) == 0



s = Stack()
x = []

s.push(5)
s.push(3)
x.append(s.pop())
s.push(2)
s.push(8)
x.append(s.pop())
x.append(s.pop())
s.push(9)
s.push(1)
x.append(s.pop())
s.push(7)
s.push(6)
x.append(s.pop())
x.append(s.pop())
s.push(4)
x.append(s.pop())
x.append(s.pop())

print("Answer for Second Question:")
print(x)





