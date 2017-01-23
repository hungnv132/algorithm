
# performance: O(2^n)
def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)


# performance: O(n)
def good_fibonacci(n):
    """ Return pair of Fibonacci numbers, F(n) and F(n-1), using the convention F(-1)=0"""
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a + b, a)

if __name__ == '__main__':
    print(bad_fibonacci(6))