import factory


class Student(object):

    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def __str__(self):
        return "%s - %s - %s" % (self.name, self.email, self.address)


class StudentFactory(factory.Factory):

    class Meta:
        model = Student

    class Params:
        duration = 50

    name = factory.LazyAttribute(lambda o: o.duration)
    email = factory.LazyAttribute(lambda a: '{0}.hn@example.com'.format(a.name).lower())
    address = factory.Faker('prefix_male')


if __name__ == '__main__':
    f = StudentFactory.build()
    print(f)
    print(type(f))