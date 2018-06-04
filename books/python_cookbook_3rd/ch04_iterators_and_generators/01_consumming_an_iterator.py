
def manually_consuming_an_iterator():
    """
    - Problem: You need to process items in an iterable, but for whatever reason,
    you can't or don't want to use a for loop.
    - Solution: use the `next()` function, and catch the StopIteration exception.
    """
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

    items = [1, 2, 3]
    # print(next(items))    # TypeError: 'list' object is not an iterator
    it = iter(items)
    print(next(it))  # 1
    print(next(it))  # 2
    print(next(it))  # 3
    # print(next(it))  # Exception :StopIteration


def delegating_iteration():
    """
    - Problem: You have build a custom container object that internally holds a
    list, tuple, some other iterable. You would like to make iteration work
    with new container
    - Solution: Define an __iter__() method.
    """
    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return 'Node({!r})'.format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

    root = Node(0)
    child_1 = Node(1)
    child_2 = Node(2)
    root.add_child(child_1)
    root.add_child(child_2)

    for child in root:
        print(child)  # Node(1) Node(2)


def create_iteration_pattern_with_generators():
    """
    - Problem: You want to implement a customer iteration pattern that's different
    than the usual built-in funstion (range(), reversed(),...)
    - Solution: Use the `yield` statement
    - The `yield` statement in a function turns it into a generator. Unlike a
    normal function, a generator only runs in response to iteration.
    """
    def frange(start, stop, increment):
        x = start
        while x < stop:
            yield x
            x += increment

    for n in frange(0, 5, 1):
        print(n)  # 0  1  2  3  4  5

    # next example
    def countdown(n):
        print("Starting to count from", n)
        while n > 0:
            yield n
            n -= 1
        print('Done!')

    c = countdown(3)
    print(c)  # <generator object create_iteration_pattern_wi....

    print(next(c))
    # Starting to count from 3
    # 3
    print(next(c))
    # 2
    print(next(c))
    # 1
    print(next(c))
    # Done!

    print(next(c))  # Exception: StopIteration


def implement_iterator_protocol():
    """
    - Problem: You are building custom objects on which you would like to support
    iteration, but would like an easy way to implement the iterator protocol
    - Solution: Use generator function: `yield` and `yield from`
    """

    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return 'Node({!r})'.format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

        def depth_first(self):
            yield self
            for c in self:
                yield from c.depth_first()

    root = Node(0)
    child_1 = Node(1)
    child_2 = Node(2)
    root.add_child(child_1)
    root.add_child(child_1)
    child_1.add_child(Node(3))
    child_1.add_child(Node(4))
    child_2.add_child(Node(5))

    for child in root.depth_first():
        print(child)  # Node(0) Node(1) Node(3) Node(4)  Node(1) Node(3)Node(4)

    # Normal way
    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return 'Node({!r})'.format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

        def depth_first(self):
            return DepthFirstIterator(self)

    class DepthFirstIterator(object):

        def __init__(self, start_node):
            self._node = start_node
            self._children_iter = None
            self._child_iter = None

        def __iter__(self):
            return self

        def __next__(self):
            # Return myself if just started; create an iterator for children
            if self._children_iter is None:
                self._children_iter = iter(self._node)
                return self._node

            # if processing a child, return its next item.
            elif self._child_iter:
                try:
                    nextchild = next(self._child_iter)
                    return nextchild
                except StopIteration:
                    self._child_iter = None
                    return next(self)

            # Advance to the next child and start its iteration
            else:
                self._child_iter = next(self._children_iter).depth_first()
                return next(self)

    root = Node(0)
    child_1 = Node(1)
    child_2 = Node(2)
    root.add_child(child_1)
    root.add_child(child_1)
    child_1.add_child(Node(3))
    child_1.add_child(Node(4))
    child_2.add_child(Node(5))

    for child in root.depth_first():
        print(child)  # Node(0) Node(1) Node(3) Node(4)  Node(1) Node(3)Node(4)


if __name__ == '__main__':
    # manually_consuming_an_iterator()
    # delegating_iteration()
    # create_iteration_pattern_with_generators()
    implement_iterator_protocol()