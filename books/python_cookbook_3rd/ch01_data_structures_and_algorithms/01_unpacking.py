
def unpacking_sequence_into_separate_variables():
    """
    + Unpacking a sequence into separate variable
    - Problem: You have an N-element tuple or sequence that you would like to
     unpack into a collection of N variables.
    - Solution: Any sequence (or iterable) can be unpacked into variables using
    a simple assignment operation.
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


def unpacking_from_iterables_of_arbitrary_length():
    """
    + Unpacking elements from iterables of Arbitrary length
    - Problem: Need to unpack N elements from an iterable, but the iterable may
    be longer than N elements, causing a "too many values to unpack" exception.
    - Solution: use star expressions
    """

    def drop_first_last(elements):
        first, *middle, last = elements
        return middle, sum(middle)

    elements = [3, 5, 2, 6, 8, 5, 4, 3, 8]
    print(drop_first_last(elements))  # ([5, 2, 6, 8, 5, 4, 3], 33)

    record = ('Hung', 'hung@gmail.com', '01631234567', '01632222222')
    name, email, *phone_numbers = record
    print(name)             # Hung
    print(email)            # hung@gmail.com
    print(phone_numbers)    # ['01631234567', '01632222222']

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
        return head + sum(tail) if tail else head

    print(tong(items))  # 36


if __name__ == "__main__":
    unpacking_from_iterables_of_arbitrary_length()