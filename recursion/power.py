"""
 + Describe: x^n =?
 + References: Data structures and Algorithms in Python by Goodrich, Michael T., Tamassia, Roberto, Goldwasser, Michael
"""

def power_v1(x, n):
    if n == 0:
        return 1
    else:
        return x * power_v1(x, n-1)


def power_v2(x, n):
    if n == 0:
        return 1
    else:
        partial = power_v2(x, n//2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result
if __name__ == '__main__':
    print(power_v1(2, 3))
    print(power_v2(4, 5))