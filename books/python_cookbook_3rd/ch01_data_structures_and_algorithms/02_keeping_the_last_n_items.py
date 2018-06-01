from collections import deque


def keep_last_n_items():
    """
    - Problem: You want to keep a limited history of the last few items seen
    during iteration or during some other kind of processing.
    - Solution: Use collections.deque
    """
    def search(lines, pattern, history=5):
        previous_lines = deque(maxlen=history)
        for line in lines:
            if pattern in line:
                yield line, previous_lines
            previous_lines.append(line)

    with open('test.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)


if __name__ == "__main__":
    keep_last_n_items()