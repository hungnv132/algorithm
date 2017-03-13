


def generator(N):
    for x in range(N):
        yield x*2

if __name__ == '__main__':
    for x in generator(5):
        print(x)

    a = generator(4)
    print(next(a))

    print(bin(88))
    print(bool({}))