
def anonymous_inline_functions():
    """
    - Problem: You need to supply a short callback function for use with an
    operation such as sort(), but you don't want to write a separate one-line
    function using the def statement.
    - Solution: use a `lambda` expression.
    """
    add = lambda x, y: x + y
    print(add(2, 3))  # 5

    names = ['David Beazley', 'Brian Jones',
             'Raymond Hettinger', 'Ned Batchelder']

    sorted_names = sorted(names, key=lambda name: name.split()[-1].lower())
    print(sorted_names)
    # ['Ned Batchelder', 'David Beazley', 'Raymond Hettinger', 'Brian Jones']


if __name__ == '__main__':
    anonymous_inline_functions()