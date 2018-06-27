def define_interface_and_abstrace_class():
    """
    - Problem:  You want to define a class that serves as an interface or abstract
    base class from which you can perform type checking and ensure that certain
    methods are implemented in subclass.
    - Solution: user the `abc` module.
    """

    from abc import ABCMeta, abstractmethod

    class IStream(metaclass=ABCMeta):

        @abstractmethod
        def read(self, maxbytes=-1):
            pass

        @abstractmethod
        def write(self, data):
            pass

    class SocketStream(IStream):

        def read(self, maxbytes=-1):
            print("Socket Stream is reading data")

        def write(self, data):
            print("Socket Stream is writing data")


if __name__ == "__main__":
    define_interface_and_abstrace_class()