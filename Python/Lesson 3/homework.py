class Stack:

    def __init__(self, value, *args):
        self._elements = [value] + list(args)

    def push(self, value, *args):
        self._elements += [value] + list(args)

    def pop(self):
        if self._elements:
            self._elements.pop(-1)
        else:
            print("The stack is empty")

    def is_empty(self):
        return not self._elements

    def top(self):
        if self._elements:
            return self._elements[-1]
        else:
            return "The stack is empty"

    def size(self):
        return len(self._elements)


s = Stack(1, 2, 3, 4)
s.push(5, 6, 7)
s.pop()
print(s.is_empty())
print(s.top())
print(s.size())

print('-'*30)


class Queue:

    def __init__(self, value, *args):
        self._elements = [value] + list(args)

    def enqueue(self, value, *args):
        self._elements += [value] + list(args)

    def dequeue(self):
        if self._elements:
            self._elements.pop(0)
        else:
            print("The queue is empty")

    def front(self):
        if self._elements:
            return self._elements[0]
        else:
            return "The queue is empty"

    def rear(self):
        if self._elements:
            return self._elements[-1]
        else:
            return "The queue is empty"


q = Queue(1)
q.enqueue(2)
print(q._elements)
q.dequeue()
q.dequeue()
q.dequeue()
