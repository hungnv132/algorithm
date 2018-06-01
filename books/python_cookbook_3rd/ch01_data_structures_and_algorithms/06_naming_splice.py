
def naming_a_slice():
    """
    - Problem: your program has become an unreadable mess of hardcoded slice
    indices and you want to clean it up.
    - Solution: Built-in slice() creates a slice object that can be used anywhere
    a slice is allowed.
    """
    # -----   0123456789012345678901234567890123456789012345678901234567890'
    record = '....................100       .......512.88     ..........'

    # Norma way
    cost = int(record[20:23]) * float(record[37:44])
    print(cost)

    SHARES = slice(20, 23)
    PRICE = slice(37, 44)

    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)

    # some examples about slice()
    items = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)

    print(items[2:4])   # [2, 3]
    print(items[a])     # [2, 3]

    items[a] = [10, 11]
    print(items)  # [0, 1, 10, 11, 4, 5, 6]

    del items[a]
    print(items)  # [0, 1, 4, 5, 6]

    b = slice(5, 50, 2)
    print(b.start)  # 5
    print(b.stop)   # 50
    print(b.step)   # 2


if __name__ == '__main__':
    naming_a_slice()