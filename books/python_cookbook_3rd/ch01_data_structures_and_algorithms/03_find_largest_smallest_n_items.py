import heapq


def find_largest_smallest_n_items():
    """
    - Problem: You want to make a list of the largest or smallest N items in a
    collections
    - Solution: The `heapq` module has two functions: `nlargest()`
    and `nsmallest()`
    """
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

    print(cheap)
    """ 
    [
        {'name': 'YHOO', 'price': 16.35, 'shares': 45},
        {'name': 'FB', 'price': 21.09, 'shares': 200}
    ]
    """

    print(expensive)
    """
    [
        {'name': 'AAPL', 'shares': 50,'price': 543.22},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    """


if __name__ == "__main__":
    find_largest_smallest_n_items()