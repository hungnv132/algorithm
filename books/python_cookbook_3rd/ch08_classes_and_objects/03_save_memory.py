def save_memory_when_create_large_number_of_instances():
    """
    - Problem: Your program creates a large number (e.g, millions) of instances
     and uses a large amount of memory.
    - Solution: adding the __slots__ attribute to the class definition
    """

    class Date(object):
        __slots__ = ['year', 'month', 'day']

        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

    class DateWithoutSlot:

        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

    d = Date(2018, 8, 2)
    # print(d.__dict__)
    #  AttributeError: 'Date' object has no attribute '__dict__'
    # print(d.__weakref__)
    # AttributeError: 'Date' object has no attribute '__weakref__'

    print(dir(d))
    # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__'
    #  '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__'
    #  '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
    # '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__',
    # '__str__', '__subclasshook__', 'day', 'month', 'year']

    d = DateWithoutSlot(2018, 8, 2)
    print(d.__dict__)  # {'year': 2018, 'month': 8, 'day': 2}
    print(d.__weakref__)  # None
    print(dir(d))
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
    # '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
    # '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
    #  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
    #  '__str__', '__subclasshook__', '__weakref__', 'day', 'month', 'year']


if __name__ == '__main__':
    save_memory_when_create_large_number_of_instances()
