import ctypes


class DynamicArray:

    def __init__(self):
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        return self._n

    def __getitem__(self, index):
        if not 0 <= index < self._n:
            raise IndexError('Invalid index')
        return self._A[index]

    def append(self, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = value
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for j in range(self._n):
            B[j] = self._A[j]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """ Return a new array with capacity c"""
        return (c * ctypes.py_object)()

if __name__ == '__main__':
    arr = DynamicArray()
    arr.append(12)
    arr.append('hungnv132')
    print(len(arr))  # print: 2
    print(arr[1])    # print: hungnv132
