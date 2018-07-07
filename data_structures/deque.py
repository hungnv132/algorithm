"""
    Double End Queue (DEQue)
"""


class Deque(object):

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Deque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return self._size

    def add_first(self, value):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = value
        self._size += 1

    def add_last(self, value):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = value
        self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise Exception('The queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Exception('The queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        return answer

    def first(self):
        if self.is_empty():
            raise Exception('The queue is empty')
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Exception('The queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def _resize(self, capacity):
        old = self._data
        self._data = [None] * capacity
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


if __name__ == '__main__':
    deq = Deque()
    deq.add_first(1)
    deq.add_first(2)
    deq.add_first(3)
    print("length: %s" % len(deq))
    deq.add_last(4)
    deq.add_last(5)
    deq.add_last(6)
    print("length: %s" % len(deq))
    print(deq.first())
    print(deq.last())
    print(deq.delete_first())
    print("length: %s" % len(deq))
    print(deq.delete_last())
    print("length: %s" % len(deq))
