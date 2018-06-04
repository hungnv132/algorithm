
def generator_function_with_extra_state():
    """
    - Problem: You would like to define a generator function, but it involves
    extra state that you would like to expose to the user somehow.
    - Solution: Putting the generator function code int her __iter__() method.
    """
    from collections import deque

    class LineHistory(object):

        def __init__(self, lines, histlen=3):
            self.lines = lines
            self.history = deque(maxlen=histlen)

        def __iter__(self):
            for lineno, line in enumerate(self.lines, 1):
                self.history.append((lineno, line))
                yield line

        def clear(self):
            self.history.clear()

    with open('name.txt') as f:
        lines = LineHistory(f)
        for line in lines:
            if 'hungnv132' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')


if __name__ == '__main__':
    generator_function_with_extra_state()