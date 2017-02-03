class _Node(object):

    __slots__ = '_element', '_prev', '_next'

    def __init__(self, element, prev, _next):
        self._element = element  # user's element
        self._prev = prev        # previous node reference
        self._next = _next       # next node reference


class DoublyLinkedBase(object):
    """ A base class providing a doubly linked list representation."""
    def __init__(self):
        self._header =  _Node(None, None, None)
        self._trailer = _Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev =  self._header
        self._size =  0

    def __len__(self):
        """Return the number of elements in the list"""
        return self._size

    def is_empty(self):
        """Return True if list is empty"""
        return self._size == 0

    def _insert_between(self, element, predecessor, successor):
        new_node = _Node(element, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predcessor = node._prev
        successor = node._next
        predcessor._next = successor
        successor._prev = predcessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

class LinkedDeque(DoublyLinkedBase):

    def first(self):
        if self.is_empty():
            raise Exception('The Deque is empty')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Exception('The Deque is empty')
        return self._trailer._prev._element

    def insert_first(self, element):
        """Add an element to the front of the deque"""
        self._insert_between(element, self._header, self._header._next)

    def insert_last(self, element):
        """Add an element to the back of the deque"""
        self._insert_between(element, self._trailer._prev, self._trailer)

    def delete_first(self):
        """remove and return the element from the front of the deque"""
        if self.is_empty():
            raise Exception('The Deque is empty')
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque"""
        if self.is_empty():
            raise Exception('The Deque is empty')
        return self._delete_node(self._trailer._prev)