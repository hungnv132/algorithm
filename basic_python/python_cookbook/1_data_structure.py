from collections import deque
import heapq


def unpacking_1_():
    """
    Unpacking a sequence into separate variable
     - Working with any iterable object: tuple, list, string, files, iterators, generators
    """
    p = (4, 5)
    x, y = p
    print(x, y)  # 4 5

    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print(name)  # ACME
    print(date)  # (2012, 12, 21)

    name, shares, price, (year, mon, day) = data
    print(name)  # ACME
    print(year)  # 2012
    print(mon)  # 12
    print(day)  # 21

    # iterable string
    s = "hello"
    a, b, c, d, e = s
    print(a, b, c, d, e)  # h e l l o

    # discard certain values:
    _, shares, price, _ = data
    print(shares)  # 50
    print(price)  # 91.1


def unpacking_2_():
    """
    Unpacking elements from iterables of Arbitrary length
     - star expressions
    """
    def drop_first_last(elements):
        first, *middle, last = elements
        return middle, sum(middle)

    elements = [3, 5, 2, 6, 8, 5, 4, 3, 8]
    print(drop_first_last(elements))  # ([5, 2, 6, 8, 5, 4, 3], 33)

    *trailing, current = [3, 5, 2, 6, 8, 5, 4, 3, 8]
    print(trailing)  # [3, 5, 2, 6, 8, 5, 4, 3]
    print(current)  # 8

    # example 2
    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4)
    ]

    def do_foo(x, y):
        print('foo', x, y)

    def do_bar(s):
        print('bar', s)

    for tag, *args, in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)

    # example 3
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *field, homedir, sh = line.split(':')
    print(uname)  # nobody
    print(homedir)  # /var/empty
    print(sh)  # /usr/bin/false

    # example 4
    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record
    print(name)  # ACME
    print(year)  # 2012

    # example 5
    items = [1, 10, 7, 4, 5, 9]
    head, *tail = items
    # print(type(*tail))  # error
    print(type(tail))  # <class 'list'>

    def tong(items):
        head, *tail = items
        return head + _sum(tail) if tail else head

    print(tong(items))  # 36


def keep_last_n_items():
    """
    Keeping the last N items
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


def find_largest_smallest_n_items():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))   # [42, 37, 23]
    print(heapq.nsmallest(3, nums))  # [-4, 1, 2]

    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]

    cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
    print(cheap)   # [{'name': 'YHOO', 'price': 16.35, 'shares': 45}, {'name': 'FB', 'price': 21.09, 'shares': 200}]
    print(expensive)  # [{'name': 'AAPL', 'shares': 50,'price': 543.22},{'name': 'ACME', 'shares': 75, 'price': 115.65}]


if __name__ == "__main__":
    find_largest_smallest_n_items()