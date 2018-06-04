
def iterating_in_reverse():
    """
    - Problem: You want to iterate in reverse over a sequence.
    - SolutionL Use the built-in reversed() function.
    - Reversed iteration can be customized on user-defined classes if they
    implement the __reversed__() method.
    """
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)  # 4 3 2 1

    class CountDown:

        def __init__(self, start):
            self.start = start

        # Forward iterator
        def __iter__(self):
            n = self.start
            while n > 0:
                yield n
                n -= 1

        # Reverse iterator
        def __reversed__(self):
            n = 1
            while n <= self.start:
                yield n
                n += 1



if __name__ == '__main__':
    iterating_in_reverse()