
from time import time

def print_time(method, *args):
    start_time = time()
    print('[= START_TIME: %s ]' % time())

    print(method(*args))

    end_time = time()
    print('[= START_TIME: %s ]' % end_time)
    print('[= ELASPSED_TIME: %s ]' % (end_time - start_time))

if __name__ == '__main__':
    print_time()