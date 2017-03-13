
name = 'hungnv132'  # This is a global variable.


def test_scope1():
    name = 'abcdef'             # A local variable.
    print('1. %s' % name)       # Print: 'abcdef'

    def test_nonlocal():
        nonlocal name
        name = 'xyz888'
        print('2. %s' % name)   # Print: 'xyz888'

    print('3. %s' % name)  # Print: 'new world'
    test_nonlocal()
    print('4. %s' % name)  # Print: 'new world'


def test_scope2():
    global name
    name = 'new world'
    print('1. %s' %name)         # Print: 'new world'




def function_call(a, b):
    print(a)
    print(b)


def test_function_call():
    list = (45, 90)
    list1 = (45, 90, 88)
    dic = {'a': 12, 'b': 56}
    dic1 = {'a': 12,}
    dic2 = {'c': 68, 'd': 88}
    # function_call(2, 3)        # OK
    # function_call(2)           # ERROR: takes 2 positional arguments but 1 were given
    # function_call(2, 3, 4)     # ERROR: takes 2 positional arguments but 3 were given
    # function_call(*list)       # OK
    # function_call(*list1)      # ERROR: takes 2 positional arguments but 3 were given
    # function_call(a=2, b=5)    # OK
    # function_call(**dic)       # OK
    # function_call(**dic1)      # ERROR: missing 1 required positional argument: 'b'
    # function_call(**dic2)      # ERROR: got an unexpected keyword argument 'c'


def function_header_tuple(*args):
    print('Type of Name: %s' % type(args))  # Tuple
    print(args)


def test_function_header_tuple():
    tup = (2, 3, 4)
    # function_header_tuple()                               # OK => print: ()
    # function_header_tuple(3, 5, 6, 8)                     # OK
    # function_header_tuple(3, 'fsfs', 4.6, 8)              # OK
    # function_header_tuple(3, 'fsfs', 4.6, 8, a=9)         # ERROR:  got an unexpected keyword argument 'a'
    # function_header_tuple(args='hungnv132')               # ERROR:  got an unexpected keyword argument 'args'
    function_header_tuple(tup)                     # OK: but 'tup' variable as a element in tuple => print: ((2, 3, 4),)


def function_header_dict(**args):
    print('Type of Name: %s' % type(args))  # Dict
    print(args)


def test_function_header_dict():
    # function_header_dict()            # OK => print: {}
    # function_header_dict(6)           # ERROR:   takes 0 positional arguments but 1 were give
    # function_header_dict(6, 8)        # ERROR:   takes 0 positional arguments but 2 were given
    # function_header_dict(a=4)         # OK => print: {'a': 4}
    # function_header_dict(a=4, b=8)    # OK => print: {'a': 4, 'b': 8}
    function_header_dict(6, a=4, b=8)   # ERROR:   takes 0 positional arguments but 1 were give


if __name__ == '__main__':
    test_function_header_dict()
