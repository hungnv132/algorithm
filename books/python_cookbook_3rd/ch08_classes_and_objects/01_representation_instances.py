
def change_string_representation_of_instances():
    """
    - Problem: You want to change the output produced by printing or viewing
    instances to something more sensible.
    - Solution: Define the __str__() ad __repr__()
    - __repr___() and __str__() is simplify debugging and instance output.
    - The outout of __repr__() to produce text such that eval(repr(x)) == x
    """

    class Pair:

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return '({0.x!s}, {0.y!s})'.format(self)

        def __repr__(self):
            return 'Pair({0.x!r}, {0.y!r})'.format(self)

    p = Pair(6, 8)

    # !r formatting code indicates the output of __repr__() should be used
    # instead of  __str__()
    print('p is {0!r}'.format(p))  # p is Pair(6, 8)
    print(p)  # (6, 8)


def customize_string_formatting():
    """
    - Problem: You want an object to support customized formatting through the
    format() fucntion and string method
    - Solution: Defien the __format__() method on a class.
    """
    _formats = {
        'ymd': '{d.year}-{d.month}-{d.day}',
        'mdy': '{d.month}/{d.day}/{d.year}',
        'dmy': '{d.day}/{d.month}/{d.year}'
    }

    class Date:

        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

        def __format__(self, code):
            if code == '':
                code = 'ymd'
            fmt = _formats[code]
            return fmt.format(d=self)

    d = Date(2012, 12, 21)
    print(d)
    print(format(d))  # 2012-12-21
    print(format(d, 'mdy'))  # 12/21/2012

    s = 'The date is {:ymd}'.format(d)
    print(s)  # The date is 2012-12-21

    s = 'The date is {:mdy}'.format(d)
    print(s)  # The date is 12/21/2012

    from datetime import date
    d = date(2018, 8, 21)
    print(format(d))  # 2018-08-21
    print(format(d, '%A, %B %d, %Y'))  # Tuesday, August 21, 2018

    s = 'The end is {:%d %b %Y}. Goodbye'.format(d)
    print(s)  # The end is 21 Aug 2018. Goodbye


if __name__ == '__main__':
    customize_string_formatting()
