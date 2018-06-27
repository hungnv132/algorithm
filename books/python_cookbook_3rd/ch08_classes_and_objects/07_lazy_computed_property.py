
def lazily_computed_properties():
    """
     - Problem: Define a read-only attribute as a property that only gets computed
    on access. However, once accessed, you'd like the value to be cached and 
    not recomputed on each access.
    - Solution: Define a lazy attribute through the use a descriptor class.
    """

    class lazyproperty(object):
        
        def __init__(self, func):
            self.func = func
        
        def __get__(self, instance, cls):
            if instance is None:
                return self
            else:
                value = self.func(instance)
                setattr(instance, self.func.__name__, value)
                return value

    import math

    class Circle(object):

        def __init__(self, radius):
            self.radius = radius

        @lazyproperty
        def area(self):
            print("computing area")
            return math.pi * self.radius * 2

    c = Circle(2)
    print(c.area)
    print(c.area)
    c = Circle(3)
    print(c.area)


if __name__ == "__main__":
    lazily_computed_properties()