
def create_managed_attributes():
    """
    - Problem: You want to add extra processing (e.g type checking or validation)
    to the getting or setting of an instance attribute.
    - Solution: A simple way to customize access to an attribute is to define
     it as a “property.”
    """
    print("====================== 1 ")

    class Person(object):

        def __init__(self, first_name):
            self.first_name = first_name

        # Getter function
        @property
        def first_name(self):
            return self._first_name

        # Setter function
        @first_name.setter
        def first_name(self, value):
            if not isinstance(value, str):
                raise TypeError('Expected a string')
            self._first_name = value

        # Deleter function (optional)
        @first_name.deleter
        def first_name(self):
            raise AttributeError("Can't delete attribute")

    a = Person('Hung')
    print(a.first_name)  # Hung

    # a.first_name = 88  # TypeError: Expected a string
    a.first_name = 'ABC'
    print(a.first_name)  # ABC

    # del a.first_name  # AttributeError: Can't delete attribute

    print("====================== 2 ")
    # Next example:
    # Properties can also be defined for existing get and set methods.

    class Person_v2(object):

        def __init__(self, first_name):
            self.set_first_name(first_name)

        # Getter function
        def method_first_name(self):
            return self._first_name

        # Setter function
        def set_first_name(self, value):
            if not isinstance(value, str):
                raise TypeError("Expected a string")
            self._first_name = value

        # Deleter function (Optional)
        def del_first_name(self):
            raise AttributeError("Can't delete this attribute.")

        # Make a property from existing get/set methods
        first_name = property(method_first_name, set_first_name, del_first_name)

    print(Person_v2.first_name.fget)
    print(Person_v2.first_name.fset)
    print(Person_v2.first_name.fdel)
    # <function create_managed_attributes.<locals>.Person_v2.get_first_name at 0x7fc9b732eae8>
    # <function create_managed_attributes.<locals>.Person_v2.set_first_name at 0x7fc9b732eb70>
    # <function create_managed_attributes.<locals>.Person_v2.del_first_name at 0x7fc9b732ebf8>

    b = Person_v2('XYZ')
    print(b.first_name)  # XYZ

    b.first_name = 'QWERTY'
    print(b.first_name)  # QWERTY

    # Don’t write properties that don’t actually add anything extra like
    # Person_v3.

    class Person_v3:
        def __init__(self, first_name):
            self.first_name = first_name

        @property
        def first_name(self):
            return self._first_name

        @first_name.setter
        def first_name(self, value):
            self._first_name = value

    print("====================== 3")
    # Properties can also be a way to define computed attributes.
    import math

    class Circle:

        def __init__(self, radius):
            self.radius = radius

        @property
        def area(self):
            return math.pi * self.radius * 2

        @property
        def perimeter(self):
            return 2 * math.pi * self.radius

    c = Circle(8)
    print(c.radius)     # 8
    print(c.area)       # 50.26548245743669
    print(c.perimeter)  # 50.26548245743669


if __name__ == '__main__':
    create_managed_attributes()