
def encapsulate_names_in_class():
    """
    - Problem: You want to encapsulate “private” data on instances of a class,
    but are concerned about Python’s lack of access control.
    - Solution: a single leading underscore (_)
    """

    class A:
        def __init__(self):
            self._internal = 0  # An internal attribute
            self.public = 1  # A public attribute

        def public_method(self):
            print('Do in public_method()')

        def _internal_method(self):
            print('Do in _internal_method()')

    a = A()
    print(a.public)                 # 1
    print(a._internal)              # 0
    a.public_method()               # Do in public_method()
    a._internal_method()            # Do in _internal_method()

    # You may also encounter the use of two leading underscores (__)
    # on names within class definitions
    #  the private attributes in the preceding class get renamed to
    # _B__private and _B__private_method,

    class B:
        def __init__(self):
            self._name = 'hungnv132'
            self.__private = 8

        def __private_method(self):
            print('class B do in __private_method()')

        def public_method(self):
            print('class B do in public_method()')
            self.__private_method()
    b = B()
    # print(b.__private)  # AttributeError:'B' has no attr '__private'
    print(b._B__private)  # 8

    # b.__private_method()  # AttributeError:'B' has no attr '__private_method'
    b._B__private_method()  # class B do in __private_method()

    b.public_method()
    # class B do in public_method()
    # class B do in __private_method()

    class C(B):
        def __init__(self):
            super(C, self).__init__()
            self.__private = 10  # Does not override B.__private

        # Does not override B.__private_method()
        def __private_method(self):
            print('class C do in __private_method')


if __name__ == '__main__':
    encapsulate_names_in_class()