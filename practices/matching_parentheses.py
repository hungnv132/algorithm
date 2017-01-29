from data_structures.stack import Stack


# string = {}()()(())
# THIS WAY IS WRONG!
"""
def is_match_v1(string):

    opening_list = []  # store opening
    ending_list = []  # store ending

    if len(string) == 0:
        return False

    for char in string:
        if char in ['(', '{', '[']:
            opening_list.append(char)
        elif char in [')', '}', ']']:
            ending_list.append(char)

    print(opening_list)
    print(ending_list)

    if len(opening_list) != len(ending_list):
        return False

    for index in range(len(opening_list)):
        if opening_list[index] != ending_list[index]:
            return False
    return True
"""

if __name__ == '__main__':
    print(is_match_v1("{}(()()){{{}}}[]()([])"))