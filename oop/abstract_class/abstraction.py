from abc import ABCMeta, abstractmethod


"""
+ abstractmethod: 
 - require subclasses must implement abstract methods
   if not, raise an Exception
 - requires that the metaclass is ABCMeta or derived from it. 
"""


class Vehicle(metaclass=ABCMeta):

    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):

    # if not override, raise an Exception.
    def move(self):
        print("Car is moving.")


if __name__ == "__main__":
    car = Car()
    car.move()
