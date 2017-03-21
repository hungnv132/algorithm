from _collections_abc import MutableMapping
from random import randrange


class MapBase(MutableMapping):
    """ Our own abstract base class that includes a nonpublic _Item class"""

    # ---------------------- nested _Item class------------------------
    class _Item:
        """Lightweight composite to store key-value pairs as mapitems"""
        __slot__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key      # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)          # opposite of __eq__

        def __lt__(self, other):
            return self._key < other._key       # compare items based on their keys


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list"""

    def __init__(self):
        """create an empty map."""
        self._table = []

    def __getitem__(self, k):
        """ Return value associated with key k,
            raise KeyError if not found
        """
        for item in self._table:
            if item._key == k:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present"""
        for item in self._table:
            if item._key == k:          # Found a match
                item._value = v
                return
        self._table.append(self._Item(k, v))  # did not find match for key, create a new _Item object, then appending

    def __delitem__(self, k):
        """ Remove item associated with key k, raise KeyError if not found"""
        for i in range(len(self._table)):
            if self._table[i]._key == k:
                self._table.pop(i)
                return

        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        """Generate iteration of map's keys"""
        for item in self._table:
            yield item._key


class HashMapBase(MapBase):
    """"Abstract base class for map using hash-table with MAD compression"""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map"""
        self._table = cap * [None]
        self._n = 0                         # number of entries in the map
        self._prime = p                     # prime for MAD compression
        self.scale = 1 + randrange(p-1)     # scale from 1 to p-1 for  MAD
        self._shift = randrange(p)          # scale from 0 to p-1 for MAD

    def _hash_function(self, k):
        repr( hash(k)*self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, key):
        i = self._hash_function(key)
        return self._bucket_getitem(i, key)         # may raise KeyError

    def __setitem__(self, key, value):
        i = self._hash_function(key)
        self._bucket_setitem(i, key, value)         # subroutine matintains self._n
        if self._n > len(self._table) // 2:         # keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)  # number 2^x -1 is often prime

    def __delitem__(self, key):
        i = self._hash_function(key)
        self._bucket_delitem(i, key)
        self._n -= 1

    def _resize(self, c):                   # resize bucket arry to capicity c
        old = list(self.items())            # use iteration to record existing items
        self._table = c * [None]            # then reset table to desired capacity
        self._n = 0
        for (k, v) in old:
            self[k] =v