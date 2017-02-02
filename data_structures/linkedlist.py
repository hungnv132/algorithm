
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

    def push(self, element):
        new_node = _Node(element, self._head)
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
        element_list = []
        while node is not None:
            element_list.append(node._element)
            node = node._next
        return str(element_list)


class LinkedQueue(object):

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, element):
        """Add an element to the back of queue Q"""

        new_node = _Node(element, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Remove and return the first element from the queue"""
        """
        if self.is_empty():
            raise Exception('The queue is empty')
        elif self._size == 1:
            self._head = self._tail = None
        else:
            self._head = self._head._next
        answer = self._head._element
        self._size -= 1
        return answer
        """
        if self.is_empty():
            raise Exception('The queue is empty')
        answer =  self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def first(self):
        """Return the element at the front of the queue, but do not remove"""
        if self.is_empty():
            raise Exception('The queue is empty')
        return self._head._element




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