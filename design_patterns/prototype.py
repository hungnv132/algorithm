import copy


class Prototype(object):

    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError("Incorrect object identifier: {}".format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


class Book(object):

    def __init__(self, title, author, price, **other):
        self.title = title
        self.author = author
        self.price = price
        self.__dict__.update(other)

    def __str__(self):
        return "{} - {} - {}".format(self.title, self.author, self.price)


if __name__ == '__main__':
    b1 = Book('The C Programming Language',
              ('Brian W. Kernighan', 'Dennis M.Ritchie'),
              price=118,
              publisher='Prentice Hall', length=228,
              publication_date='1978-02-22',
              tags=('C', 'programming', 'algorithms', 'data structures'))

    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language (ANSI)',
                         price=48.99, length=274, publication_date='1988-04-01',
                         edition=2)
    print(id(b1))
    print(id(b2))
