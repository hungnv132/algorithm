from data_structures.stack import Stack


# string = {}()()(())
# THIS WAY IS WRONG!
"""
def is_match_v1(string):

    opening_list = []  # store opening
    closing_list = []  # store closing

    if len(string) == 0:
        return False

    for char in string:
        if char in ['(', '{', '[']:
            opening_list.append(char)
        elif char in [')', '}', ']']:
            closing_list.append(char)

    print(opening_list)
    print(closing_list)

    if len(opening_list) != len(closing_list):
        return False

    for index in range(len(opening_list)):
        if opening_list[index] != closing_list[index]:
            return False
    return True
"""


# THIS WAY IS RIGHT!
def is_match_v2(string):
    
    opening = '({['
    closing  = ')}]'
    if len(string) == 0:
        return False

    opening_stack = Stack()
    for char in string:
        if char in opening:
            opening_stack.push(char)
        elif char in closing:
            if opening_stack.is_empty() or (not closing.index(char) == opening.index(opening_stack.pop())):
                return False
    return opening_stack.is_empty()

if __name__ == '__main__':
    print(is_match_v2("{}(()()){{{}}}[]()(][)"))