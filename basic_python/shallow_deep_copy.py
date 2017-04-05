import copy

# shallow copy
"""A shallow copy contructs a new compound object and then inserts references into it to the objects found in the
original
"""
list1 = [1, 2, 3, 4]
list2 = list1
list3 = copy.copy(list1)

print(list1)        # [1, 2, 3, 4]
print(list1)        # [1, 2, 3, 4]
print(list3)        # [1, 2, 3, 4]

list1[0] = 'abc'
list2[1] = 'xyz'
list3[2] = 'dcm'

print(list1)        # ['abc', 'xyz', 3, 4]
print(list2)        # ['abc', 'xyz', 3, 4]
print(list3)        # [1, 2, 'dcm', 4]
# =============

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
shallow_c = copy.copy(c)

a[0] = 'new a'
b[1] = 'new b'

print(c)                # [['new a', 2, 3], [4, 'new b', 6]]
print(shallow_c)          # [[1, 2, 3], [4, 5, 6]]

#============
# deep copy
"""A deep copy constructs a new compound object and then, recusively, insert copies into it of the objects found in the
original
"""
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
deep_c = copy.deepcopy(c)

a[0] = 'new a'
b[1] = 'new b'

print(c)                # [['new a', 2, 3], [4, 'new b', 6]]
print(deep_c)          # [['new a', 2, 3], [4, 'new b', 6]]
