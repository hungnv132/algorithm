
def mapping_keys_to_multiple_values():
    """
    - Problem: You want to make a dictionary that maps keys to more than
    one value (a so-called "multidict")
    - Solution: A dictionary is a mapping where each key is mapping to a single
    value. If you want to map keys to multiple values, you need to store the
    multiple values in another container such as a list or set.
    """

    # values is a list
    d = {
        'a': [1, 2, 3],
        'b': [4, 5],
    }

    # values is a set
    e = {
        'a': {1, 2, 3},
        'b': {4, 5},
    }

    from collections import defaultdict

    # Create a dict values is list type
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(3)
    d['b'].append(4)

    print(d)  # defaultdict(<class 'list'>, {'b': [3, 4], 'a': [1, 2]})

    # Create a dict values is set type
    d = defaultdict(set)
    d['a'].add(5)
    d['a'].add(6)
    d['b'].add(7)
    d['b'].add(8)

    print(d)  # defaultdict(<class 'set'>, {'b': {8, 7}, 'a': {5, 6}})

    # next example
    d = {}
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(3)
    d.setdefault('b', []).append(4)

    # to values in a list, we must initialize an empty list
    def add_to_dict(pairs):
        _d = {}
        for key, value in pairs:
            if key not in _d:
                _d[key] = []
            _d[key].append(value)

    # Using a defaultdict simply leads to much cleaner code,
    def add_to_dict_2(pairs):
        _d = defaultdict(list)
        for key, value in pairs:
            _d[key].append(value)


def keeping_dictionary_in_order():
    """
    - Problem: You want to create a dictionary, and you also want to control
    the order of items when iterating or serializing.
    - Solution: Use OrderedDict from the collections module.
    - OrderedDict can be useful when want to build a mapping to serialize
    or encode into a different format.
    - An OrderedDict is a dictionary subclass that remembers the order in which
    its contents are added.
    - Be aware that the size of an OrderedDict is more than twice as large as
    a normal dictionary due to the extra linked list that’s created.
    """
    from collections import OrderedDict

    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    print(d)  # OrderedDict([('foo', 1), ('bar', 2), ('spam', 3)])


def calculating_with_dictionaries():
    """
    - Problem: YOu want to perform various calculations (min value, max value,
    sorting, ...) on a dictionary of data.
    - Solution: zip()
    """
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    # zip(): Returns an iterator of tuples, where the i-th tuple contains
    # the i-th element from each of the argument sequences or iterables.
    # zip() creates an iterator that can only be consumed once.

    # zip() invert the dictionary into a sequence of (value, key) pairs.
    # When performing comparisons on such tuple, the value element is compared
    # first, followed by the key

    min_price = min(zip(prices.values(), prices.keys()))
    print(min_price)  # (10.75, 'FB')

    max_price = max(zip(prices.values(), prices.keys()))
    print(max_price)  # (612.78, 'AAPL')

    # to rank the data
    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print(prices_sorted)
    # [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'),
    #  (205.55, 'IBM'), (612.78, 'AAPL')]

    # zip() creates an iterator that can only be consumed once.
    prices_and_names = zip(prices.values(), prices.keys())
    print(min(prices_and_names))   # OK
    # print(max(prices_and_names))   # ValueError: max() arg is an empty sequence

    # The normal way we do.

    print(min(prices))  # AAPL
    print(max(prices))  # IBM

    print(min(prices.values()))  # 10.75
    print(max(prices.values()))  # 612.78

    # You can get the key corressponding to the min or max value
    print(min(prices, key=lambda k: prices[k]))  # FB
    print(max(prices, key=lambda k: prices[k]))  # AAPL

    # However, to get the minimum value,...
    min_value = prices[min(prices, key=lambda k: prices[k])]
    print(min_value)  # 10.75


def finding_commonalities_in_two_dictionaries():
    """
    - Problem: You have two dictionaries and want to find out what they might
    have in common (same keys, same values,...
    - Solution: perform common set operations using the keys() or items() methods
    """
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    # Find keys in common
    c = a.keys() & b.keys()
    print(c)  # {'x', 'y'}

    # Find keys in a that are not in b
    d = a.keys() - b.keys()
    print(d)   # {'z'}

    # Find (key, value) pairs in common
    e = a.items() & b.items()
    print(e)  # {('y', 2)}

    # These kinds of operations can be used to alter or filter dict content
    # Eg: Make a new dict with certain keys removed
    f = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(f)  # {'y': 2, 'x': 1}


if __name__ == "__main__":
    finding_commonalities_in_two_dictionaries()