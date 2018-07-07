
"""
 + Last-in, First-out (LIFO)
"""


class Stack(object):

    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)


if __name__ == '__main__':
    stack = Stack()
    stack.push(4)
    stack.push(2)
    stack.push(3)
    stack.push(1)
    print(len(stack))
    print(stack.top())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(len(stack))
    print(stack.is_empty())
