

class _DoublyLinkedBase(object):

    class _Node(object):
        """Nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, _next):
            self._element = element  # user's element
            self._prev = prev  # previous node reference
            self._next = _next  # next node reference

    """ A base class providing a doubly linked list representation."""
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list"""
        return self._size

    def is_empty(self):
        """Return True if list is empty"""
        return self._size == 0

    def _insert_between(self, element, predecessor, successor):
        new_node = self._Node(element, predecessor, successor)
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


class LinkedDeque(_DoublyLinkedBase):

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


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positonal access"""

# ------------------------------- START  Position class -------------------------------
    class Position:
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position"""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)

# ------------------------------- END  Position class -------------------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise TypeError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        """Return the first Position in the list(or None if list is empty)"""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list(or None if list is empty)"""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Postion p (or None if p is first)"""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Postion just after Position p(or None if p is last)"""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward interation of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # override inherited version to return Position, rather than Node
    def _insert_between(self, element, predecessor, successor):
        """Add an element between existing nodes and return new Position"""
        node =  super()._insert_between(element, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Positon"""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Postion"""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position"""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position"""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p"""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """Replace the element at Position p with e. Return the element formerly at Position p"""
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
