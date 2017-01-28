
class Person(object):
    a = 10
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    print(Person.a)
    Person.a = 20
    print(Person.a)