from data_structures.stack import Stack
from _collections import deque


# Give a recursion method for removing all the elements from a stack
def remove_all_stack(stack):
    if not stack.is_empty():
        stack.pop()
        remove_all_stack(stack)


def test_remove_all_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(len(stack))
    remove_all_stack(stack)
    print(len(stack))


def hash_code(s):
    mask = (1 << 32) - 1  # limit to 32-bit integers
    h = 0
    for character in s:
        h = (h << 5 & mask) | (h >> 27)  # 5-bit cyclic shift of running sum
    h += ord(character)  # add in value of next character
    return h

if __name__ == '__main__':

    print(ord('A'))
    print(list(map(ord, 'spam')))
    print(hash_code("hungnv132"))

    global name
    name ="huVgn"
    print(set(name))
    print(chr(97))
    print(ord('â'))
    print(hex(10))
    print(oct(20))
    print(globals())
    print(min(name))
    print(name.swapcase())

    l = [1, 2, 3, 4]
    l.insert(1, 5)
    print(l)
    print(str(3) is str('3'))
    import time
    import calendar

    cal = calendar.month(2008, 1)
    print(cal)