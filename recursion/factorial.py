from common import time_log as log

def factorial_first(n):
    n = int(n)
    if n == 0:
        return 1
    else:
        return n * factorial_first(n-1)

if __name__ == '__main__':
    print(factorial_first(4))