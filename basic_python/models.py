
def _set_name(self, name):
    self.name = name

class A:

    __c =32
    def m(self):
        print('aaaaa')
    def m(self):
        print('ccccc')
class B:
    def m(self):
        print('bbbbbbb')

class Person(A, B):
    __c = 32
    human = True
    numner = 24
    _numner = 241
    set_name = _set_name

    def __init__(self, name='hungnv132', age=24):
        self.name = name
        self.age = age

    def __str__(self):
        return "{name!s} - age {age!s}".format(**self.__dict__)

    def get_name(self):
        return self.name

    def get_name(self):
        return