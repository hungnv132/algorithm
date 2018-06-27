
def call_method_on_parent_class():
    """
    - Problem: You want to invoke a method in a parent class in place of a
    method that has been overridden in a subclass.
    - Solution: use the super() function.
    """

    class A(object):

        def spam(self):
            print("A.spam")

    class B(A):

        def spam(self):
            print("B.spam")
            super().spam()  # Call parent spam()

    b = B()
    b.spam()
    # B.spam
    # A.spam

    print("==================== 2")

    class Proxy(object):

        def __init__(self, obj):
            self._obj = obj

        # Delegate attribute lookup to internal obj
        def __getattr__(self, key):
            return getattr(self._obj, key)

        # Delegate attribute assignment
        def __setattr__(self, key, value):
            if key.startswith('_'):
                # Call original __setattr__
                super(Proxy, self).__setattr__(key, value)
            else:
                setattr(self._obj, key, value)


if __name__ == '__main__':
    call_method_on_parent_class()
