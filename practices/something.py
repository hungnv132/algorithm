from data_structures.stack import Stack
from _collections import deque


# Give a recursion method for removing all the elements from a stack
def remove_all_stack(stack):
    if not stack.is_empty():
        stack.pop()
        remove_all_stack(stack)

if __name__ == '__main__':

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(len(stack))
    remove_all_stack(stack)
    print(len(stack))
