

def generator(N):
    for x in range(N):
        yield x*2


def runt():
    for x in generator(5):
        print(x)

    a = generator(4)
    print(next(a))

    print(bin(88))
    print(bool({}))


# Example generator:
def firstn(n):
    """
    This code is quite simple and straightforward, but its builds the full list in memory.
    """
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


# Using the generator pattern (an iterable)
class FirstN(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def __next__(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
            return cur
        else:
            raise StopIteration()


# a generator that yield items instead of returning a list.
def first_n_v2(n):
    num = 0
    while num < n:
        yield num
        num += 1


def simple_generator():
    yield "hello"
    yield 'how are you?'
    yield 'Nice to meet you'

if __name__ == '__main__':
    # sum_of_first_n = sum(firstn(1000000))
    # sum_of_first_n = sum(FirstN(1000000))
    # sum_of_first_n = sum(first_n_v2(1000000))
    # print(sum_of_first_n)

    print(type(simple_generator))  # <class 'function'>
    print(type(simple_generator()))  # <class 'generator'>
    print(simple_generator())  # <generator object simple_generator at 0x7f1268d1dc50>
    print(next(simple_generator()))  # hello
    print(next(simple_generator()))  # hello
    print(next(simple_generator()))  # hello
    
    for say in simple_generator():
        print(say)  # hello how are you? Nice to meet you

    print(hasattr(simple_generator(), '__iter__'))