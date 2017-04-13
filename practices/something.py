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

    city_list = [
        {'name': 'HN', 'population': 80000},
        {'name': 'HCM', 'population': 40000},
        {'name': 'DN', 'population': 20000},
        {'name': 'HP', 'population': 10000},
    ]

    # using sum() method
    print(sum(city['population'] for city in city_list))  # 150000

    # using reduce() method, only python 2.7
    def tinh_tong(x, y):
        return x + y

    population_list = (city['population'] for city in city_list)
    print(reduce(tinh_tong, population_list))

    # hoac su dung lambda
    print(reduce(lambda x, y: x+y, (city['population'] for city in city_list)))

    # remove duplicate items in a list
    num_list = [1, 2, 4, 6, 4, 2, 8, 8, 3, 2]
    new_list = []
    for item in num_list:
        if item not in new_list:
            new_list.append(item)

    print(num_list)             # [1, 2, 4, 6, 4, 2, 8, 8, 3, 2]
    print(new_list)             # [1, 2, 4, 6, 8, 3]

    # or use set() method, cast back to list
    print(list(set(num_list)))  # [1, 2, 4, 6, 8, 3]
