

class Queue(object):

    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, value):
        """Add an element to back of the queue"""
        self._data.append(value)

    def dequeue(self):
        """
        Remove and return the first element of the queue;
        Raise an error if the queue is emtpy.
        """
        if self.is_empty():
            raise Exception('The queue is empty')
        return self._data.pop(0)
        # Performace: O(n), where n is length of '_data'

    def first(self):
        return self._data[0]

    def __len__(self):
        return len(self._data)


class ArrayQueue(object):

    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('The queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """
        Remove and return the first element of the queue
        Raise an exception if the queue is empty
        """
        if self.is_empty():
            raise Exception('The queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, value):
        """Add an element to the back of queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = value
        self._size += 1

    def _resize(self, capacity):
        old = self._data
        self._data = [None] * capacity
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


if __name__ == '__main__':
    q = ArrayQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.first())
    print(len(q))
    print(q.dequeue())
    print(q.first())
    print(len(q))
    print(q.dequeue())
    print(q.first())
