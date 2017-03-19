


def generator(N):
    for x in range(N):
        yield x*2

def test():
    for x in generator(5):
        print(x)

    a = generator(4)
    print(next(a))

    print(bin(88))
    print(bool({}))

if __name__ == '__main__':

    generator = (x * x for x in range(3))
    print(type(generator))
    print('length: %s' % len(generator))
    for i in generator:
        print('3')
    print('length: %s' % len(generator))
    for i in generator:
        print(i)