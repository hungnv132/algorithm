
class _Node(object):

    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class LinkedStack(object):

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, value):
        new_node = _Node(value,self._head)
        self._head = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Exception(' The LinkedStack is empty.')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def top(self):
        if self.is_empty():
            raise Exception(' The LinkedStack is empty.')
        return self._head._element

    def __str__(self):
        node = self._head
        value_list = []
        while node is not None:
            value_list.append(node._element)
            node = node._next
        return str(value_list)


if __name__ == '__main__':
    stack = LinkedStack()
    print('Length: %s' % (len(stack)))
    print('push 3 times')
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print('Length: %s' % (len(stack)))
    print("First pop: %s" % (stack.pop()))
    print("Top: %s" % (stack.top()))
    print("Second pop: %s" % (stack.pop()))
    print('Length: %s' % (len(stack)))